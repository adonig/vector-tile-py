from setuptools import setup, find_packages
import sys, os

# Parse the version from the fiona module.
with open('vector_tile/__init__.py') as f:
    for line in f:
        if line.find("__version__") >= 0:
            version = line.split("=")[1].strip()
            version = version.strip('"')
            version = version.strip("'")
            continue

setup(name='vector_tile',
      version=version,
      description="Python implementation of Mapbox vector tiles",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Sean Gillies',
      author_email='sean@mapbox.com',
      url='https://github.com/mapbox/vector-tile-py',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'protobuf'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

