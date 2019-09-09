from setuptools import setup

requires = ["matplotlib"]

setup(
    name="PyACO",
    version="1.0",
    description="Ant Colony Optimization in python",
    url="https://github.com/Ganariya/PyACO",
    author="ganariya",
    license="MIT",
    keywords="ACO python",
    packages=[
        "PyACO"
    ],
    install_requires=requires,
    classifiers=[
        "Programming Language :: Python :: 3.6"
    ],
    long_description="This Package is able to use ACO in Python."

)
