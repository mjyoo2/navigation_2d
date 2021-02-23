from setuptools import setup
import sys
from os.path import dirname, realpath

def read_requirements_file(filename):
    req_file_path = '%s/%s' % (dirname(realpath(__file__)), filename)
    with open(req_file_path) as f:
        return [line.strip() for line in f]

# only support 2.7 for mujoco compatibility
if sys.version_info < (2,7):
    print('Sorry, Python < 2.7 is not supported, please install Python 3.7')
    sys.exit()

setup(name='navigation_2d',
      version='1.2.0',
      packages=['navigation_2d'],
      python_requires='>=3.7',
      install_requires=read_requirements_file('requirements.txt'),
      description='2d navigation environment with Box2D',
      author='Minjong Yoo, Gwangpyo Yoo',
      url='https://github.com/mjyoo2/2d_navi_with_obstacle',
)
