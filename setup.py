from setuptools import setup, find_packages

setuptools.setup(
        name='pyblep',
        version='0.0.0',
        description='Python Beam Line Exchange Protocol',
        author='Riccardo De Maria',
        author_email='riccardo.de.maria@cern.ch',
        url='https://github.com/rdemaria/pyblep',
        packages=find_packages(),
        install_requires=['numpy'],
)
