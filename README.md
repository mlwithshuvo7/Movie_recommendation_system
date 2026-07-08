# 🎬 Movie Recommendation System

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Poppins&size=28&duration=3000&pause=1000&color=00C2FF&center=true&vCenter=true&width=800&lines=Movie+Recommendation+System;Machine+Learning+Project;Content-Based+Recommendation+Engine;Python+%7C+Scikit-Learn+%7C+Streamlit" />
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-orange?style=for-the-badge&logo=scikitlearn)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit)
![Render](https://img.shields.io/badge/Render-Deployed-success?style=for-the-badge&logo=render)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

---

## 📌 Overview

Choosing the perfect movie from thousands of available titles can be challenging.

This project is a **Content-Based Movie Recommendation System** built using **Machine Learning**. Instead of recommending movies based on ratings or user behavior, it analyzes movie content such as genres, keywords, cast, crew, and overview to suggest similar movies.

The recommendation engine converts movie information into numerical vectors and uses **Cosine Similarity** to recommend the **Top 5 most similar movies**.

---

## 🚀 Features

- 🎬 Content-Based Recommendation System
- 🤖 Machine Learning Powered
- 🔍 Recommend Top 5 Similar Movies
- ⚡ Fast Recommendation Engine
- 🌐 Interactive Web Application
- 📦 Easy Deployment
- 💻 Clean User Interface

---

# 📊 Dataset

**Dataset Used**

TMDB 5000 Movie Dataset

Movie metadata includes:

- Movie Title
- Genres
- Keywords
- Cast
- Crew
- Overview

---

# ⚙️ Project Workflow

```text
TMDB 5000 Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Create Tags Column
        │
        ▼
Text Preprocessing
        │
        ▼
CountVectorizer
(Max Features = 5000)
        │
        ▼
Movie Vector Matrix
        │
        ▼
Cosine Similarity
        │
        ▼
Recommend Top 5 Movies
```

---

# 🧠 How It Works

### Step 1

Load the TMDB 5000 dataset.

### Step 2

Clean the dataset by removing missing values and unnecessary columns.

### Step 3

Combine important movie features into a single **tags** column.

Features combined:

- Genres
- Keywords
- Cast
- Crew
- Overview

### Step 4

Apply text preprocessing.

- Lowercase
- Remove spaces
- Stemming

### Step 5

Convert text into numerical vectors using:

```python
CountVectorizer(max_features=5000, stop_words='english')
```

### Step 6

Generate a vector representation for every movie.

### Step 7

Calculate similarity using:

```python
cosine_similarity()
```

### Step 8

Recommend the **Top 5 Most Similar Movies**.

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Pandas | Data Processing |
| NumPy | Numerical Computing |
| Scikit-Learn | Machine Learning |
| NLTK | Text Preprocessing |
| Pickle | Model Serialization |
| Streamlit | Frontend |
| Render | Deployment |

---

# 📂 Project Structure

```text
movie_recommendation_system/

├── app.py
├── model.pkl
├── similarity.pkl
├── movie_list.pkl
├── requirements.txt
├── README.md
├── dataset/
├── notebooks/
├── assets/
└── screenshots/
```

---

# 📈 Recommendation Pipeline

```text
Movie Title
      │
      ▼
Find Movie Index
      │
      ▼
Retrieve Movie Vector
      │
      ▼
Calculate Cosine Similarity
      │
      ▼
Sort Similarity Scores
      │
      ▼
Return Top 5 Movies
```

---

# 💻 Installation

```bash
git clone https://github.com/yourusername/movie_recommendation_system.git

cd movie_recommendation_system

pip install -r requirements.txt

streamlit run app.py
```

---

# 📸 Screenshots

## Home Page

<img width="979" height="482" alt="fffe" src="https://github.com/user-attachments/assets/995b2f05-81d7-4115-b18e-5b137f89c039" />


---

## Recommendation Result

<img width="835" height="702" alt="streamli2" src="https://github.com/user-attachments/assets/ff951cef-7965-49c0-bfea-ebe6d3426780" />


---

# 🌍 Live Demo

### 🚀 Streamlit

 http://localhost:8501

### 🌐 Render

https://movie-recommendation-system-3-3vss.onrender.com

---

# 📚 Machine Learning Concepts Used

- Data Cleaning
- Feature Engineering
- Natural Language Processing (NLP)
- Count Vectorization
- Cosine Similarity
- Recommendation Systems

---

# 🚀 Future Improvements

- 🎥 Movie Posters using TMDB API
- 👤 User Authentication
- ❤️ Personalized Recommendations
- ⭐ Movie Ratings
- 🎭 Genre Filtering
- 🔍 Smart Search Suggestions
- 🤖 Hybrid Recommendation System
- 📱 Responsive UI

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository

2. Create a new feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

## Shuvo Kundu

**Machine Learning & AI Enthusiast**

Passionate about building real-world AI applications using Machine Learning, NLP, and Data Science.

---

<p align="center">

### ⭐ If you like this project, don't forget to Star this repository!

**Made with ❤️ using Python & Machine Learning**

</p>
