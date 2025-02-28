# AI Methods Explorer
A full-stack application capable of performing Summarization and Named Entity Recognition (NER) on text.

## Implementation
The backend is built with Python using FastAPI, while the AI models are powered by the Hugging Face API. The frontend is developed using Next.js.

### Backend
The backend provides two endpoints:
* Summarization
* Named Entity Recognition (NER)
  
Each endpoint extracts text from the incoming POST request and forwards it to the Hugging Face API. The processed response is then sent back to the frontend for display.

### Frontend
The frontend features a single text input field where users can either:
* Summarize the text
* Extract named entities

Once a request is submitted, the processed response is displayed below the input field.

## Challenges
The only challenge I faced with this project was communicating with huggingface api.
