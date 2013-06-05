import os
from setuptools import setup

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='djangocms_wymeditor_plugin',
    version='0.3.0',
    author='Nick McLaughlin, Ani Chan',
    author_email='n.mclaughlin22@yahoo.com, ani.chan844@gmail.com',
    packages=['djangocms_wymeditor_plugin',],
    url='https://github.com/FriedRice/djangocms_wymeditor_plugin.git',
    license='LICENSE.txt',
    description='A plugin for using WYMeditor in Django CMS 3',
    platforms=['OS Independent'],
    long_description=open('README.md').read(),
    include_package_data=True,
    zip_safe=False,
)
