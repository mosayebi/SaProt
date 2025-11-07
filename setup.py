from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

__pkg_name__ = 'saprot'
setup(name=__pkg_name__,
      version='0.0.1',
      description='SaProt',
      #url='https://github.com/westlake-repl/SaProt',
      #scripts=["scripts/run_inference.py"],
      install_requires=requirements,
      entry_points = {
        'console_scripts': [
            '{0} = {0}:main'.format(__pkg_name__)
        ]
      },
      packages=find_packages(),
)
