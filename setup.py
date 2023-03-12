from setuptools import setup

setup(
    version='0.1',
    name='GLPIScan',
    author='Digitemis',
    install_requires=['pychalk>=2.0.1', 'requests>=2.18.4', 'urllib3>=1.25.8', 'packaging>=19.0'],
    entry_points = {
        'console_scripts': ['glpiscan = glpiscan.GLPIScan:main'],
    }
)
