
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
![Screenshot 2025-05-02 223909](https://github.com/user-attachments/assets/7ab64fff-bd9e-4975-9caf-8248d1686ffb)

![Screenshot 2025-05-02 223948](https://github.com/user-attachments/assets/02d7463a-f6d1-4822-a3ee-f41a203a233d)

![Screenshot 2025-05-02 224017](https://github.com/user-attachments/assets/aac36b9d-24b6-4b53-9449-79a49e72f064)





---

## 📧 Credits

- Movie data from [The Movie Database (TMDb)](https://www.themoviedb.org/)
- Developed by Susheeth 💻 with ❤️

---

## 📜 License

MIT License
