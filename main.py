import uvicorn
from core.config import settings
from langchain_huggingface import HuggingFaceEndpoint
from fastapi import FastAPI, Request



app = FastAPI()


summarizer = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    token=settings.huggingfacehub_api_token,
    task="summarization"
)

def summarize(text: str) -> str:
    response = summarizer(
        prompt=text,
        max_new_tokens=100,
        do_sample=False
    )
    return response

@app.post("/summarize")
async def summarize_endpoint(request: Request):
    data = await request.json()
    text = data.get("text", "")
    summary = summarize(text)
    return {"summary": summary}


if __name__ == "__main__":
    uvicorn.run(app, host=settings.app_host, port=int(settings.app_port), reload=True)
