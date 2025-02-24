# LL Example

## Description

This project is an basic API based on Django and Django REST Framework (DRF) that allows the user to interact with Hugging Face natural language models (LLMs). The API exposes an endpoint that receives input text and generates a response using a natural language processing (NLP) model.

## Objectives

- Build a REST API with Django + DRF.
- Integrate a Hugging Face language model to generate natural language responses.
- Expose a /chat/ endpoint where users send messages and receive AI-generated responses.
- Allow local execution for testing and development.

## Tech's used

- Python
- Django (web Framework)
- Django REST Framework (For bulding REST API)
- Transformers (Hugging Face) (for natural language model)

## Instalation and running steps:

1. Clone repo
```
git clone https://github.com/hanoirocker/llm_example.git
cd llm_example
```
2. Create and active virtual environment
```
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```
3. Install dependencies
```
pip install -r requirements.txt
```
4. Run local dev server
```
python manage.py runserver
```
5. Test API by accesing `http://127.0.0.1:8000/api/chat/`
