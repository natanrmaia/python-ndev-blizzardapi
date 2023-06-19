from setuptools import setup, find_packages

setup(
    name="python-ndev-blizzardapi",
    version="0.0.4",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.2",
    ],
    author="natanrmaia",
    author_email="contato@natanael.dev.br",
    description="Python module created to integrate your Python project with the Blizzard API",
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/natanrmaia/python-ndev-blizzardapi",
    project_urls={
        'Documentation': 'https://python-ndev-blizzardapi.readthedocs.io/en/latest/',
        'Source': 'https://github.com/natanrmaia/python-ndev-blizzardapi',
        'Bug Reports': 'https://github.com/natanrmaia/python-ndev-blizzardapi/issues',
    },    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
