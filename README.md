# Heroku-Holiday
---

Heroku上で祝日API

## 手順

ローカルリポジトリを作成

```cmd
$ mkdir Heroku-Holiday
$ cd Holiday
$ git init
```

仮想環境を作成

```cmd
$ conda create -n py37flask python=3.7
```

PowerShellの場合、`activate`実行前に以下のコマンドを実行

```powershell
PS> conda install -n root -c pscondaenvs pscondaenvs
```

仮想環境に切り替えて必要なパッケージをインストール

```cmd
$ activate py37flask
$ pip install Flask
$ pip install flask-migrate
$ pip install flask-sqlalchemy
$ pip install gunicorn
$ pip install psycopg2
$ pip install requests
$ pip install sqlalchemy
```

index.pyの編集

```cmd
$ nano index.py
```

ローカルで走らせる

```cmd
$ python index.py
```

設定ファイル類を作成

```cmd
$ nano Procfile
$ pip freeze > requirements.txt
```

ローカルリポジトリにコミット

```cmd
$ git add .
$ git commit -m 'init'
$ git push origin master
```

Herokuにプッシュ

```cmd
$ heroku login
$ heroku create holid
$ git push heroku master
$ heroku scale web=1
$ heroku open
```

終わったら仮想環境から抜ける

```cmd
$ deactivate
```
