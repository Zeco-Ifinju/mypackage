from setuptools import setup, find_packages

setup(
    name= 'mypackage',
    version= "0.1",
    packages= find_packages(exclude=["test"]),
    license= "MIT",
    description= "EDSA Exanole python Package",
    long_description=open('README.md').read(),
    insatll_requires=["numpy"],
    url= 'http.github.com//',
    author= "Ifinju Isaac",
    Email= "isaacIfinju@gmail,com")