import re
from setuptools import setup

with open('TvPy/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

setup(
    name='TvPy',
    version=version,
    packages=['TvPy'],
    entry_points={
        "console_scripts": ['TvPy = TvPy.TvPy:main']
    },
    description='Command line remote for Soney Bravia Tv',
    long_description='Command line remote for Soney Bravia Tv',
    url='https://github.com/HimanshuAttri/TvPy',
    download_url='https://github.com/HimanshuAttri/TvPy/archive/master.zip',
    author='HimanshuAttri',
    license='GNU Affero General Public License v3 or later (AGPLv3+)',
    keywords=['Sony Bravia Remote', 'Sony', 'Bravia', 'Remote'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Home Automation',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=[
        'requests'
        
    ],
)
