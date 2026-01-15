# AI Chat Application

A real-time chat application with a FastAPI backend and a modern web frontend that streams responses from an AI language model (Ollama) in a typewriter-style format.

## Features

- Real-time chat interface with streaming responses
- Markdown rendering for code blocks and formatting
- Syntax highlighting for code snippets
- Conversation history
- Responsive design using Tailwind CSS
- Easy configuration via environment variables

## Prerequisites

- Python 3.11+
- Node.js (for frontend dependencies)
- [Ollama](https://ollama.ai/) running locally (default: http://localhost:11434)
- Git (optional)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-chat-windsurf.git
   cd ai-chat-windsurf
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install frontend dependencies (Marked.js and Highlight.js are loaded via CDN)

## Configuration

Create a `.env` file in the project root with the following variables:

```env
# Ollama configuration
LLM_API_URL=http://localhost:11434/v1
LLM_API_KEY=no-key-required  # No API key needed for local Ollama
LLM_MODEL=mistral  # Or your preferred model
```

## Running the Application

1. Start the Ollama server (if not already running):
   ```bash
   ollama serve
   ```

2. In a new terminal, start the FastAPI application:
   ```bash
   ./dev.sh
   ```
   or manually:
   ```bash
   uvicorn app:app --reload --host 0.0.0.0 --port 8000
   ```

3. Open your browser and navigate to:
   ```
   http://localhost:8000
   ```

## Project Structure

```
ai-chat-windsurf/
├── app.py                # FastAPI application
├── requirements.txt      # Python dependencies
├── static/
│   ├── index.html        # Frontend HTML
│   ├── app.js            # Frontend JavaScript
│   └── style.css         # Custom styles
└── .env.example         # Example environment variables
```

## Environment Variables

| Variable      | Default Value               | Description                           |
|---------------|-----------------------------|---------------------------------------|
| LLM_API_URL   | http://localhost:11434/v1   | Base URL for the Ollama API           |
| LLM_API_KEY   | no-key-required             | API key (not needed for local Ollama) |
| LLM_MODEL     | mistral                     | Default model to use                  |

## Development

- The application uses hot-reload for development. Any changes to Python files will automatically restart the server.
- Frontend assets are served from the `static` directory.
- The chat interface is built with vanilla JavaScript and uses Tailwind CSS for styling.

## Troubleshooting

1. **Streaming not working**:
   - Ensure Ollama is running and accessible at the specified URL
   - Check browser console for JavaScript errors
   - Verify the API responses in the terminal where the FastAPI server is running

2. **Static files not loading**:
   - Make sure the `static` directory exists and contains the necessary files
   - Check the browser's network tab for 404 errors

3. **Model not found**:
   - Ensure the specified model is available in your Ollama installation
   - Pull the model: `ollama pull mistral`

## License

[MIT](LICENSE) - Feel free to use this project for any purpose.