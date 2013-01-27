'''
:copyright: Copyright 2013 by christian.meichsner@informatik.tu-chemnitz.de, see AUTHORS.
:license: BSD, see LICENSE for details.
'''

from distutils.core import setup
setup(name='ComparareEtPendere',
      version='0.9',
      packages=['MultisourceHtmlFormatter'],
      provides=['MultisourceHtmlFormatter'],  
      description='Multisource Code Formatter outputting HTML. Based on pygments',
      author='Christian Meichsner',
      author_email='christian.meichsner@informatik.tu-chemnitz.de',
      url='https://github.com/gixxi/comparareetpendere',
      license="BSD",
      platforms="Tested with Python 3.1",
      keywords='sourcecode formatting html output pygments python documentation',
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 3',
                   'License :: OSI Approved :: BSD License',
                   'Topic :: Software Development :: Documentation'
                  ],      
      )
