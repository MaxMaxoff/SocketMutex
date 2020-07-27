# -*- coding: utf-8 -*-

from distutils.core import setup
setup(
  name = 'Mutex',
  packages = ['Mutex'],
  version = '0.1',
  license = 'MIT',
  description = "module for realize locking mechanism using sockets",
  author = 'Maxim Toropov',
  author_email = 'maxim.vt at gmail.com',
  url = '',
  download_url = '',
  keywords = ['locking', 'lock', 'mutex', 'socket', 'run-once'],
  install_requires = [
      ],
  classifiers = [
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable      
    'Development Status :: 5 - Production/Stable',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ]
)