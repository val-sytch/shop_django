import configparser
import os

path = os.path.realpath(os.path.dirname(__file__))
config = configparser.ConfigParser(interpolation=None)
config.read(os.path.join(path, 'config.ini'))

DATABASE_NAME = config.get('DATABASE', 'database_name')
DATABASE_ENGINE = config.get('DATABASE', 'database_engine')
DATABASE_USER = config.get('DATABASE', 'database_username')
DATABASE_PASSWORD = config.get('DATABASE', 'database_password')

DEBUG = config.get('OTHER', 'debug')

SECRET_KEY = config.get('SECRET', 'secret_key')

APP_DIR = path.rsplit('/djog', 1)[0]
STATIC_URL = config.get('PATH', 'static_url')
UPLOAD_IMAGE = os.path.join(APP_DIR, config.get('PATH', 'upload_image'))
WATERMARK = os.path.join(APP_DIR, config.get('PATH', 'watermark'))

IMG_WIDTH_REQUIR = int(config.get('IMAGERESIZER', 'width'))
IMG_HEIGHT_REQUIR = int(config.get('IMAGERESIZER', 'height'))
WATERMARK_OPACITY = float(config.get('IMAGERESIZER', 'watermark_opacity'))
