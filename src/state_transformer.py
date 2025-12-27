
import numpy as np

class EmbeddingTransformer:
    def __init__(self, target_dim=384):
        self.target_dim = target_dim

    def transform(self, embeddings):
        transformed = []
        for e in embeddings:
            e = np.array(e)
            if e.shape[0] > self.target_dim:
                e = e[:self.target_dim]
            else:
                pad = self.target_dim - e.shape[0]
                e = np.pad(e, (0, pad))
            transformed.append(e.astype('float32'))
        return transformed
