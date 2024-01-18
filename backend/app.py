from flask import Flask, render_template
from spotipy.oauth2 import SpotifyOAuth
import spotipy

app = Flask(__name__, template_folder='templates')

# Replace these with your actual Spotify API credentials
scope = 'user-top-read'
cid = "c17c2586583748488396a26cf58c46c9"
cs = "7f83d99bd1684fcb9f939418220ff3d4"
ruri = "http://localhost:3000"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid, client_secret=cs, redirect_uri=ruri, scope=scope))

@app.route('/')
def index():
    # Fetch top artists
    results = sp.current_user_top_artists(time_range='short_term', limit=5)
    artists = [item['name'] for item in results['items']]

    # Fetch genres from top artists
    genres = [item['genres'][-1] for item in results['items']]

    # Fetch recommendations based on top artist genres
    recs = sp.recommendations(seed_genres=genres, limit=20)
    recommendations = [{'name': item['name'], 'artists': [ktem['name'] for ktem in item['artists']]} for item in recs['tracks']]

    # Pass data to the HTML template
    print("Top Artists:", artists)
    print("Recommendations:", recommendations)

    return render_template('index.html', artists=artists, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)