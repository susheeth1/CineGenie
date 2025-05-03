
# 🎬 CineGenie 🍿

CineGenie is a fun and beautiful web application that helps users discover movies based on any search term — such as a movie name, actor, genre, or theme. It uses the TMDb API to fetch movie data and provides recommendations with a rich and engaging UI.

## 🌐 Live Demo - [CineGenie](https://cinegenie.onrender.com/)

---

## 🚀 Features

- 🔍 Search movies by title, actor, or genre
- 📸 Beautiful display with posters, ratings, genres, and release dates
- 🎨 Modern UI with responsive design
- 🎯 Works with The Movie Database (TMDb) API

---

## 📁 Project Structure

```
CineGenie/
│
├── app.py                # Flask application
├── templates/
│   └── index.html        # Frontend HTML (with inline JS & CSS)
├── .env                  # Environment file for API key
├── requirements.txt      # Python dependencies
└── README.md             # You're reading this!
```

---

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/cinegenie.git
   cd cinegenie
   ```

2. **Create and activate a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file and add your TMDb API Key**
   ```
   TMDB_API_KEY=your_tmdb_api_key_here
   ```

5. **Run the Flask app**
   ```bash
   python app.py
   ```

6. Open your browser and visit: [http://localhost:5000](http://localhost:5000)



## 📦 Requirements

Include this in `requirements.txt`:

```
Flask
requests
python-dotenv
gunicorn
```

---

## 📸 Preview
![image](https://github.com/user-attachments/assets/b45aac7a-7b83-447b-be14-abf726513384)
![image](https://github.com/user-attachments/assets/08afcee3-c4f3-4bfd-90d3-326e8017ad79)
![image](https://github.com/user-attachments/assets/3d57b676-ff77-4b90-b963-b6c705f4f120)




---

## 📧 Credits

- Movie data from [The Movie Database (TMDb)](https://www.themoviedb.org/)
- Developed by Susheeth 💻 with ❤️

---

## 📜 License

MIT License
