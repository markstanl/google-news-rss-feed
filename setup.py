from setuptools import setup, find_packages

setup(
    name='https://github.com/markstanl/google-news-rss-feed',
    version='1.0',
    description='As a demo for the wisconsin messenger role I just landed, I wanted to run'
                'some demo code to show how to parse an RSS feed. I chose the Google News RSS feed',
    author='markstanl',
    author_email='markgstanley1@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'feedparser',
        'yagmail'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.8',
    ],
)