import streamlit as st
import random

st.title("🎧 Mood-Based Song Recommender")

st.write("Pick your current mood and get a song recommendation.")

# Mood options
mood = st.selectbox(
    "How are you feeling?",
    ["Happy", "Sad", "Motivated", "Chill", "Stressed"]
)

# Song database
songs = {
    "Happy": [
        ("Happy", "Pharrell Williams"),
        ("Can't Stop the Feeling", "Justin Timberlake"),
        ("Good as Hell", "Lizzo")
    ],
    "Sad": [
        ("Someone Like You", "Adele"),
        ("Stay", "Rihanna"),
        ("Fix You", "Coldplay")
    ],
    "Motivated": [
        ("Lose Yourself", "Eminem"),
        ("Stronger", "Kanye West"),
        ("Eye of the Tiger", "Survivor")
    ],
    "Chill": [
        ("Sunflower", "Post Malone"),
        ("Location", "Khalid"),
        ("Peaches & Cream", "Sade")
    ],
    "Stressed": [
        ("Weightless", "Marconi Union"),
        ("Breathe Me", "Sia"),
        ("Holocene", "Bon Iver")
    ]
}

if st.button("Recommend a Song"):
    song, artist = random.choice(songs[mood])
    st.success(f"🎵 Your song: **{song}** by {artist}")
    st.write("🎧 Sit back, press play, and enjoy the vibe ✨")