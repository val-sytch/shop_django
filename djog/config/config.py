import configparser
import os

path = os.path.realpath(os.path.dirname(__file__))
config = configparser.ConfigParser(interpolation=None)
file_config = 'config{0}.ini'.format("_" + os.environ.get('DJANGO_PROJ_MODE')
                                     if os.environ.get('DJANGO_PROJ_MODE') else '')
config.read(os.path.join(path, file_config))

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

IMG_WIDTH_REQUIR = int(config.get('IMAGES', 'width'))
IMG_HEIGHT_REQUIR = int(config.get('IMAGES', 'height'))
WATERMARK_OPACITY = float(config.get('IMAGES', 'watermark_opacity'))
NUMBER_IMG_REQUIR = int(config.get('IMAGES', 'numb_img_requir'))
