import os
from setuptools import setup

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='djangocms_wymeditor_plugin',
    version='0.1.0',
    author='',
    author_email='',
    packages=['djangocms_wymeditor_plugin',],
    url='https://github.com/FriedRice/djangocms_wymeditor_plugin.git',
    license='',
    description='A plugin for using WYMeditor in Django CMS',
    include_package_data=True,
    zip_safe=False,
)
