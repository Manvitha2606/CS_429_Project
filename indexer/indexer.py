# basic_indexer.py
import re

documents = [
    "Python is a great language.",
    "Language processing is essential for Python.",
    "Great minds think alike."
]

def create_inverted_index(docs):
    inverted_index = {}
    for idx, doc in enumerate(docs):
        words = re.findall(r'\w+', doc.lower())
        for word in words:
            if word in inverted_index:
                inverted_index[word].add(idx)
            else:
                inverted_index[word] = {idx}
    return inverted_index

if __name__ == "__main__":
    index = create_inverted_index(documents)
    print(index)
