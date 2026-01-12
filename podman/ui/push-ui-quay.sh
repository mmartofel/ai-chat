#!/bin/bash

podman tag localhost/ai-chat-ui:latest quay.io/mmartofe/ai-chat-ui:latest

podman push quay.io/mmartofe/ai-chat-ui:latest

echo "Pushed ai-chat-ui to Quay.io"