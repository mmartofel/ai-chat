FROM nvidia/cuda:13.1.0-runtime-ubi9

WORKDIR /app

RUN dnf update -y && dnf install -y python3 python3-pip
COPY requirements-vllm.txt .
RUN pip install --no-cache-dir -r requirements-vllm.txt

EXPOSE 8080
CMD ["python3", "-m", "vllm.entrypoints.openai.api_server","--model","TinyLlama/TinyLlama-1.1B-Chat-v1.0","--host", "0.0.0.0", "--port", "8080"]