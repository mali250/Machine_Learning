from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    This function gives the list of requirements directly from the file.
    """
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
    return requirements

setup(
    name="project",
    version="0.2.5",
    author="rana",
    author_email="alimuazzam2000@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirments.txt'),  # Fix the typo in the filename
)
