from secret_service import SecretService
from playlist_service import PlayListService
from user_service import UserService

print('hello')

secret_service = SecretService()
user_service = UserService()
token = user_service.authenticate()
spotify_secret_key = secret_service.get_spotify_secret_key()
spotify_client_id = secret_service.get_spotify_client_id()
spotify_username = secret_service.get_spotify_username()
playlist_service = PlayListService(token, spotify_username )

# res = create_playlist.create_playlist()

res = playlist_service.get_spotify_uri('Anne','John Frusciante');



print(res)
