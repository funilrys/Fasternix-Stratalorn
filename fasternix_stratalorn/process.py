#!/bin/env python

class Process(object):
    """A class to manipulate shell commands

    :param command: A string, the command to execute
    """

    def __init__(self, command):
        self.command = command
