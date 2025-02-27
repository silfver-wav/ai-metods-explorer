from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI
app = FastAPI(title="AI Methods Explorer")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define data models
class TextInput(BaseModel):
    text: str

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "AI Methods Explorer API"}

# AI processing endpoint
@app.post("/api/summarize")
async def summarize_text(input_data: TextInput):
    # Simple integration with Hugging Face Inference API
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Authorization": f"Bearer {os.getenv('HF_API_KEY', '')}"}
    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json={"inputs": input_data.text, "parameters": {"max_length": 100}}
        )

        return {"result": response.json()[0]["summary_text"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/sentiment_analysis")
async def sentiment_analysize_text(input_data: TextInput):
    # Simple integration with Hugging Face Inference API
    API_URL = "https://api-inference.huggingface.co/models/tabularisai/multilingual-sentiment-analysis"
    headers = {"Authorization": f"Bearer {os.getenv('HF_API_KEY', '')}"}

    print(input_data.text)
    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json=input_data.text
        )

        print(response)

        return {"result": response.json()[0]["sentiment"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/ner")
async def named_entity_recognition(input_data: TextInput):
    API_URL = "https://api-inference.huggingface.co/models/dslim/bert-base-NER"
    headers = {"Authorization": f"Bearer {os.getenv('HF_API_KEY', '')}"}
    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json={"inputs": input_data.text}
        )
        entities = response.json()  # Expected to return a list of recognized entities
        return {"entities": entities}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))