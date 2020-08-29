from secret_service import SecretService
from playlist_service import PlayListService
from user_service import UserService

print('hello')

secret_service = SecretService()
user_service = UserService()

# spotify_token = user_service.authenticate_spotify()
spotify_token = secret_service.get_spotify_token_from_file()
spotify_username = secret_service.get_spotify_username()
print(spotify_token)
youtube_client = secret_service.get_youtube_client()
playlist_service = PlayListService(spotify_token, spotify_username, youtube_client)

# res = playlist_service.create_playlist()

# res = playlist_service.get_spotify_uri('Anne','John Frusciante');


res = playlist_service.add_song_to_playlist()


print(res)
