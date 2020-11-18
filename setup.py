import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="video-thumbnail-maker-edmpark", # Replace with your own username
    version="0.0.1",
    author="Edmond P",
    author_email="edmondpark1@gmail.com",
    description="Make video thumnails in a montage/collage format",
    long_description="Please read the README file in github link",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)