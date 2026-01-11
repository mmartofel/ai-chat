from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import StreamingResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import httpx
import json

app = FastAPI()

REMOTE_MODEL_URL = "http://localhost:11434/api/chat"  # Replace with the actual URL of the remote model server

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: ChatRequest):
    async def stream():
        try:
            async with httpx.AsyncClient() as client:
                async with client.stream("POST", REMOTE_MODEL_URL, json={"message": req.message}) as response:
                    response.raise_for_status()  # Raise an exception for HTTP errors
                    async for line in response.aiter_lines():
                        yield f"data: {line}\n\n"
        except httpx.RequestError as e:
            raise HTTPException(status_code=503, detail=f"Remote model server is unreachable: {e}")
        except httpx.HTTPStatusError as e:
            # Read the response content before accessing it
            error_content = await e.response.aread()
            raise HTTPException(status_code=e.response.status_code, detail=f"Error from remote model server: {error_content.decode('utf-8')}")

    return StreamingResponse(stream(), media_type="text/event-stream")

@app.get("/chat")
async def chat_stream(message: str = Query(...)):
    async def stream():
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                async with client.stream("POST", REMOTE_MODEL_URL, json={
                    "model": "mistral",
                    "messages": [
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": message}
                    ]
                }) as response:
                    if response.status_code != 200:
                        error_content = await response.aread()
                        yield f"data: {{\"error\": \"Remote model server returned an error: {error_content.decode('utf-8')}\"}}\n\n"
                    else:
                        async for line in response.aiter_lines():
                            if line.strip():
                                yield f"data: {line}\n\n"
        except httpx.RequestError as e:
            yield f"data: {{\"error\": \"Backend cannot reach the remote model server: {str(e)}\"}}\n\n"
        except Exception as e:
            yield f"data: {{\"error\": \"An unexpected error occurred: {str(e)}\"}}\n\n"

    return StreamingResponse(stream(), media_type="text/event-stream")


app.mount("/", StaticFiles(directory="static", html=True), name="static")