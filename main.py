from secret_service import SecretService
from playlist_service import PlayListService


print('hello')

secret_service = SecretService()
create_playlist = PlayListService(
    secret_service.get_spotify_secret_key(), secret_service.get_spotify_client_id(), secret_service.get_spotify_token_from_file(), secret_service.get_spotify_username())


res = create_playlist.create_playlist()

print(res)
