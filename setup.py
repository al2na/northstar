import os
from setuptools import setup, find_packages



def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        out = f.read()
    return out


def update_version():
    ver = read('VERSION').rstrip('\n')
    fdn = os.path.join(os.path.dirname(__file__), 'semiknn')
    fn = os.path.join(fdn, 'version.py')
    with open(fn, 'wt') as f:
        f.write('version = "{:}"'.format(ver))
    return ver


setup(
    name="semiknn",
    version=update_version(),
    author="Fabio Zanini",
    author_email="fabio.zanini@fastmail.fm",
    description="Semi-supervised k-nearest neighbor graphs.",
    license="MIT",
    keywords="graph semi-supervised",
    url="https://github.com/iosonofabio/semiknn",
    packages=['semiknn'] + ['singlet.' + s for s in find_packages(where='semiknn')],
    long_description='''
    Semi-supervised knn graph construction

    ''',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
