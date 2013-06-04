import os
from setuptools import setup

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-wymeditor',
    version='0.0.1',
    author=u'',
    author_email='',
    packages=['django_wymeditor',],
    url='',
    license='BSD licence, see LICENCE.txt',
    description='',
    include_package_data=True,
    zip_safe=False,
)
