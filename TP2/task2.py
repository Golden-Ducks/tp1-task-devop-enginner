import re


def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text.split()


def add_padding(tokens):
    return ["<s>"] + tokens + ["</s>"]


def extract_windows(tokens, window_size=1):
    windows = []
    for i in range(window_size, len(tokens) - window_size):
        window = tokens[i-window_size : i+window_size+1]
        windows.append(" ".join(window))
    return windows


def build_vocab(all_windows):
    vocab_list = sorted(set(all_windows))
    return {w: i for i, w in enumerate(vocab_list)}


def vectorize_doc(doc_windows, vocab):
    vector = [0] * len(vocab)
    for w in doc_windows:
        if w in vocab:
            vector[vocab[w]] = 1
    return vector



D1 = "I love cats"
D2 = "Cats are chill"
D3 = "I am late"

all_docs = [D1, D2, D3]


all_windows = []
docs_windows = []

for doc in all_docs:
    tokens = preprocess_text(doc)
    tokens = add_padding(tokens)
    windows = extract_windows(tokens, window_size=1)

    docs_windows.append(windows)
    all_windows.extend(windows)


vocab = build_vocab(all_windows)


vectors = []
for w in docs_windows:
    vectors.append(vectorize_doc(w, vocab))


for k in vocab.items():
    print(k)


for i, vec in enumerate(vectors):
    print(f"D{i+1}:", vec)
