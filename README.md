# moodToMusic

This project takes a user's mood description and generates a custom music playlist using Spotify, along with AI-generated album art and original song lyrics.

## Features

    Mood Input: User enters a description of their mood or vibe.

    Mood Classification: Uses OpenAI GPT to extract relevant music mood tags.

    Playlist Generation: Fetches 10 matching tracks from the Spotify API.

    Album Art: Generates a unique cover using OpenAI's DALL·E.

    Lyrics Generator: Creates original chorus-style lyrics that match the mood.


## Getting Started
1. Clone the Repository

git clone https://github.com/yourusername/music-mood-playlist.git
cd music-mood-playlist

2. Set Up Environment Variables

Create a .env file in the root directory with the following:

SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
OPENAI_API_KEY=your_openai_api_key

3. Install Dependencies

pip install -r requirements.txt

4. Run the App

python app.py

Then open http://localhost:5000 in your web browser.


## Tech Stack

    Flask (Web Framework)

    OpenAI GPT-3.5 (Mood classification and lyrics generation)

    Spotify Web API (Playlist generation)

    DALL·E (Album art generation)

    HTML/CSS (Frontend)

## Potential Extensions

    Add voice input using OpenAI Whisper

    Use MusicGen to create AI-generated music previews

    Deploy the app using Streamlit, Hugging Face Spaces, or Render

    Support playlist saving to user's Spotify account via OAuth
