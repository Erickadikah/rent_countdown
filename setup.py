from setuptools import setup, find_packages

setup(
    name='rent_countdown',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    description='A Python library for managing rent expiration countdowns',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    license='MIT',
    url='https://github.com/Erickadikah/rent_countdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
)
