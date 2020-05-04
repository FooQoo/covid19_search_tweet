from google.cloud import datastore
import hashlib


class RssDataStore:
    def __init__(self):
        self.client = datastore.Client()

    """
    RSSエンティティのモデル
    - 辞書型
    -- title
    -- link
    -- published_at (unix time)
    """

    def insert_rss_docs(self, rss_docs):
        entities = []
        for doc in rss_docs:
            entitie_id = hashlib.sha256((doc['link']).encode()).hexdigest()
            task = datastore.Entity(
                self.client.key('rss', entitie_id))
            task.update({
                'title': doc['title'],
                'link': doc['link'],
                'published_at': doc['published_at']
            })
            entities.append(task)

        self.client.put_multi(entities)
