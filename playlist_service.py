
import json
import requests
import youtube_dl

from secret_service import SecretService


class PlayListService:

    def __init__(self, spotify_token, spotify_username, youtube_client):
        self.spotify_token = spotify_token
        self.spotify_username = spotify_username
        self.youtube_client = youtube_client
        self.all_song_info = {}
        pass

    def get_liked_videos(self):
        request = self.youtube_client.videos().list(
            part="snippet,contentDetails,statistics",
            myRating="like"
        )
        response = request.execute()
        # print(response)
        youtube_dl.utils.std_headers['User-Agent'] = "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)"

        for item in response["items"]:
            video_title = item["snippet"]["title"]
            youtube_url = f'https://www.youtube.com/watch?v={item["id"]}'
            # take song name and artist
            video = youtube_dl.YoutubeDL({}).extract_info(
                youtube_url, download=False)
            print(video)
            if(video["track"] == 'None'):
                song_name = video['title']
            else:
                song_name = video['track']
            artist = video["artist"]

            self.all_song_info[video_title] = {
                "youtube_url": youtube_url,
                "song_name": song_name,
                "artist": artist,

                "spotify_uri": self.get_spotify_uri(song_name, artist)
            }
        # print(self.all_song_info)

    def create_playlist(self):
        request_body = json.dumps({
            "name": "Youtube Likes",
            "description": "This is a automated playlist from my youtube likes",
            "public": 1
        })
        url = f'https://api.spotify.com/v1/users/{self.spotify_username}/playlists'

        response = requests.post(url,
                                 data=request_body,
                                 headers={'Content-Type': 'application/json',
                                          'Authorization': f'Bearer {self.spotify_token}'})

        response_json = response.json()
        # print(response_json)

        return response_json['id']

    # search
    def get_spotify_uri(self, song_name, artist):
        url = f"https://api.spotify.com/v1/search?query=track%3A{song_name}+artist%3A{artist}&type=track&offset=0&limit=20"

        print(song_name)
        print(artist)
        response = requests.get(url, headers={'Content-Type': 'application/json',
                                              'Authorization': f'Bearer {self.spotify_token}'})
        response_json = response.json()
        # print(response_json)
        songs = response_json["tracks"]["items"]

        uri = songs[0]['uri']
        return uri

    def add_song_to_playlist(self):
        self.get_liked_videos()

        uris = []
        for song, info in self.all_song_info.items():
            uris.append(info["spotify_uri"])

        playlist_id = self.create_playlist()

        requests_data = json.dumps(uris)

        query = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

        response = requests.post(
            query,
            data=requests_data,
            headers={'Content-Type': 'application/json',
                     'Authorization': f'Bearer {self.spotify_token}'}
        )

        response_json = response.json()

        return response_json
