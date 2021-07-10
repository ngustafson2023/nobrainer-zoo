from setuptools import setup

setup(
    name="nobrainer-zoo",
    version='0.0.1',
    py_modules=['cli'],
    install_requires=[
        'Click',
        'pyyaml'
    ],
    entry_points='''
        [console_scripts]
        nobrainer-zoo=nobrainerzoo.cli:cli
    ''',
)