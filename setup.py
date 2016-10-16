from setuptools import setup, find_packages

setup(
    name='djog',
    version='1.0',
    packages=find_packages(),
    install_requires=['Django==1.8',
                      'google-api-python-client',
                      'Pillow',
                      'lxml',
                      'beautifulsoup4'
                      ],
    include_package_data=True,
    url='https://github.com/val-sytch/shop_django',
    author='',
    description='Dogs shop on Django'
)
