from setuptools import setup

setup(name='wordpresspy',
      version='0.0.9',
      long_description='Library for management WordPress and its plugins, please visit https://github.com/weecan-group/wordpresspy for documentation.',
      url='https://github.com/weecan-group/wordpresspy',
      author='Weecan',
      author_email='contato@moacirbrg.org',
      license='MIT',
      packages=['wordpresspy'],
      zip_safe=False,
      install_requires=[
        'six'
      ],
      classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ))
