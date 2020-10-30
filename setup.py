import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Important-Places", # Replace with your own username
    version="0.0.1",
    author="Benedict Flexen",
    author_email="benedict.flexen@gmail.com",
    description="An aplication that displays visualisations of data from important places",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    scripts = ["Important-Places/important-places.py"]
    ],
    python_requires='>=3.6',
)
