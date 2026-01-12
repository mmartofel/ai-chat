
export MODEL_SERVER_URL="http://localhost:11434/api/chat"

uvicorn app:app \
  --host 0.0.0.0 \
  --port 8000 \
  --reload
