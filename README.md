# ai-chat

initiate environment:

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

Update dev.sh file with proper environment variables as needed to reflect your model server configuration.

export MODEL_SERVER_URL="http://localhost:11434/api/chat"
export MODEL_NAME="mistral"


Development:

./dev.sh

Deployment on OpenShift:

oc apply -k ./deployment/ui


