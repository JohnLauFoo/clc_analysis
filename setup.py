from setuptools import setup, find_packages, Command
import os


class CleanCommand(Command):
    # override the abstract methods
    # look more into abstract class in python
    user_options = []
    def initialize_options(self): pass
    def finalize_options(self): pass

    def run(self):
        os.system('rmdir -vrf ./*.pyc ./*.tgz ./*.egg-info')


VERSION = '0.0.1'
DESCRIPTION = 'clc_analysis 0.0.1'
LONG_DESCRIPTION = 'closed loop control project analysis package'

setup(
    name="clc_analysis",
    version=VERSION,
    author='Mengzhan Liufu',
    author_email="mliufu@uchicago.edu",
    url='https://bitbucket.org/EMK_Lab/clc_analysis/',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy',
                      'scipy'],
    keywords=['closed-loop control', 'analysis'],
    classifiers=[],
    cmdclass={
        'clean': CleanCommand,
        # this command automatically remove all the cache files
    }
)