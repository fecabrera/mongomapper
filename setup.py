from setuptools import find_packages, setup

setup(
  name='mongomapper',
  packages=find_packages(include=['mongomapper']),
  version='0.1.0',
  description='MongoMapper',
  install_requires=open('requirements.txt').read().split(),
  author='Felipe Cabrera',
  author_email='fecabrera@protonmail.com',
  license='MIT',
)