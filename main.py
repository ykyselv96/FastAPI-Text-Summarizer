from fastapi import FastAPI, Request
import uvicorn
from langchain_openai import ChatOpenAI
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain

from core.config import settings

app = FastAPI()

@app.post("/summarize")
async def summarize(request: Request):
    data = await request.json()
    text = data.get("text", "")

    llm = ChatOpenAI(temperature=0, openai_api_key=settings.openai_api_key)

    text_splitter = CharacterTextSplitter()
    texts = text_splitter.split_text(text)

    docs = [Document(page_content=t) for t in texts]

    chain = load_summarize_chain(llm, chain_type='map_reduce')
    summary = chain.invoke(docs)
    return {"summary": summary}


if __name__ == "__main__":
    uvicorn.run(app, host=settings.app_host, port=int(settings.app_port), reload=True)
