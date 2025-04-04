from setuptools import setup, find_packages

setup(
    name='ChatSelfbot',
    version='1.0.0',
    description='A fast and light selfbot made by Bjarnos for Chat (a program by Jona Zwetsloot)!',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Bjarnos',
    author_email='contact@bjarnos.dev',
    url='https://github.com/Bjarnos/SelfbotSource',
    packages=find_packages(),
    install_requires=[
      'requests',
      'beautifulsoup4',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
