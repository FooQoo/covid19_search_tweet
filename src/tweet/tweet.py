import tweepy
import traceback


class TweetAPI:
    def __init__(self, consumer_key, consumer_secret, access_token,
                 access_token_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth, wait_on_rate_limit=True)

    def fetch_by_query(self, q, lang='ja', count=10, since_id=None):
        tweets = []

        try:
            for status in tweepy.Cursor(self.api.search, q=q, lang=lang,
                                        since_id=since_id,
                                        result_type='recent').items(count):
                tweet = self.__convert_to_dict(status)
                tweets.append(tweet)
        except tweepy.error.RateLimitError:
            print('Exceed rate limit.')
        except tweepy.error.TweepError:
            print(traceback.format_exc())

        return tweets

    def __convert_to_dict(self, tweet):
        return {
            'id_str': tweet.id,
            'hashtags': [tag['text'] for tag in tweet.entities['hashtags']],
            'created_at': tweet.created_at.timestamp()
        }
