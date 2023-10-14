from sentence_transformers import SentenceTransformer

class SentenceEncoder:
    def __init__(self) -> None:
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def encode(self, sentences):
        sentence_embeddings = self.model.encode(sentences)
        return sentence_embeddings