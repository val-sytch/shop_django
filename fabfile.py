"""
To use this, you need to install fabric
http://www.fabfile.org/installing.html
"""
from fabric.api import local


def runserver():
    """
    Run Django development sever
    """
    local('python manage.py runserver')


def makemigr():
    """
    Create migrations after models changing
    """
    local('python manage.py makemigrations ')


def migrate():
    """
    Apply changes to database
    """
    local('python manage.py migrate')


def superuser():
    """
    Create superuser
    """
    local('python manage.py createsuperuser')


def runtest():
    """
    Run tests in djog
    """
    local('python manage.py test djog')


def write_breeds_in_db():
    """
    Launch script, which parse wiki and write all breeds to database
    """
    local('python djog/servises/parser_dog_breeds.py')


def download_img():
    """
    Launch script, which download pictures for each breed in db
    """
    local('python djog/servises/google_img_downloader.py')
