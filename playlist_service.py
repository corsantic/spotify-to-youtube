
import json
import requests

from secret_service import SecretService


class PlayListService:

    def __init__(self, spotify_secret, spotify_client_id, spotify_token, spotify_username):
        self.spotify_secret = spotify_secret
        self.spotify_client_id = spotify_client_id
        self.spotify_token = spotify_token
        self.spotify_username = spotify_username
        pass

    def get_youtube_client(self):
        pass

    def get_liked_videos(self):
        pass

    def create_playlist(self):
        request_body = json.dumps({
            "name": "Youtube Likes",
            "description": "This is a automated playlist from my youtube likes",
            "public": 1
        })
        url = f'https://api.spotify.com/v1/users/{self.spotify_username}/playlists'

        print(self.spotify_secret)
        response = requests.post(url,
                                 data=request_body,
                                 headers={'Content-Type': 'application/json',
                                          'Authorization': f'Bearer {self.spotify_token}'})

        response_json = response.json()
        print(response_json)

        return response_json['id']

    # search
    def get_spotify_uri(self, song_name, artist):
        url = f"https://api.spotify.com/v1/search?query=track%3A{song_name}+artist%3A{artist}&type=track&offset=0&limit=20"

        response = requests.get(url, headers={'Content-Type': 'application/json',
                                              'Authorization': f'Bearer {self.spotify_token}'})
        response_json = response.json()
        print(response_json)
        songs = response_json["tracks"]["items"]
        return songs

    def add_song_to_playlist(self):
        pass
