from secret_service import SecretService
import requests
import json

import base64

class UserService:

    def __init__(self):
        pass


    def authenticate(self):
        secret = SecretService()
        headers = {}
        data = {}

        client_id =secret.get_spotify_client_id();
        client_secret =secret.get_spotify_secret_key();
        url = "https://accounts.spotify.com/api/token"        
        message = f'{client_id}:{client_secret}'
        messageBytes = message.encode('ascii')
        base64Bytes = base64.b64encode(messageBytes)
        base64Message = base64Bytes.decode('ascii')
        
        headers['Authorization'] = f"Basic {base64Message}"
        data['grant_type'] = "client_credentials"

        r = requests.post(url, headers=headers, data=data)

        print(r.json())
        token = r.json()['access_token']

        # url =f'https://accounts.spotify.com/authorize?client_id={secret.get_spotify_client_id()}&response_type=code&redirect_uri=https%3A%2F%2Fexample.com%2Fcallback'

        return token
