from tweet import TweetAPI
from tweet import ApiConfig
from rss import RssAPI
from datastore import TweetDataStore, RssDataStore
from dotenv import load_dotenv

config = 'src/resources/.env'


def get_tweet(event, context):
    load_dotenv(config, verbose=True)

    tweet_datastore = TweetDataStore()

    latest_tweet = tweet_datastore.get_latest_tweet()
    latest_id = None if len(latest_tweet) == 0 else latest_tweet[0]['tweet_id']

    api_config = ApiConfig()
    api_key = api_config.get_key_from_env()
    wrapper = TweetAPI(
        api_key['CONSUMER_KEY'],
        api_key['CONSUMER_SECRET'],
        api_key['ACCESS_TOKEN'],
        api_key['ACCESS_TOKEN_SECRET'])

    tweets = wrapper.fetch_by_query(
        q='#福井県マスク在庫', since_id=latest_id)

    entities = []
    for tweet in tweets:
        for tag in list(set(tweet['hashtags'])):
            if tag != '福井県マスク在庫':
                entities.append({
                    'tweet_id': tweet['id_str'],
                    'shop': tag,
                    'created_at': tweet['created_at']
                })

    tweet_datastore.insert_tweets(entities)


def get_rss(event, context):
    load_dotenv(config, verbose=True)

    rss_datastore = RssDataStore()

    wrapper = RssAPI()

    rss_docs = wrapper.fetch_rss()

    rss_datastore.insert_rss_docs(rss_docs)


if __name__ == "__main__":
    #get_tweet(None, None)
    get_rss(None, None)
