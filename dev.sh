
#!/bin/bash
# Update environment variables as needed to reflect your model server configuration
#
# export MODEL_SERVER_URL="http://localhost:11434/api/chat"
# export MODEL_NAME="mistral"

# initiate virtual environment 
python3 -m venv .venv
source .venv/bin/activate

# upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt

uvicorn app:app \
  --host 0.0.0.0 \
  --port 8000 \
  --reload
