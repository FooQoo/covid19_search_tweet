# Covid19TweetFeeder

## poetry env

```
# プロジェクトルートごとに.venvファイルをする設定
$ poetry config virtualenvs.in-project true

# 仮想環境を作成
$ poetry install
$ poetry shell
```

## vscode の設定

1. `cmd + shift + p`
2. Python: Select interpriter を選択
3. .venv の仮想環境を指定

## deploy

```get_tweet
gcloud beta functions deploy get_tweet --entry-point=get_tweet --trigger-topic=datastore --env-vars-file=env.yaml --source=src --runtime=python37
```

```get_rss
gcloud beta functions deploy get_rss --entry-point=get_rss --trigger-topic=datastore --source=src --runtime=python37
```

## スケジュール

```
gcloud scheduler jobs create pubsub feeder \
  --topic datastore \
  --message-body='fetch info' \
  --schedule '*/5 * * * *' \
  --time-zone='Asia/Tokyo'
```
