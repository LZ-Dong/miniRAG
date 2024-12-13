import numpy as np
from transformers import AutoModel
from numpy.linalg import norm
from typing import List

class Jinaembedding:
    def __init__(self, path:str='jinaai/jina-embeddings-v2-base-zh'):
        self.path = path
        self.embedding_model=AutoModel.from_pretrained('jinaai/jina-embeddings-v2-base-zh', trust_remote_code=True) 
    
    def get_embedding(self,content:str=''):
        return self.embedding_model.encode([content])[0]
    
    def compare(self, text1: str, text2: str):
        
        cos_sim = lambda a,b: (a @ b.T) / (norm(a)*norm(b))
        embeddings = self.embedding_model.encode([text1, text2])
        return cos_sim(embeddings[0], embeddings[1])

    def compare_v(cls, vector1: List[float], vector2: List[float]) -> float:
        dot_product = np.dot(vector1, vector2)
        magnitude = np.linalg.norm(vector1) * np.linalg.norm(vector2)
        if not magnitude:
            return 0
        return dot_product / magnitude