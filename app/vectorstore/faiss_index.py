import faiss
import numpy as np
import pickle
import os

class FaissIndex:
    def __init__(self, dim, index_path="app/data/index/faiss.index"):
        self.dim = dim
        self.index_path = index_path

        if os.path.exists(index_path):
            self.index = faiss.read_index(index_path)
        else:
            self.index = faiss.IndexFlatIP(dim)

        self.metadata = []

    def add(self, vectors, metadata):
        self.index.add(np.array(vectors).astype("float32"))
        self.metadata.extend(metadata)

    def search(self, vector, k=10):
        D, I = self.index.search(vector.reshape(1, -1).astype("float32"), k)
        return D[0], I[0]

    def save(self):
        faiss.write_index(self.index, self.index_path)
        with open(self.index_path + ".meta", "wb") as f:
            pickle.dump(self.metadata, f)