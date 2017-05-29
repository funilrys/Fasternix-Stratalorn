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

from subprocess import Popen, PIPE

class Process(object):
    """A class to manipulate shell commands

    :param command: A string, the command to execute
    """

    def __init__(self, command):
        self.DECODE_TYPE = 'utf-8'
        self.command = command

    def decode_output(self,to_decode):
        """Decode the output of a shell command in order to be readable

        :param to_decode: byte(s), Output of a command
        """

        return to_decode.decode(self.DECODE_TYPE)

    def execute(self):
        """Execute a given command"""

        process = Popen(self.command,stdout=PIPE, stderr=PIPE, shell=True)
        (output,error) = process.communicate()

        if process.returncode != 0:
            return self.decode_output(error)
        return self.decode_output(output)
