from setuptools import setup

setup(
    name='image-uploader',
    packages=['image-uploader'],
    include_package_data=True,
    version='0.1',
    url='https://github.com/Morikko/flask-image-uploader',
    install_requires=[
        'flask==0.12.2',
        'gunicorn==19.7.1',
    ],
)
