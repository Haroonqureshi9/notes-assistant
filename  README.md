# Notes Assistant

A terminal AI assistant built with Python and the Gemini API. Ask it questions and get answers streamed back word-by-word, like a real chat app.

## Features

- Streaming responses (text appears as it's generated)
- Automatic retry when the API is busy
- Interactive loop — ask question after question until you type `quit`

## Built with

- Python 3
- google-genai (Gemini API, model `gemini-2.5-flash`)

## Structure

- `main.py` — the interactive loop
- `ai.py` — handles talking to the Gemini API
- `config.py` — holds the API key (not tracked in git)

## Setup

1. Install the library: `pip3 install google-genai`
2. Create a `config.py` file with your key: `API_KEY = "your-key-here"`
3. Run it: `python3 main.py`