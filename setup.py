import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hltv-data",
    version="0.2.1",
    author="Dariusz Choruzy",
    author_email="dariusz.choruzy@gmail.com",
    description="HLTV.org data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dchoruzy/hltv-data",
    project_urls={
        "Bug Tracker": "https://github.com/dchoruzy/hltv-data/issues",
    },
    license='MIT License',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "beautifulsoup4",
        "soupsieve",
        "requests",
    ]
)