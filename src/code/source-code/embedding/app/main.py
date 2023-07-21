from fastapi import FastAPI
import uvicorn
from schema import EmbeddingRequest, EmbeddingResponse, SimilarityResponse
import service
app = FastAPI()


@app.post("/encode", response_model=EmbeddingResponse)
async def encode(request: EmbeddingRequest):
    return {
        "embeddings": service.encode(request.sentences).tolist()
    }


@app.post("/similarity", response_model=SimilarityResponse)
async def similarity(request: EmbeddingRequest):
    return {
        "score": service.compute_similarity(request.sentences)
    }


uvicorn.run(app, host="0.0.0.0", port=8000)
