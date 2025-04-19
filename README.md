# moodToMusic

This project takes a user's mood description and generates a custom music playlist using Spotify, along with AI-generated album art and original song lyrics.

## Features

    1. Mood input: User enters a description of their mood or vibe.

    2. Mood classification: Uses OpenAI GPT to extract relevant music mood tags.

    3. Playlist generation: Fetches 10 matching tracks from the Spotify API.

    4. Album art: Generates a unique cover using OpenAI's DALL·E.

    5. Lyrics fethcher: Creates original chorus-style lyrics that match the mood.


## Getting Started

1. Clone the repo
'''
git clone https://github.com/yourusername/music-mood-playlist.git
cd music-mood-playlist
'''
2. Set Up Environment Variables

Create a .env file in the root directory with the following:
'''
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
OPENAI_API_KEY=your_openai_api_key
'''
3. Install Dependencies
'''
pip install -r requirements.txt
'''
4. Run the App
'''
python app.py
'''
Then open http://localhost:5000 in your web browser.


## Tech Stack

    1. Flask (Web Framework)

    2. OpenAI GPT-3.5 (Mood classification and lyrics generation)

    3. Spotify Web API (Playlist generation)

    4. DALL·E (Album art generation)

    5. HTML/CSS (Frontend)

## Potential Extensions

    1. Add voice input using OpenAI Whisper

    2. Use MusicGen to create AI-generated music previews

    3. Deploy the app using Streamlit, Hugging Face Spaces, or Render

    4. Support playlist saving to user's Spotify account via OAuth
