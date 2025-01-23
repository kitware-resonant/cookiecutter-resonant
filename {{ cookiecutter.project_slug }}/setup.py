from pathlib import Path

from setuptools import find_packages, setup

readme_file = Path(__file__).parent / 'README.md'
if readme_file.exists():
    with readme_file.open() as f:
        long_description = f.read()
else:
    # When this is first installed in development Docker, README.md is not available
    long_description = ''

setup(
    name='{{ cookiecutter.project_slug }}',
    version='0.1.0',
    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='Apache 2.0',
    author='Kitware, Inc.',
    author_email='kitware@kitware.com',
    keywords='',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django :: 5',
        'Framework :: Django :: 5.1',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python',
    ],
    python_requires='>=3.10',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'celery',
        'django[argon2]',
        'django-allauth',
        'django-auth-style',
        'django-cors-headers',
        'django-environ',
        'django-extensions',
        'django-filter',
        'django-oauth-toolkit',
        'django-resonant-settings[allauth]',
        'django-resonant-utils',
        'djangorestframework',
        'drf-yasg',
        'psycopg[binary]',
        'rich',
        'whitenoise[brotli]',
        # Production-only
        'django-s3-file-field[s3]',
        'django-storages[s3]',
        'gunicorn',
        'sentry-sdk',
    ],
    extras_require={
        'dev': [
            'django-debug-toolbar',
            'django-minio-storage',
            'django-s3-file-field[minio]',
            'ipython',
            'tox',
        ]
    },
)
