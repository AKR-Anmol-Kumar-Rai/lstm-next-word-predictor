# 🧠 LSTM Next Word Predictor

<p align="center">

  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/PyTorch-LSTM-ee4c2c?style=for-the-badge&logo=pytorch" />
  <img src="https://img.shields.io/badge/NLP-Natural%20Language%20Processing-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Streamlit-Deployed-red?style=for-the-badge&logo=streamlit" />
  <img src="https://img.shields.io/badge/Docker-Containerized-blue?style=for-the-badge&logo=docker" />

</p>

<p align="center">
  <b>An end-to-end NLP application for predicting the next word using a trained LSTM neural network.</b>
</p>

<p align="center">
  <b>Created by Anmol Kumar Rai</b>
</p>

---

## 🚀 Live Demo

<p align="center">

### 🌐 Try the Model

<a href="https://lstm-next-word-predictor01.streamlit.app/">
  <img src="https://img.shields.io/badge/🚀%20LIVE%20DEMO-Streamlit-red?style=for-the-badge" />
</a>

</p>

🔗 **Application:**  
https://lstm-next-word-predictor01.streamlit.app/

---

# 📌 Project Overview

**LSTM Next Word Predictor** is a word-level Natural Language Processing project that uses a **Long Short-Term Memory (LSTM)** neural network to predict the most likely next word in a given sentence.

The application provides an interactive **Streamlit web interface** where users can enter a sentence and receive a predicted next word from the trained model.

Unlike simply creating a traditional machine learning classifier, this project implements a complete **sequence modeling pipeline**, starting from raw text preprocessing and vocabulary creation all the way to model training, model serialization, inference, and cloud deployment.

---

# 🎯 What Does This Project Do?

The application takes a sequence of words entered by the user and attempts to predict what word is most likely to come next based on the patterns learned during training.

### Example

**User Input:**

```text
I am learning
