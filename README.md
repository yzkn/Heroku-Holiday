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
$ pip install flask-cors
$ pip install flask-migrate
$ pip install flask-sqlalchemy
$ pip install gunicorn
$ pip install psycopg2
$ pip install pytest
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

ローカルにDBを用意

```powershell
$ createdb -U postgres -W {パスワード}holiday
```

マイグレーション

```powershell
$ python
```

```python
from index import db
db.create_all()
```

pytestの実行

```cmd
$ pytest .\tests\test_date_util.py
```

Herokuへ反映

```cmd
$ git push heroku master
$ heroku addons:add heroku-postgresql
$ heroku config:set DATABASE_URL="{HerokuのDatabase CredentialsにあるURL}"
$ heroku run python
```

```python
from index import db
db.create_all()
from index import db,Holiday
Holiday.query.all()
```

終わったら仮想環境から抜ける

```cmd
$ deactivate
```
