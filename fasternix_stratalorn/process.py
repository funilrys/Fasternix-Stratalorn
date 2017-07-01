#!/bin/env python

# Fasternix Stratalorn -  Python module/library for saving the list of translators of a given Transifex project into a JSON file.
# Copyright (C) 2017  Funilrys - Nissar Chababy <contact at funilrys dot com>
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Original Version: https://github.com/funilrys/Fasternix-Stratalorn

from subprocess import PIPE, Popen


class Process(object):
    """A class to manipulate shell commands

    :param command: A string, the command to execute
    """

    def __init__(self, command):
        self.DECODE_TYPE = 'utf-8'
        self.command = command

    def decode_output(self, to_decode):
        """Decode the output of a shell command in order to be readable

        :param to_decode: byte(s), Output of a command
        """

        return to_decode.decode(self.DECODE_TYPE)

    def execute(self):
        """Execute a given command"""

        process = Popen(self.command, stdout=PIPE, stderr=PIPE, shell=True)
        (output, error) = process.communicate()

        if process.returncode != 0:
            return self.decode_output(error)
        return self.decode_output(output)
