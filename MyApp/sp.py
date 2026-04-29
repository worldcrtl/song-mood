import streamlit as st
import random
import requests

# Spotify API credentials (replace with your own)
CLIENT_ID = "f1cbb1589acb44bab1cf71ed905c54c1"
CLIENT_SECRET = "3d937c58d30e4795bd13b0e54289b1d9"

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
        ("Good as Hell", "Lizzo"),
        ("APT", "Bruno Mars")
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
    
    # Try to get Spotify player if credentials provided
    if CLIENT_ID and CLIENT_SECRET:
        try:
            # Get access token
            auth_url = "https://accounts.spotify.com/api/token"
            auth_data = {"grant_type": "client_credentials"}
            auth_response = requests.post(auth_url, data=auth_data, auth=(CLIENT_ID, CLIENT_SECRET))
            token = auth_response.json().get("access_token")
            
            if token:
                # Search for the track
                search_url = "https://api.spotify.com/v1/search"
                headers = {"Authorization": f"Bearer {token}"}
                params = {"q": f"{song} {artist}", "type": "track", "limit": 1}
                response = requests.get(search_url, headers=headers, params=params)
                results = response.json()
                
                if results.get("tracks", {}).get("items"):
                    track = results["tracks"]["items"][0]
                    track_id = track["id"]
                    track_name = track["name"]
                    artist_name = track["artists"][0]["name"]
                    album_art = track["album"]["images"][0]["url"] if track["album"]["images"] else ""
                    spotify_url = track["external_urls"].get("spotify", "")
                    
                    # Display track info
                    col1, col2 = st.columns([1, 3])
                    with col1:
                        if album_art:
                            st.image(album_art, width=150)
                    with col2:
                        st.write(f"**{track_name}**")
                        st.write(f"*{artist_name}*")
                    
                    # Embed Spotify player
                    st.markdown(f"""
                    <iframe style="border-radius:12px" 
                    src="https://open.spotify.com/embed/track/{track_id}?utm_source=generator&theme=0" 
                    width="100%" height="152" frameBorder="0" allowfullscreen="" 
                    allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" 
                    loading="lazy"></iframe>
                    """, unsafe_allow_html=True)
                    
                    # Also show Spotify link
                    st.markdown(f"[🔗 Open in Spotify]({spotify_url})")
                else:
                    st.info("Song not found on Spotify. Try another mood!")
        except Exception as e:
            st.error(f"Could not connect to Spotify: {str(e)}")
            st.info("Make sure your Spotify credentials are correct.")
    else:
        st.warning("⚠️ Spotify credentials not configured.")
        st.info("""
        To enable the player:
        1. Go to [developer.spotify.com](https://developer.spotify.com/dashboard)
        2. Create an app and get Client ID & Secret
        3. Update the credentials in the code
        """)
    
    st.write("🎧 Sit back, press play, and enjoy the vibe ✨")