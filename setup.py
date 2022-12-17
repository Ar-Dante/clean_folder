from setuptools import setup, find_namespace_packages

setup(name='clean-folder',
      version='1',
      description='Script to sort files in a directory',
      url='https://github.com/Ar-Dante/clean_folder.git',
      author='ArDante',
      author_email='ar.dantess@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_point={'console_scripts': ['CleanFolder=clean-folder.clean:main']}
      )
