from fastapi import FastAPI, Query
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
import httpx

app = FastAPI()

REMOTE_MODEL_URL = "http://localhost:11434/api/chat"

@app.get("/chat")
async def chat_stream(message: str = Query(...)):
    """Stream responses from the remote model server."""
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

# Mount static files
app.mount("/", StaticFiles(directory="static", html=True), name="static")