#!/bin/env python

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

#    Original Version: https://github.com/funilrys/Fasternix-Stratalorn

from core import Core
from getpass import getpass

def get_translators(username,password,project_slug):
    """Send data and perform Core()"""

    return Core(username,password,project_slug).get()


username = input('Transifex username: ')
password = getpass('Transifex password: ')
project_slug = input('Transifex project_slug: ')

get_translators(username,password,project_slug)
