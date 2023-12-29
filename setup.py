import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "red_wine_quality"
AUTHOR_USER_NAME = "prasad535"
SRC_REPO = "wine_quality"
AUTHOR_EMAIL = "prasad.nagineni12345@gmail.com"


setuptools.setup(
    name = SRC_REPO,
    version = __version__, 
    author = AUTHOR_USER_NAME, 
    author_email = AUTHOR_EMAIL,
    description= "A small ML End to end project description",
    long_description = long_description,
    long_description_content="text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_url = {
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir= {"":"src"},
    packages=setuptools.find_packages(where='src')
)