from setuptools import setup, find_packages

setup(
    name='nextmatter_api_wrapper',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'python-dotenv',
        'pydantic',
        'python-dateutil',
    ],
    test_suite='tests',
)