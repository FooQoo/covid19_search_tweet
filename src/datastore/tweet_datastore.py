from google.cloud import datastore
import hashlib


class TweetDataStore:
    def __init__(self):
        self.client = datastore.Client()

    """
    ツイートエンティティのモデル
    - 辞書型
    -- tweet_id
    -- shop (店舗名)
    -- created_at (unix time)
    """

    def insert_tweets(self, tweets):
        entities = []
        for tweet in tweets:
            entitie_id = hashlib.sha256(
                ('{0}{1}'.format(tweet['tweet_id'], tweet['shop']))
                .encode()).hexdigest()
            task = datastore.Entity(self.client.key('Tweet', entitie_id))
            task.update({
                'tweet_id': tweet['tweet_id'],
                'shop': tweet['shop'],
                'created_at': tweet['created_at']
            })
            entities.append(task)

        self.client.put_multi(entities)

    def get_latest_tweet(self):
        query = self.client.query(kind='Tweet')
        query.order = ['-created_at']
        tasks = list(query.fetch(limit=1))

        return tasks[:1]
