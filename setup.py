#StudentUnderground/setup.py
from setuptools import setup

setup(name='clusterblog',
      version='0.1dev',
      description="Clusterflunk's flunking awesome blog.",
      long_description='',
      install_requires=['pyramid==1.4a2',
                        'mako',
                        'sqlalchemy',
                        'zope.sqlalchemy',
                        'pyramid_redis_sessions',
                        'waitress',
                        'nose',
                        'coverage',
                        'markdown'],
      packages=['clusterblog'],
      test_suite='clusterblog.tests',
      entry_points="""\
      [paste.app_factory]
      main = clusterblog:main
      """,
      )
