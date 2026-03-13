from setuptools import setup, find_namespace_packages
import os

pkg_version = '0.0.1rc21'

dir = os.path.dirname(__file__)
if dir == '':
   rwd = os.path.abspath('.')
else:
   rwd = os.path.abspath(dir)
with open(os.path.join(rwd, 'README.md'), encoding='u8') as f:
   long_description = f.read()

sub_packages = find_namespace_packages(
   where='dggal/high-vibes',
   include=['dggsExport', 'dggsImport', 'dggsStore', 'fg', 'ogcapi', 'ogcapi.common', 'ogcapi.dggs']
)
setup(
   name='dgg_vibes',
   version=pkg_version,
   install_requires=['dggal >= 0.0.7rc1', 'shapely', 'numpy', 'rasterio', 'pyproj', 'py-ubjson', 'flask', 'requests', 'geopandas', 'pyarrow' ], # 'pyogrio' ],
   packages=['dgg_vibes'] + [f"dgg_vibes.{p}" for p in sub_packages],
   py_modules=[
      'dgg_export',
      'dgg_fetch',
      'dgg_fg',
      'dgg_import',
      'dgg_serve',
      'dgg_togeo'
   ],
   package_dir={'dgg_vibes': 'dggal/high-vibes'},
   entry_points={
      'console_scripts': [
         'dgg-export = dgg_vibes.dgg_export:main',
         'dgg-fetch  = dgg_vibes.dgg_fetch:main',
         'dgg-fg     = dgg_vibes.dgg_fg:main',
         'dgg-import = dgg_vibes.dgg_import:main',
         'dgg-serve  = dgg_vibes.dgg_serve:main',
         'dgg-togeo  = dgg_vibes.dgg_togeo:main',
      ]
   },
   description='DGGAL High Vibes (vibe-coded high level DGGS tools using DGGAL)',
   url='https://dggal.org',
   long_description=long_description,
   long_description_content_type='text/markdown',
   author='Jérôme Jacovella-St-Louis, Ecere Corporation',
   author_email='jerome@ecere.com',
   license='BSD-3-Clause',
   keywords='dggs hexagonal-grid global-grid ogc ogc-api gnosis dggrs isea ivea rtea isea3h isea9r ivea3h ivea9r slice-and-dice polyhedral-globe icosahedral rhealpix',
   classifiers=[
      'Development Status :: 4 - Beta',
      'Environment :: Console',
      'Intended Audience :: Developers',
      'Intended Audience :: Science/Research',
      'Operating System :: Microsoft :: Windows',
      'Operating System :: POSIX :: Linux',
      'Operating System :: MacOS',
      'Programming Language :: Python :: 3',
      'Topic :: Scientific/Engineering :: GIS',
      'Topic :: Scientific/Engineering :: Astronomy',
      'Topic :: Scientific/Engineering :: Atmospheric Science',
      'Topic :: Scientific/Engineering :: Hydrology',
      'Topic :: Scientific/Engineering :: Image Processing',
      'Topic :: Scientific/Engineering :: Information Analysis',
      'Topic :: Scientific/Engineering :: Oceanography',
      'Topic :: Scientific/Engineering :: Visualization',
   ],
)
