from distutils.core import setup

setup(
    name='mailer-jinja2',
    packages=['mailer_jinja2'],  # this must be the same as the name above
    version='0.1',
    description='A Python 3 mailer package with Jinja2 template',
    author='Theo Bouwman',
    author_email='theobouwman98@gmail.com',
    url='https://github.com/theobouwman/mailer',  # use the URL to the github repo
    download_url='https://github.com/peterldowns/mypackage/tarball/0.1',  # I'll explain this in a second
    keywords=['mail', 'template'],  # arbitrary keywords
    classifiers=[],
    package_dir= {'': 'src'},
    install_requires=['Jinja2>=2.9,<3'],
)
