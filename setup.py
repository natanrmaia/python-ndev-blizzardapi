from setuptools import setup, find_packages

setup(
    name="python-ndev-blizzardapi",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="natanrmaia",
    author_email="contato@natanael.dev.br",
    description="Python module created to integrate your Python project with the Blizzard API",
    long_description="Python module created to integrate your Python project with the Blizzard API",
    long_description_content_type="text/markdown",
    url="https://github.com/natanrmaia/python-ndev-blizzardapi",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
