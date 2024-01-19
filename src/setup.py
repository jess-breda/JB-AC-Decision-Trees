from setuptools import setup, find_packages
from pathlib import Path

# Path to the directory of setup.py
setup_dir = Path(__file__).parent

# Path to requirements.txt (two directories up)
requirements_path = setup_dir.parent / "requirements.txt"

# Read the contents of the requirements file
with open(requirements_path) as f:
    requirements = f.read().splitlines()

setup(
    name="decision_trees",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements,
    description="Decision Trees Mini Project",
    author="Jess Breda",
    author_email="jbreda19@gmail.com",
)
