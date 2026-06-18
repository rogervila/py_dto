from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='py_dto',
    packages=['py_dto'],
    version='CURRENT_VERSION',
    license='MIT',
    description='data transfer objects with Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.9',
    author='Roger Vilà',
    author_email='rogervila@me.com',
    url='https://github.com/rogervila/py_dto',
    download_url='https://github.com/rogervila/py_dto/archive/CURRENT_VERSION.tar.gz',
    keywords=['python data transfer objects', 'data transfer objects', 'python dto', 'dto'],
    install_requires=[
        'runtype >= 0.5.0',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
    ],
)
