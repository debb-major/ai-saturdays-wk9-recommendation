# recommender.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity

# Loading the dataset
df = pd.read_csv("book.csv")

# Preparing the data
df['combined_features'] = (
    df['title'].fillna('') + " " +
    df['authors'].fillna('') + " " +
    df['description'].fillna('')
)

# Building TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
feature_matrix = vectorizer.fit_transform(df['combined_features'])

# Computing similarity between all books
cosine_sim = cosine_similarity(feature_matrix, feature_matrix)

# Building a recommendation function based on book titles
def recommend_books(title, top_n=5, df=df, cosine_sim=cosine_sim):
    # Find index of the book
    if title not in df['title'].values:
        return f"'{title}' not found in dataset."
    
    idx = df.index[df['title'] == title][0]
    
    # Get similarity scores for this book
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Sort by similarity score (descending)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get top_n similar books (excluding the book itself)
    top_indices = [i[0] for i in sim_scores[1:top_n+1]]
    
    return df[['title', 'authors', 'average_rating']].iloc[top_indices]


# Building a recommendation function based on keyword
def recommend_by_keywords(keywords, top_n=5, df=df, feature_matrix=feature_matrix):
    """
    Recommend books based on keyword search.
    """
    # Transform the input keyword into the same TF-IDF space
    keyword_vec = vectorizer.transform([keywords])

    # Compute cosine similarity between the keyword vector and all books
    sim_scores = linear_kernel(keyword_vec, feature_matrix).flatten()

    # Get top_n book indices
    top_indices = sim_scores.argsort()[-top_n:][::-1]

    return df[['title', 'authors', 'average_rating']].iloc[top_indices]