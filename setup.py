import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="instagiveaway",
    version="0.0.1",
    author="Konstantinos Oikonomou",
    author_email="kons.oikonomou@gmail.com",
    description="An python package for instagram giveaways",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/konoikon/instagiveaway",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
