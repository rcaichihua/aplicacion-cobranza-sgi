## Collection application

Collection application for the SGI(Real estate management system)

- Install and created virtual environments

```shell
python -m venv venv
```

#

### Activate virtual environments

- windows

```shell
source venv/Scripts/activate
```

- MacOS

```shell
source venv/bin/activate
```

#

- Install Flask

```shell
pip install Flask
```

- Generate requirements.txt file

```shell
pip freeze > requirements.txt
```

- Reinstall dependencies from requirements.txt

```shell
pip install -r requirements.txt
```

- Declaration of environment variables

```python
FLASK_APP = main.py
FLASK_RUN_HOST = 127.0.0.1
FLASK_RUN_PORT = 6001
FLASK_DEBUG = true

DATABASE_URI =
'postgresql://postgres:1234@localhost:5432/sblm'
```

- Install to recognize the variables declared in the .env file

```shell
pip install python-dotenv
```

- Install psycopg2-binary for database client

```shell
pip install psycopg2-binary
```

- More practical and common than pony or tortoise

```shell
pip install SQLAlchemy
```

- Install Flask-Migrate

```shell
pip install Flask-Migrate
```

- Migration

```properties
flask db init -> migration starts once / beginning
```

```properties
flask db migrate -m "comment" -> second step
```

```properties
flask db upgrade -> Execute the migrations
```

- Install flask-restx restx-monkey

```shell
pip install flask-restx restx-monkey
```

- Install sql alchemy mixins

```shell
pip install sqlalchemy_mixins
```

- Install flask Marshmallow and marshmallow sqlalchemy -> for serialization

```shell
pip install flask-marshmallow
```

```shell
pip install marshmallow-sqlalchemy
```

- to encrypt password

```shell
pip install bcrypt
```

- to created token jwt

```shell
pip install flask-jwt-extended
```

### Mail encryption

```properties
MAIL_SERVER="smtp.gmail.com"
MAIL_PORT=587
MAIL_USE_TLS=true
MAIL_USERNAME="xxxx@xxxx.com"
MAIL_PASSWORD="xxxxxx"
```

- Install Send Email

```shell
pip install Flask-Mail
```

- Install Cors security

```shell
pip install flask-cors
```
