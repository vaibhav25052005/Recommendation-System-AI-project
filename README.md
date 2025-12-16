

## **1. Purpose of the Code**

This code implements a **content-based movie recommendation system**.
It recommends movies based on **genre similarity** using **cosine similarity**.

---

## **2. Import Library**

```python
import math
```

Used for mathematical operations like square root, required for cosine similarity.

---

## **3. Movie Dataset**

```python
movies = [
    {"title": "Inception", "genres": ["Action", "Sci-Fi", "Thriller"]},
    ...
]
```

Each movie has:

* `title`
* `genres`

This data is the basis for recommendations.

---

## **4. Create Genre Vocabulary**

```python
all_genres = list(set(g for movie in movies for g in movie["genres"]))
```

* Extracts **all unique genres**
* Creates a genre list like:
  `['Action', 'Sci-Fi', 'Drama', 'Romance', ...]`

This helps convert genres into vectors.

---

## **5. Vectorization Function**

```python
def vectorize(genres):
    return [1 if g in genres else 0 for g in all_genres]
```

* Converts movie genres into a **binary vector**
* Example:
  `[1, 0, 1, 0]` → genre present or not

This allows mathematical comparison.

---

## **6. Cosine Similarity Function**

```python
def cosine_similarity(v1, v2):
```

* Measures **similarity between two movies**
* Formula:
  [
  \text{similarity} = \frac{v1 \cdot v2}{|v1| \times |v2|}
  ]
* Output range: `0` (no similarity) to `1` (very similar)

---

## **7. Vector Creation**

```python
vectors = [vectorize(movie["genres"]) for movie in movies]
```

* Converts **all movies** into vectors
* Stored for quick comparison

---

## **8. Recommendation Function**

```python
def recommend_movies(movie_title, top_n=3):
```

### Steps:

1. Find selected movie index
2. Compare it with all other movies
3. Calculate cosine similarity
4. Sort movies by similarity score
5. Return top `N` recommendations

If movie is not found → returns error message.

---

## **9. Test Execution**

```python
movie_name = "Inception"
print(recommend_movies(movie_name))
```

* Recommends movies similar to **Inception**
* Based on shared genres like Action & Sci-Fi

---

## **10. Output**

Displays recommended movie titles ranked by similarity.

---

## **Summary**

✔ Content-based recommendation system
✔ Uses **cosine similarity**
✔ No external libraries like pandas required
✔ Beginner-friendly AI project



