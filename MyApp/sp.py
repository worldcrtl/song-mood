import streamlit as st
import random
import requests

# Spotify API credentials (replace with your own)
CLIENT_ID = "YOUR_SPOTIFY_CLIENT_ID"
CLIENT_SECRET = "YOUR_SPOTIFY_CLIENT_SECRET"

def get_spotify_token():
    """Get Spotify access token"""
    auth_url = "https://accounts.spotify.com/api/token"
    auth_data = {"grant_type": "client_credentials"}
    auth_response = requests.post(auth_url, data=auth_data, auth=(CLIENT_ID, CLIENT_SECRET))
    return auth_response.json().get("access_token")

def search_spotify(query, token):
    """Search for a song on Spotify"""
    search_url = "https://api.spotify.com/v1/search"
    headers = {"Authorization": f"Bearer {token}"}
    params = {"q": query, "type": "track", "limit": 1}
    response = requests.get(search_url, headers=headers, params=params)
    return response.json()

st.title("🎧 Mood-Based Song Recommender")

st.write("Pick your current mood and get a song recommendation.")

# Add credentials input in sidebar
with st.sidebar:
    st.header("🔐 Spotify API")
    st.info("""
    To enable playback:
    1. Go to [developer.spotify.com](https://developer.spotify.com/dashboard)
    2. Create an app and get credentials
    3. Enter them below
    """)
    client_id_input = st.text_input("Client ID", type="password", placeholder="Enter your Client ID")
    client_secret_input = st.text_input("Client Secret", type="password", placeholder="Enter your Client Secret")

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
    
    # Try to get Spotify preview if credentials provided
    if client_id_input and client_secret_input:
        try:
            # Use user credentials
            auth_url = "https://accounts.spotify.com/api/token"
            auth_data = {"grant_type": "client_credentials"}
            auth_response = requests.post(auth_url, data=auth_data, auth=(client_id_input, client_secret_input))
            token = auth_response.json().get("access_token")
            
            if token:
                search_url = "https://api.spotify.com/v1/search"
                headers = {"Authorization": f"Bearer {token}"}
                params = {"q": f"{song} {artist}", "type": "track", "limit": 1}
                response = requests.get(search_url, headers=headers, params=params)
                results = response.json()
                
                if results.get("tracks", {}).get("items"):
                    track = results["tracks"]["items"][0]
                    preview_url = track.get("preview_url")
                    
                    if preview_url:
                        st.audio(preview_url, format="audio/mp3")
                    else:
                        st.markdown(f"[🎵 Open in Spotify]({track['external_urls']['spotify']})")
                else:
                    st.info("Song not found on Spotify")
        except Exception as e:
            st.warning("Could not connect to Spotify. Check your credentials!")
    
    st.write("🎧 Sit back, press play, and enjoy the vibe ✨")