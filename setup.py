from setuptools import setup, find_packages

setup(
    name='web_assets_downloader',
    version='1.0.3',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4'
    ],
    entry_points={
        'console_scripts': [
            'web-assets-downloader = web_assets_downloader.downloader:main'
        ]
    },
    author='Ariffudin',
    author_email='sudo.ariffudin@email.com',
    description='A package for downloading web content and assets',
    license='MIT',
    keywords='web downloader requests BeautifulSoup',
    url='https://github.com/arif-x/web_downloader',
)