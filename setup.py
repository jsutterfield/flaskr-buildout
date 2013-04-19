from setuptools import setup, find_packages

setup(
    name = 'flaskr',
    version = '1.0',
    description = 'A micro blog using flask',
    author = 'James Sutterfield',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools',
                        'Flask',
                        ],
    entry_points="""
    [console_scripts]
    flask-ctl = flaskr.script:runserver
    """
)
