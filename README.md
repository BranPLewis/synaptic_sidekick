# Synaptic Sidekick

A machine learning research assistant that helps answer ML-related questions using document retrieval and web search capabilities.

## Setup

1. Set up the virtual environment (optional but recommended):
```bash
python -m venv syn_side
source syn_side/bin/activate  # On macOS/Linux
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Code

1. To ingest PDF documents (if you have any research papers to add):
```bash
python ingestion/ingest_pdfs.py
```

2. To run the research assistant:
```bash
python run_agent.py "Your question here"
```

Example question:
```bash
python run_agent.py "How does a convolutional neural network (CNN) differ from a recurrent neural network (RNN)?"
```

The agent will search through relevant machine learning resources and provide a detailed answer combining information from the ingested documents and trusted ML websites.
