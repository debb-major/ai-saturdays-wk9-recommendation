# Book Recommender System

A simple content-based **Book Recommendation System** built with **FastAPI** and **scikit-learn**.  
You can get book recommendations either by **title** or by **keywords**.


## Project Structure
```
ai-saturdays-wk9-recommendation
 ├── app.py            # FastAPI app
 ├── recommender.py    # Recommendation logic
 ├── book.csv             # Dataset
 └── book-recommendation.ipynb    # Jupyter notebook experiments
```
## Setup

1. Clone this repo:
   ```bash
   git clone https://github.com/debb-major/ai-saturdays-wk9-recommendation.git
   cd ai-saturdays-wk9-recommendation
   ```
2. Install requirements:
   ```bash
   pip install fastapi uvicorn pandas scikit-learn numpy
   ```
3. Run the API:
   ```bash
   uvicorn app:app --reload
   ```
## API Endpoints
**Root**
`GET /`
- Returns a welcome message.

Recommend by Title

`GET /recommend/title?title=Book+Title&top_n=5`

Example:
```
http://127.0.0.1:8000/recommend/title?title=Harry%20Potter&top_n=3
```

Recommend by Keyword

`GET /recommend/keywords?keywords=magic+adventure&top_n=5`

Example:
```
http://127.0.0.1:8000/recommend/keywords?keywords=romance+space&top_n=3
```

## Notes

- `app.py` runs the API.
- `recommender.py` contains the logic.
- The notebook is only for experiments, not needed to run the API.

## Acknowledgements
- Dataset: [Book Recommendation](https://www.kaggle.com/datasets/sinatavakoli/books-dataset-for-nlp-and-recommendation-systems)
- Libraries: FastAPI, scikit-learn, pandas, numpy
- Inspiration: Content-based recommendation systems lesson from AI Saturdays Lagos Cohort 9
