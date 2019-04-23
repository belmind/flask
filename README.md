## Learning Flask
Available: https://flask-bd.herokuapp.com/

### Installation
[Flask Installation](http://flask.pocoo.org/docs/1.0/installation/#installation)

### Deploy to Heroku
```
1. $ heroku create <app-name>
2. $ pip freeze >> requirements.txt
3. $ heroku run python server.py deploy
4. $ heroku ps:scale web=1
5. $ heroku restart
```
