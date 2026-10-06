# My Product Sentiment Analyzer Backend

## Run
1. Open PowerShell in this folder.
2. Create a virtual environment:
   `python -m venv venv`
3. Activate it:
   `.env\Scripts\Activate.ps1`
4. Install packages:
   `pip install -r requirements.txt`
5. Start the server:
   `python app.py`

API:
POST http://127.0.0.1:5000/api/analyze

Request JSON:
{
  "url": "https://example.com/product"
}

The backend uses Flask, Selenium, JSON-LD product data, and VADER sentiment analysis.
