from setuptools import setup, find_packages
setup(
    name="lambdata",
    version="0.1",
    packages=find_packages(),
    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=["pandas>=1.0.0"],
    # metadata to display on PyPI
    author="Isaac Grove",
    author_email="isaacgrove333@gmail.com",
    description="Unit 3 lambdata package",
    keywords="",
    url="",   # project home page, if any
    classifiers=[
        "License :: MIT"
    ]
    # could also include long_description, download_url, etc.
)