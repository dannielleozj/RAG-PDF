# RAG-PDF-Mistral Project

The RAG-PDF Evaluation Project is designed to manage and query a database of PDF using Retrieval-Augmented Generation (RAG) with the Mistral LLM model. It includes scripts for populating the database, querying the model, and evaluating its performance through unit tests.

This project runs locally using Ollama and Langchain.

## Project Structure

- `eval.py`: Contains the main evaluation functions and helper methods.
- `query.py`: Contains the functions to query the RAG model.
- `populate_database.py`: Contains functions to populate the database with necessary data.
- `test_eval.py`: Contains the unit tests for the evaluation functions.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/rag-pdf-evaluation.git
   cd rag-pdf-evaluation
