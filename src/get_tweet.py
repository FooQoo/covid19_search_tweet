import fire
import pandas as pd
from tweet import TweepyWrapper
from tweet import ApiConfig


def get_tweet(config='./resources/twitter.json',
              output='../csv/ff.csv'):
    api_config = ApiConfig(config)
    api_key = api_config.get_key()
    wrapper = TweepyWrapper(
        api_key['CONSUMER_KEY'],
        api_key['CONSUMER_SECRET'],
        api_key['ACCESS_TOKEN'],
        api_key['ACCESS_TOKEN_SECRET'])

    tweets = wrapper.fetch_by_query('パズドラ', count=10)
    df = pd.DataFrame(tweets)
    df.to_csv(output, index=None)


if __name__ == '__main__':
    fire.Fire(get_tweet)
