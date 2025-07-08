
# 1. 🎧 SpotSuggest – Find Similar Songs Instantly 
![image](https://github.com/user-attachments/assets/3a59bd30-bcc5-428a-98b7-afc7c8a757ab)

![image](https://github.com/user-attachments/assets/4af2e019-d096-4ab4-ad19-aa839e5a19cb)

![image](https://github.com/user-attachments/assets/ea6b9888-0d88-4e00-a71e-e21bf33a0263)

--- 
- **SpotSuggest** is a simple and smart music recommendation tool that helps you find songs similar to the ones you already love.

- Just pick any song from a provided list, and SpotSuggest will instantly recommend other songs that match its vibe — based on musical features like tempo, energy, mood, and more.

---

## 🚀 What It Does

- 🎵 **Select a Song, Get Recommendations**  
  Choose any track from the list and discover songs that are musically similar.

- 🤖 **Smart Recommendations using ML**  
  Uses basic machine learning methods like:
  - **KMeans Clustering** – groups songs with similar audio features
  - **Cosine Similarity** – finds songs closest in sound and feel to your selected track

- 📋 **View & Copy Song History**  
  Get a personalized list of your previously selected songs and copy them all with a single click.

---

## 💡 Why Use SpotSuggest?

Whether you're building a playlist, exploring new music, or just looking for something with a similar vibe to your favorite track — SpotSuggest helps you discover it effortlessly.

---

# 2. Live Demo 

https://drive.google.com/file/d/1sHClHFm05A7Sdk-kTciocbCb-JtcGc_z/view?usp=sharing

---

# 3. Tech Stack 
```bash
- Python
- Flask
- sk-learn
- Spotify Songs Dataset (kaggle)
- bootstrap 
```

---

# 4. Installation & Setup 

- Clone the repo
```bash
git clone <copy the https url of the repo>
```

- Open the project folder in your favourite IDE

- Install the requirements with the below command
```bash
pip install -r requirements.txt
```

- Run the app.py file using below command from your terminal
```bash
python app.py (for windows)
python3 app.py (for linux or mac)
```

--- 

# 5. Folder Structure 
```bash
SPOTIFY MUSIC RECOMMENDATION/
├── .ipynb_checkpoints/ # Jupyter notebook checkpoints
├── .venv/ # Python virtual environment
├── templates/ # HTML templates for the web app (if using Flask)
├── .gitignore # Specifies files/folders to be ignored by Git
├── app.py # Main backend app script
├── clustered_df.csv # Dataset with clustered songs for ML model
├── data_by_artist.csv # Songs grouped by artist
├── data_by_genres.csv # Songs grouped by genre
├── data_by_year.csv # Songs grouped by release year
├── data_w_genres.csv # Dataset including genres and features
├── data.csv # Original song dataset
├── README.md # Project documentation
└── spotify music recom.ipynb # Jupyter notebook for data analysis & ML
```

---

# 6. Future Improvements 
## I am planning to add below improvements in near future and you can also try these features and send pull requests 

- Add Spotify API support to fetch live songs
- Playlist creation and export options
- User authentication and profile-based recommendations

# 7. Acknowledgements 
- Flask docs
- sk-learn docs
- jupyter notebook
- AI with noor youtube channel
- kaggle datasets
