# AI Sales Deck Builder

This project uses Crew AI to generate sales decks. It leverages a team of AI agents, each with a specific role, to research, analyze, and create a compelling sales presentation.

## Features

- **Four AI Agents:**
    - **Market Researcher:** Researches the product and market.
    - **Sales Analyst:** Analyzes the product from a sales perspective.
    - **Media Relations Specialist:** Crafts a compelling narrative.
    - **Master Sales Deck Writer:** Creates the final sales deck.
- **RAG System:** Uses `crewai_tools` to provide the researcher agent with information from any documents in a specified directory.
- **Local LLM Integration:** Configured to use local models via Ollama.

## Setup

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up Ollama:**
   - Make sure you have Ollama installed and running.
   - Pull the `openhermes` and `gemma3` models:
     ```bash
     ollama pull openhermes:latest
     ollama pull gemma3:latest
     ```

3. **Set Environment Variables:**
   - Create a `.env` file in the root of the project.
   - Add your Serper API key to the `.env` file in the following format:
     ```
     SERPER_API_KEY="YOUR_SERPER_API_KEY"
     ```
   - You can get a free API key from [serper.dev](https://serper.dev).

4. **Add your Product Information:**
   - Place your product information files (PDF, DOCX, TXT, etc.) in the `Place product description here` directory.

## Usage

To run the sales deck generator, execute the following command from the `sales-deck-generator` directory:

```bash
python -m src.main
```
