"""
Created on Thu Jul 21 01:11:04 2016

@author: chc
"""

from setuptools import setup, find_packages

setup(name='crikit2',
      version = '17.10b1',
      description = 'Hyperspectral imaging (HSI) processing and analysis \
      platform (user interface, UI)',
      url = 'https://github.com/CoherentRamanNIST/crikit2',
      author = 'Charles H. Camp Jr.',
      author_email = 'charles.camp@nist.gov',
      license = 'NONLICENSE',
      packages = find_packages(),
      entry_points={
          'gui_scripts': (
              'crikit2-start = crikit.__main__:main')},
      zip_safe = False,
      include_package_data = True,
      install_requires=['numpy','matplotlib','scipy','sciplot-pyqt>=0.1.3', 
                        'h5py','cvxopt'],
      classifiers=['Development Status :: 2 - Pre-Alpha',
                   'Intended Audience :: Developers',
                   'Intended Audience :: Science/Research',
                   'Operating System :: OS Independent',
                   'Environment :: X11 Applications :: Qt',
                   'Programming Language :: Python :: 3 :: Only',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   'Topic :: Scientific/Engineering :: Visualization'])
