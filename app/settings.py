import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
# 从环境变量读入配置信息
APP_NAMESPACE = os.getenv('APP_NAMESPACE', 'BLOG')
FLASK_DEBUG = bool(os.getenv('FLASK_DEBUG', 0) == 1)
FLASK_ENV = os.getenv('FLASK_ENV', 'production')
MYSQL_USERNAME = os.getenv('MYSQL_USERNAME', 'root')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'password')
MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', 'databases')
MYSQL_PORT = os.getenv('MYSQL_PORT', 3306)

app.config['FLASK_DEBUG'] = FLASK_DEBUG
app.config['FLASK_ENV'] = FLASK_ENV
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}' \
                                        f'@{MYSQL_HOST}:{MYSQL_PORT}' \
                                        f'/{MYSQL_DATABASE}?charset=utf8mb4'
# app.config['SQLALCHEMY_ECHO'] = FLASK_DEBUG
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
