mkdir dist
cd dist/
mkdir ai42
echo "from setuptools import setup

setup(name='ai42',
      version='1.0.0',
      description='Made by tmarcon',
      author='tmarcon',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['ai42'],
      zip_safe=False)" > ai42/setup.py
mkdir ai42/ai42
echo "import ai42.progressbar
import ai42.logging.log" > ai42/ai42/__init__.py

cp ../progressbar.py ai42/ai42/
cp ../logging.py ai42/ai42/

tar -cvzf ai42-1.0.0.tar.gz ai42/
