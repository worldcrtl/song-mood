import streamlit as st
import random

st.title("🎧 Mood-Based Song Recommender")

st.write("Pick your current mood and get a song recommendation.")

# Mood options
mood = st.selectbox(
    "How are you feeling?",
    ["Happy", "Sad", "Motivated", "Chill", "Stressed"]
)

# Song database with Spotify links (track IDs)
songs = {
    "Happy": [
        ("Happy", "Pharrell Williams", "2noRn2A2tNp3Q2F2hX1M9y"),
        ("Can't Stop the Feeling!", "Justin Timberlake", "5aT0lGrmKhql6l8Uk1v2kW"),
        ("Good as Hell", "Lizzo", "52g8uRTrsC3UV3RwM61O7i")
    ],
    "Sad": [
        ("Someone Like You", "Adele", "4fdnp8T6CL6xOrbLRTVGoT"),
        ("Stay", "Rihanna", "0GjEhVFGHJ8umNskHrRBz5"),
        ("Fix You", "Coldplay", "7uStwfxF0M9jFCwXo2k0qB")
    ],
    "Motivated": [
        ("Lose Yourself", "Eminem", "7FIkT1fXhE7I1dKj4dY1xW"),
        ("Stronger", "Kanye West", "4lCyQrjQBxE3C5j9dD4xZf"),
        ("Eye of the Tiger", "Survivor", "0lPOPg9Hnd8d7wX3jY7W8k")
    ],
    "Chill": [
        ("Sunflower", "Post Malone", "0Ri7pu5r6QE3kS0uHw3J9y"),
        ("Location", "Khalid", "3S0ocg4y5q2dCuC9f3k5xZ"),
        ("Peaches & Cream", "Sade", "6j8ccdxD3q2x1Y2dK4f6Z8")
    ],
    "Stressed": [
        ("Weightless", "Marconi Union", "5eAWCfyUhZtHHtBdNk56l1"),
        ("Breathe Me", "Sia", "4tZwfgrHOc3mvqYlEYSvVi"),
        ("Holocene", "Bon Iver", "1Xyo4u8p8x5H7dK4f3Y9Z2")
    ]
}

if st.button("Recommend a Song"):
    song, artist, spotify_id = random.choice(songs[mood])
    st.success(f"🎵 Your song: **{song}** by {artist}")
    
    # Embed Spotify player
    st.markdown(f"""
    <iframe style="border-radius:12px" 
    src="https://open.spotify.com/embed/track/{spotify_id}?utm_source=generator&theme=0" 
    width="100%" height="152" frameBorder="0" allowfullscreen="" 
    allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" 
    loading="lazy"></iframe>
    """, unsafe_allow_html=True)
    
    st.write("🎧 Sit back, press play, and enjoy the vibe ✨")