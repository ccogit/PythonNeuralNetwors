# PythonNeuralNetwors

Code, notebooks, and notes as I work through **"Deep Learning with Python, Third Edition"** by François Chollet (Manning Publications).

> ⚠️ This repo is just getting started. Right now it contains material for chapter 2 only; more chapters will be added as I work through the book.

## 📖 About the Book

"Deep Learning with Python" is one of the standard introductions to neural networks, written by the creator of Keras. The third edition has been thoroughly revised and covers, among other topics:

- Keras 3 with multi-backend support (TensorFlow, JAX, PyTorch)
- Modern architectures including Transformers
- Generative models
- Practical workflows, training, and deployment

Author: **François Chollet** · Publisher: Manning Publications

## 🎯 Goals of This Repo

- Work through the book's code examples myself instead of just reading along
- Add my own notes, explanations, and small experiments
- Build up a personal reference for neural networks with Python

## 📂 Current Structure

```
.
└── Ch2/    # Chapter 2 – Mathematical foundations of neural networks
```

More chapters will land here as I progress.

## 🛠️ Requirements

- Python 3.10+
- Keras 3.x
- A backend: TensorFlow, JAX, or PyTorch
- NumPy, Matplotlib
- Jupyter (if you want to run notebooks)

### Quick Setup

```bash
git clone https://github.com/ccogit/PythonNeuralNetwors.git
cd PythonNeuralNetwors

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install keras tensorflow numpy matplotlib jupyter
```

### Selecting a Keras 3 Backend

```bash
export KERAS_BACKEND="tensorflow"   # default
# export KERAS_BACKEND="jax"
# export KERAS_BACKEND="torch"
```

## 📚 Progress

| Chapter | Topic | Status |
|---------|-----------------------------------------------|--------|
| 1 | What is deep learning? | ⬜ |
| 2 | Mathematical foundations of neural networks | 🟡 In progress |
| 3 | Introduction to Keras and TensorFlow | ⬜ |
| 4+ | … | ⬜ |

> Legend: ✅ done · 🟡 in progress · ⬜ open

## 🤝 Copyright Notice

The book's content is protected by copyright. This repository contains **no text from the book itself** — only my own code (inspired by the examples) and my own notes. If you want to learn deep learning seriously, get the book from [Manning](https://www.manning.com/books/deep-learning-with-python-third-edition) or your preferred bookseller.

## 🔗 Links

- [Manning – Deep Learning with Python, Third Edition](https://www.manning.com/books/deep-learning-with-python-third-edition)
- [Keras documentation](https://keras.io/)
- [François Chollet on GitHub](https://github.com/fchollet)