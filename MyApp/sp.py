import streamlit as st
import random

st.title("🎧 Mood-Based Song Recommender")

st.write("Pick your current mood and get a song recommendation.")

# Mood options
mood = st.selectbox(
    "How are you feeling?",
    ["Happy", "Sad", "Motivated", "Chill", "Stressed"]
)

# Song database with YouTube links
songs = {
    "Happy": [
        ("Happy", "Pharrell Williams", "https://www.youtube.com/watch?v=y6Sxv-sUYtM"),
        ("Can't Stop the Feeling!", "Justin Timberlake", "https://www.youtube.com/watch?v=ru0K8uoeZWc"),
        ("Good as Hell", "Lizzo", "https://www.youtube.com/watch?v=1e3a1J1Q0o8")
    ],
    "Sad": [
        ("Someone Like You", "Adele", "https://www.youtube.com/watch?v=n-e6Q2eGi0s"),
        ("Stay", "Rihanna", "https://www.youtube.com/watch?v=SDcbB9o3qT8"),
        ("Fix You", "Coldplay", "https://www.youtube.com/watch?v=cQfI6K8C7gY")
    ],
    "Motivated": [
        ("Lose Yourself", "Eminem", "https://www.youtube.com/watch?v=7AcDmT3H6Vc"),
        ("Stronger", "Kanye West", "https://www.youtube.com/watch?v=4mOK7ZOX5gQ"),
        ("Eye of the Tiger", "Survivor", "https://www.youtube.com/watch?v=btPJPFnesV4")
    ],
    "Chill": [
        ("Sunflower", "Post Malone", "https://www.youtube.com/watch?v=ApXoWvfEYVU"),
        ("Location", "Khalid", "https://www.youtube.com/watch?v=2fuvJgYwW3Q"),
        ("Peaches & Cream", "Lo-Fi Beats", "https://www.youtube.com/watch?v=5qap5aO4i9A")
    ],
    "Stressed": [
        ("Weightless", "Marconi Union", "https://www.youtube.com/watch?v=a9UkFdH3qW8"),
        ("Breathe Me", "Sia", "https://www.youtube.com/watch?v=1w7GlY3In7U"),
        ("Holocene", "Bon Iver", "https://www.youtube.com/watch?v=SS-wjn9cD90")
    ]
}

if st.button("Recommend a Song"):
    song, artist, youtube_url = random.choice(songs[mood])
    st.success(f"🎵 Your song: **{song}** by {artist}")
    
    # Extract video ID for embedding
    video_id = youtube_url.split("v=")[-1] if "v=" in youtube_url else youtube_url.split("/")[-1]
    
    # Embed YouTube player
    st.markdown(f"""
    <iframe width="100%" height="315" 
    src="https://www.youtube.com/embed/{video_id}?autoplay=1" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
    """, unsafe_allow_html=True)
    
    st.write("🎧 Sit back, press play, and enjoy the vibe ✨")