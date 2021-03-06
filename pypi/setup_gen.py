#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from pkgversion import list_requirements, pep440_version, write_setup_py
from setuptools import find_packages

write_setup_py(
    file='./setup.py',
    name='bitdust-p2p',
    version='0.0.2',
    description="BitDust is new software framework to build distributed and secure peer-to-peer applications.",
    long_description=open('README.md').read(),
    author="Veselin Penev",
    author_email='bitdust.io@gmail.com',
    url='https://github.com/bitdust-io/public.git',
    install_requires=list_requirements('requirements.txt'),
    packages=find_packages(exclude=['deploy*', 'icons*', 'release*', 'scripts*', 'devops*', 'regress*', 'requirements*', 'venv*', ]),
    tests_require=[],
    include_package_data=True,
    zip_safe=False,
    license='GNU Affero General Public License v3 or later (AGPLv3+)',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: No Input/Output (Daemon)',
        'Framework :: Twisted',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Communications :: Chat',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Communications :: File Sharing',
        'Topic :: Desktop Environment :: File Managers',
        'Topic :: Internet :: File Transfer Protocol (FTP)',
        'Topic :: Security :: Cryptography',
        'Topic :: System :: Archiving :: Backup',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Filesystems',
        'Topic :: System :: System Shells',
        'Topic :: Utilities',
    ]
)
