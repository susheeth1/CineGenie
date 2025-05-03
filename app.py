from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"

GENRE_ID_NAME_MAP = {
    28: "Action", 12: "Adventure", 16: "Animation", 35: "Comedy", 80: "Crime",
    99: "Documentary", 18: "Drama", 10751: "Family", 14: "Fantasy", 36: "History",
    27: "Horror", 10402: "Music", 9648: "Mystery", 10749: "Romance", 878: "Sci-Fi",
    10770: "TV Movie", 53: "Thriller", 10752: "War", 37: "Western"
}

def get_movies_by_title(query):
    url = f"{BASE_URL}/search/movie"
    params = {"api_key": TMDB_API_KEY, "query": query, "language": "en-US"}
    return requests.get(url, params=params).json().get("results", [])

def get_movies_by_actor(query):
    person_url = f"{BASE_URL}/search/person"
    params = {"api_key": TMDB_API_KEY, "query": query, "language": "en-US"}
    person_data = requests.get(person_url, params=params).json()
    if person_data.get("results"):
        person_id = person_data["results"][0]["id"]
        credits_url = f"{BASE_URL}/person/{person_id}/movie_credits"
        credits_params = {"api_key": TMDB_API_KEY, "language": "en-US"}
        return requests.get(credits_url, params=credits_params).json().get("cast", [])
    return []

def get_movies_by_language(query):
    language_query = query.lower()
    url = f"{BASE_URL}/discover/movie"
    params = {
        "api_key": TMDB_API_KEY,
        "with_original_language": language_query,
        "sort_by": "popularity.desc"
    }
    return requests.get(url, params=params).json().get("results", [])

def format_movie_data(movie):
    genre_ids = movie.get("genre_ids", [])
    genres = [GENRE_ID_NAME_MAP.get(gid, "Unknown") for gid in genre_ids]
    return {
        "title": movie.get("title", "N/A"),
        "release_date": movie.get("release_date", "N/A"),
        "overview": movie.get("overview", "No description available."),
        "poster_path": f"https://image.tmdb.org/t/p/w500{movie['poster_path']}" if movie.get("poster_path") else None,
        "rating": movie.get("vote_average", "N/A"),
        "language": movie.get("original_language", "N/A"),
        "genres": ", ".join(genres)
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend_movies():
    data = request.get_json()
    query = data.get("query", "").strip()

    if not query:
        return jsonify({"error": "No query provided"}), 400

    seen_ids = set()
    all_results = []

    # Title-based results
    for movie in get_movies_by_title(query):
        if movie["id"] not in seen_ids:
            all_results.append(format_movie_data(movie))
            seen_ids.add(movie["id"])

    # Actor-based results
    for movie in get_movies_by_actor(query):
        if movie["id"] not in seen_ids:
            all_results.append(format_movie_data(movie))
            seen_ids.add(movie["id"])

    # Language-based results (2-letter ISO code only)
    if len(query) == 2:
        for movie in get_movies_by_language(query):
            if movie["id"] not in seen_ids:
                all_results.append(format_movie_data(movie))
                seen_ids.add(movie["id"])

    if not all_results:
        return jsonify({"error": "No movies found for your query"}), 404

    # Optional: sort by rating
    all_results.sort(key=lambda x: float(x["rating"]) if x["rating"] != "N/A" else 0, reverse=True)

    return jsonify({"movies": all_results[:20]}), 200  # Limit to 20 results

if __name__ == "__main__":
    app.run(debug=True)
