import pickle

with open("model/vocab.pkl", "rb") as f:
    vocab = pickle.load(f)

def text_to_indices(sentence, vocab):
    numerical_sentence = []

    for token in sentence:
        if token in vocab:
            numerical_sentence.append(vocab[token])
        else:
             numerical_sentence.append(vocab['<unk>'])

    return numerical_sentence
