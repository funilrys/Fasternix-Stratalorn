#!/bin/env python
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
