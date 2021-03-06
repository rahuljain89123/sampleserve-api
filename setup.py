
from setuptools import setup

setup(
    name='sampleserve',
    packages=['sampleserve'],
    include_package_data=True,
    install_requires=[
        'alembic>=0.8',
        'flask>=0.12',
        'flask-login>=0.4',
        'flask-bcrypt>=0.7',
        'flask-sqlalchemy>=2.1',
        'flask-cors>=3.0',
        'jsonschema>=2.6',
        'psycopg2>=2.6',
        'flask-mail',
        'hashids>=1.2.0',
        'requests',
        'pandas>=0.20.2',
        'flask-wtf',
        'wtforms-json',
        'wtforms-alchemy',
        'raven',
        'flask-admin',
        'numpy==1.9.0',
        'matplotlib==1.3.1',
        'Pillow==2.5.0',
        'Cython==0.18',
        'unidecode',
        'docraptor',
    ],
    setup_requires=[
        'pytest-runner>=2.11',
    ],
    dependency_links=[
        'https://github.com/scipy/scipy@38ad5d2183b76e1ae4466916126c92c03af6404a#egg=scipy',
    ],
    tests_require=[
        'pytest>=3.0',
        'pytest-cov>=2.4',
    ],
    test_suite='pytest',
)
