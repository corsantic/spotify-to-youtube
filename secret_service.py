import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors


class SecretService:

    def __init__(self):
        pass

    def get_spotify_secret_key(self):
        secret = self.get_stripped_str(0, 1, ':')
        # print(secret)
        return secret

    def get_spotify_client_id(self):
        client_id = self.get_stripped_str(1, 1, ':')
        # print(client_id)
        return client_id

    def get_youtube_client(self):
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
        scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = "client_secret_CLIENTID.json"  # YOUR_CLIENT_SECRET_FILE

        # Get credentials and create an API client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)
        credentials = flow.run_console()
        print(credentials)
        youtube_client = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)

        print(youtube_client)

        return youtube_client

    def get_spotify_token_from_file(self):
        token = self.get_stripped_str(2, 1, ':')
        # print(token)
        return token

    def get_spotify_username(self):
        username = self.get_stripped_str(3, 1, ':')
        print(username)
        return username

    def read_file(self):
        f = open("secret.txt", "r")
        return f

    def get_stripped_str(self, lineIndex, splitIndex, splitStr):
        f = self.read_file()
        lines = f.readlines()
        f.close()
        q = lines[lineIndex]
        result = q.split(splitStr)[splitIndex].strip()
        return result
