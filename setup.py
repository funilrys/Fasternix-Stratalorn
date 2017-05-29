#    Fasternix Stratalorn -  Python module/library for saving the list of translators of a given Transifex project into a JSON file.

#    Copyright (C) 2017  Funilrys - Funilrys - Nissar Chababy <contact at funilrys dot com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

#    https://github.com/funilrys/Fasternix-Stratalorn

from distutils.core import setup

setup(
    name='fasternix_stratalorn',
    version="1.0.0",
    description='Python module/library for saving the list of translators of a given Transifex project into a JSON file.',
    long_description=open('README').read(),
    author='funilrys',
    author_email='contact@funilrys.com',
    license='GPL-3.0 https://opensource.org/licenses/GPL-3.0',
    url='https://github.com/funilrys/Fasternix-Stratalorn',
    platforms=['any'],
    packages=['fasternix_stratalorn'],
    keywords=['Python', 'JSON', 'transifex','translator','translators'],
    classifiers=[
        'Environment :: Console',
        'Topic :: Internet',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)'
    ],
)

'''
test_suite='testsuite',
entry_points="""
[console_scripts]
cmd = package:main
""",
'''
