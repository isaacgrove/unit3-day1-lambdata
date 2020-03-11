import setuptools

REQUIRED = [
    "numpy",
    "pandas",
    "scikit-learn"
]

setuptools.setup(
    name="lambdata-isaacgrove",
    version="0.8",
    packages=setuptools.find_packages(),
    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=REQUIRED,
    # metadata to display on PyPI
    author="isaacgrove",
    author_email="isaacgrove333@gmail.com",
    description="Lambda DS Unit 3 lambdata - helper functions",
    keywords="",
    url="",   # project home page, if any
    classifiers=[
        "License :: OSI Approved :: MIT License"
    ]
    # could also include long_description, download_url, etc.
)