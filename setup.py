from setuptools import setup, find_namespace_packages

setup(name='clean-folder',
      version='1',
      description='Script to sort files in a directory',
      url='https://github.com/Ar-Dante/clean_folder.git',
      author='Ar.Dante',
      author_email='abc',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean-folder=clean-folder.clean:main']}
      )
