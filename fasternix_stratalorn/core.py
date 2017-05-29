#!/bin/env python
from helpers import write_file
from process import Process

class Core(object):
    """Brain of the program. Get the list of translators from a Transifex project"""

    def __init__(self, username, password, project_slug):
        self.username = username
        self.password = password
        self.project_slug = project_slug

        self.BASE_URL = 'http://www.transifex.com/api/2/project/' + self.project_slug
        self.ID = self.username + ':' + self.password
        self.OUTPUT_DESTINATION = './translators.json'
        self.QUERY_OUTPUT_DESTINATION = './query_results/'

        self.URL_DETAILS = self.BASE_URL + '/?details'
        self.URL_LANGUAGE = self.BASE_URL + '/language/'

        self.COMMAND_BASE = 'curl -L --user ' + self.ID + ' -X GET '

        self.languages = []
        self.translators = []

    def execute_save_cmd(self,command, destination):
        """Execute and save the result of a command into a defined file.

        :param command: A string, the command to execute in shell format
        :param destination: A string, the location where we're going to save the result(s)
        """

        result = Process(command).execute()
        destination = self.OUTPUT_DESTINATION + destination

        write_file(result,destination)
        return 
