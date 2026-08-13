import nltk
from nltk import word_tokenize
import torch
import torch.nn as nn
import pickle
from functions.text_to_indices import text_to_indices
from functions.tokens_generator import token_generator





device = torch.device("cuda" if torch.cuda.is_available() else "cpu")



with open("model/vocab.pkl", "rb") as f:
    vocab = pickle.load(f)

# -----------------------------
# Load parameters
# -----------------------------

with open("model/parameters.pkl", "rb") as f:
    parameters = pickle.load(f)

max_len = parameters["max_len"]
# -----------------------------
# LSTM model
# -----------------------------

class LSTMModel(nn.Module):

    def __init__(self, vocab_size, embedding_dim, hidden_size):
        super().__init__()

        self.embedding = nn.Embedding(
            vocab_size,
            embedding_dim
        )

        self.lstm = nn.LSTM(
            embedding_dim,
            hidden_size,
            batch_first=True
        )

        self.fc = nn.Linear(
            hidden_size,
            vocab_size
        )

    def forward(self, x):

        embedded = self.embedding(x)

        _, (hidden, cell) = self.lstm(embedded)

        hidden = hidden[-1]

        output = self.fc(hidden)

        return output


# -----------------------------
# Create model
# -----------------------------

model = LSTMModel(
    vocab_size=parameters["vocab_size"],
    embedding_dim=parameters["embedding_dim"],
    hidden_size=parameters["hidden_size"]
)


# -----------------------------
# Load trained weights
# -----------------------------

state_dict = torch.load(
    "model/lstm_next_word_predictor.pth",
    map_location=device
)

model.load_state_dict(state_dict)

model.to(device)
model.eval()

def load_model():
    return model

def load_vocab():
    return vocab


def prediction(model, vocab, text):

    # tokenize
    tokenized_text = word_tokenize(text.lower())
    
    # text -> numerical
    numerical_text = text_to_indices(tokenized_text, vocab)
    
    # padding
    padded_text = torch.tensor([0]*(max_len -len(numerical_text)) + numerical_text, dtype = torch.long).unsqueeze(0)  #model take input as batch_size(no. of sentence),no.of words in a sentence

    # send to model
    with torch.no_grad():
        output = model(padded_text.to(device))

        # predicted word index
        _, index = torch.max(output, dim=1)

    # merge with the text
    return text +" "+list(vocab.keys())[index]

    