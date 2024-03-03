from setuptools import setup, find_packages

setup(
    name='web_assets_downloader',
    version='1.0.5',
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
    long_description='A package for downloading web content and assets from URLs.',
    long_description_content_type='text/plain',
    license='MIT',
    keywords='web downloader requests BeautifulSoup',
    url='https://github.com/arif-x/web-assets-downloader',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
)