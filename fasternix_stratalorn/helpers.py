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

from json import loads, dump

def write_file(content,destination):
    """Write a content in a given file

    :param content: A string, the content we have to write into the file
    :param destination: A string, A path to a file where we're going to save the content
    """

    with open(destination,'w') as file:
        file.write(content)

def read_file(file_to_read):
    """Read the content of a given file

    :param file_to_read: A string, a path to the file we have to read
    """

    with open(file_to_read,'r') as file:
        funilrys = file.read()
    return funilrys

def convert_JSON_to_dict(data):
    """Convert a JSON into a dictionary

    :param data: A string, a JSON formated string
    """

    return loads(data)

def save_dict_to_JSON(data,destination):
    """Save a dictionary into a JSON format

    :param data: A dict
    :param destination: A string, A path to a file where we're going to write the converted dict into a JSON format
    """

    with open(destination, 'w') as file:
        dump(data, file, ensure_ascii=False, indent=4, sort_keys=True)
