from flask import Flask, render_template, request
from convertMood import get_mood_tags
from spotifyUtils import search_tracks_by_mood
from albumArt import generate_album_art
from lyricsFetcher import fetch_lyrics

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        mood_input = request.form.get("mood")
        mood_tags = get_mood_tags(mood_input)
        tracks = search_tracks_by_mood(mood_tags)
        art_url = generate_album_art(mood_tags)
      
        current_index = int(request.form.get("track_index", 0))
        current_track = tracks[current_index]
        lyrics = fetch_lyrics(current_track["artist"], current_track["name"])

        return render_template(
            "index.html",
            mood=mood_input,
            mood_tags=mood_tags,
            tracks=tracks,
            current_track_index=current_index,
            lyrics=lyrics,
            art_url=art_url
        )

    return render_template("index.html", tracks=None)
