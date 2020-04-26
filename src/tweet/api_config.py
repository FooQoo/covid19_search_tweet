from os import environ


class ApiConfig:
    def get_key_from_env(self):
        return {
            'CONSUMER_KEY': environ.get('CONSUMER_KEY'),
            'CONSUMER_SECRET': environ.get('CONSUMER_SECRET'),
            'ACCESS_TOKEN': environ.get('ACCESS_TOKEN'),
            'ACCESS_TOKEN_SECRET': environ.get('ACCESS_TOKEN_SECRET')
        }
