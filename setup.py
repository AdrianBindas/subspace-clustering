from setuptools import setup, find_packages

setup(
    name="subspace-clustering",
    version="1.0",
    description="Fork of Chong You's toolbox for large scale subspace clustering, updated with setup.py for python packaging.",
    url="https://github.com/AdrianBindas/subspace-clustering",
    author="Chong You",
    author_email="chong.you1987@gmail.com",
    license="MIT",
    project_urls={
        'Source': 'https://github.com/ChongYou/subspace-clustering/',
        'Fork': 'https://github.com/AdrianBindas/subspace-clustering',
    },
    packages=find_packages(),
    install_requires=["numpy", "scipy", "scikit-learn", "progressbar2", "kymatio"]
)