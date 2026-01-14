FROM nvcr.io/nvidia/pytorch:24.02-py3

WORKDIR /app

# IMPORTANT: ensure we are root at build time
USER root

# Upgrade pip in the active Python environment
#RUN python3 -m pip install --no-cache-dir --upgrade pip

# CRITICAL: downgrade NumPy in the REAL runtime environment
#RUN python3 -m pip install --no-cache-dir --force-reinstall "numpy<2"

# Install vLLM AFTER NumPy is fixed
#RUN python3 -m pip install --no-cache-dir vllm

# OpenShift compatibility: allow arbitrary UID
RUN chmod -R g=u /usr/local /opt

EXPOSE 8080

# DO NOT set ENTRYPOINT or CMD
