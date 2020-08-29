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

    def get_youtube_secret_key(self):
        pass

    def get_youtube_client_id(self):
        pass

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
