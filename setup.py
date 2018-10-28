
from setuptools import setup
from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

pipfile = Project(chdir=False).parsed_pipfile

setup(
    name="Maglev",
    version="1.0.0",
    author="Jeremy Potter",
    author_email="pypi@stormdesign.us",
    description=("PHP-like Async/IO web framework"),
    long_description=read("README.md"),
    license="GNU",
    keywords="web framework mako asyncio",
    install_requires=convert_deps_to_pip(pipfile["packages"], r=False),
    packages=["maglev"],
    scripts=["maglev-serve"]
)