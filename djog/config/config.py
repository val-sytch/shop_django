import configparser
import os

path = os.path.realpath(os.path.dirname(__file__))
config = configparser.ConfigParser()
config.read(os.path.join(path, 'config.ini'))

DATABASE_NAME = config.get('DATABASE', 'DATABASE_NAME')
DATABASE_ENGINE = config.get('DATABASE', 'DATABASE_ENGINE')
DATABASE_USER = config.get('DATABASE', 'DATABASE_USER')
DATABASE_PASSWORD = config.get('DATABASE', 'DATABASE_PASSWORD')

DEBUG = config.get('OTHER', 'DEBUG')

SECRET_KEY = config.get('SECRET', 'SECRET_KEY')

APP_DIR = path.rsplit('/djog', 1)[0]
STATIC_URL = config.get('PATH', 'STATIC_URL')
UPLOAD_IMAGE = os.path.join(APP_DIR, config.get('PATH', 'UPLOAD_IMAGE'))
WATERMARK = os.path.join(APP_DIR, config.get('PATH', 'WATERMARK'))

IMG_WIDTH_REQUIR = int(config.get('IMAGERESIZER', 'WIDTH'))
IMG_HEIGHT_REQUIR = int(config.get('IMAGERESIZER', 'HEIGHT'))
WATERMARK_OPACITY = float(config.get('IMAGERESIZER', 'WATERMARK_OPACITY'))
