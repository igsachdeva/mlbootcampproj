from setuptools import setup, find_packages
from typing import List

hyp="-e ."

def get_requirement(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if hyp in requirements:
            requirements.remove(hyp)
        
    return requirements

setup(
    name='src',
    version='0.0.1',
    author='sunny',
    author_email='kuchbhi@gmail.com',
    install_requires=get_requirement("requirements.txt"),
    packages=find_packages()
)
