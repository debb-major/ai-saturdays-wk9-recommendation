from fastapi import FastAPI
from recommender import recommend_books, recommend_by_keywords

app = FastAPI()

# API Endpoints
@app.get("/")
def home():
    return {"message": "Welcome to the Book Recommender API"}

@app.get("/recommend/title")
def recommend_by_title(title: str, top_n: int = 5):
    results = recommend_books(title, top_n)
    return {
        "query": title,
        "results": results.to_dict(orient="records")  # Convert DataFrame to list of dicts
    }

@app.get("/recommend/keywords")
def recommend_by_kw(keywords: str, top_n: int = 5):
    results = recommend_by_keywords(keywords, top_n)
    return {
        "query": keywords,
        "results": results.to_dict(orient="records")  # Same here
    }