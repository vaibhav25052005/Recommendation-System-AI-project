import math

# Movie dataset
movies = [
    {"title": "Inception", "genres": ["Action", "Sci-Fi", "Thriller"]},
    {"title": "Interstellar", "genres": ["Sci-Fi", "Drama"]},
    {"title": "The Dark Knight", "genres": ["Action", "Crime", "Drama"]},
    {"title": "Avengers", "genres": ["Action", "Sci-Fi", "Fantasy"]},
    {"title": "Titanic", "genres": ["Romance", "Drama"]},
    {"title": "Iron Man", "genres": ["Action", "Sci-Fi"]}
]

# Create vocabulary
all_genres = list(set(g for movie in movies for g in movie["genres"]))

def vectorize(genres):
    return [1 if g in genres else 0 for g in all_genres]

def cosine_similarity(v1, v2):
    dot = sum(a * b for a, b in zip(v1, v2))
    mag1 = math.sqrt(sum(a * a for a in v1))
    mag2 = math.sqrt(sum(b * b for b in v2))
    if mag1 == 0 or mag2 == 0:
        return 0
    return dot / (mag1 * mag2)

vectors = [vectorize(movie["genres"]) for movie in movies]

def recommend_movies(movie_title, top_n=3):
    idx = next((i for i, m in enumerate(movies) if m["title"] == movie_title), None)
    if idx is None:
        return "Movie not found!"

    scores = []
    for i, vec in enumerate(vectors):
        if i != idx:
            sim = cosine_similarity(vectors[idx], vec)
            scores.append((movies[i]["title"], sim))

    scores.sort(key=lambda x: x[1], reverse=True)
    return [title for title, _ in scores[:top_n]]

# Test
movie_name = "Inception"
print(f"Recommended movies for '{movie_name}':")
for m in recommend_movies(movie_name):
    print("-", m)
