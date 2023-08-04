from pathlib import Path

from setuptools import find_packages, setup

readme_file = Path(__file__).parent / 'README.md'
if readme_file.exists():
    with readme_file.open() as f:
        long_description = f.read()
else:
    # When this is first installed in development Docker, README.md is not available
    long_description = ''

setup(
    name='isic-oauth-example',
    version='0.1.0',
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='Apache 2.0',
    url='https://github.com/ImageMarkup/isic-oauth-example',
    project_urls={
        'Bug Reports': 'https://github.com/ImageMarkup/isic-oauth-example/issues',
        'Source': 'https://github.com/ImageMarkup/isic-oauth-example',
    },
    author='Kitware, Inc.',
    author_email='kitware@kitware.com',
    keywords='',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python',
    ],
    python_requires='>=3.9',
    packages=find_packages(),
    include_package_data=True,
    # manually require requests for authlib: https://github.com/lepture/authlib/issues/365
    install_requires=['flask', 'authlib', 'requests'],
    extras_require={
        'dev': [
            'ipython',
            'tox',
        ]
    },
)
