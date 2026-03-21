# Class 1: Sports & Athletics (Context: Winning/Medals)
doc1 = "The gold medal price is high effort"
doc2 = "Winning a gold medal needs a high jump"
doc3 = "Market for a gold medal is a trade of sweat"
doc4 = "The athlete will trade all for a gold medal"

# Class 2: Finance & Economy (Context: Market/Investment)
doc5 = "The gold bars price is high today"
doc6 = "Investing in gold bars needs a high rate"
doc7 = "Market for gold bars is a trade of money"
doc8 = "The bank will trade all for gold bars"

import re
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
# Your Task: Fill these functions
def preprocess_text(text):
    """
    Make sure to lowercase and remove punctuation.
    """
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text.split()


def vectorize(docs, n_gram_size=1):
    
    def generate_ngrams(tokens, n):
        return [" ".join(tokens[i:i+n]) for i in range(len(tokens)-n+1)]
    
    all_ngrams = []
    docs_ngrams = []

    for doc in docs:
        tokens = preprocess_text(doc)
        ngrams = generate_ngrams(tokens, n_gram_size)
        docs_ngrams.append(ngrams)
        all_ngrams.extend(ngrams)

    
    vocab = sorted(set(all_ngrams))

   
    vectors = []
    for ngrams in docs_ngrams:
        vector = [ngrams.count(v) for v in vocab]
        vectors.append(vector)

    return np.array(vectors)



# Training / Clustering

all_docs = [doc1, doc2, doc3, doc4, doc5, doc6, doc7, doc8]

# 1-gram Experiment
X1 = vectorize(all_docs, n_gram_size=1)
km1 = KMeans(n_clusters=2, random_state=42).fit(X1)
pred1 = km1.labels_

# 2-gram Experiment
X2 = vectorize(all_docs, n_gram_size=2)
km2 = KMeans(n_clusters=2, random_state=42).fit(X2)
pred2 = km2.labels_


# Compare accuracy and precision

# True labels (0 = sports, 1 = finance)
true_labels = [0,0,0,0,1,1,1,1]


def best_accuracy(true, pred):
    acc1 = accuracy_score(true, pred)
    acc2 = accuracy_score(true, [1-p for p in pred])
    return max(acc1, acc2)

acc1 = best_accuracy(true_labels, pred1)
acc2 = best_accuracy(true_labels, pred2)


print(f"1-gram clusters: {pred1}")
print(f"2-gram clusters: {pred2}")
print(f"1-gram accuracy: {acc1}")
print(f"2-gram accuracy: {acc2}")
