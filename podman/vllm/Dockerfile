FROM nvcr.io/nvidia/pytorch:24.02-py3

WORKDIR /app

# Ensure pip is up to date
RUN pip install --no-cache-dir --upgrade pip

# CRITICAL: NumPy compatibility
RUN pip install --no-cache-dir "numpy<2"

# Install vLLM after NumPy is pinned
RUN pip install --no-cache-dir vllm

# Expose API port
EXPOSE 8080
