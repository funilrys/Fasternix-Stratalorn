#!/bin/env python

class Core(object):
    """Brain of the program. Get the list of translators from a Transifex project"""

    def __init__(self, username, password, project_slug):
        self.username = username
        self.password = password
        self.project_slug = project_slug

        self.BASE_URL = 'http://www.transifex.com/api/2/project/' + self.project_slug
        self.ID = self.username + ':' + self.password
        self.OUTPUT_DESTINATION = './translators.json'

        self.URL_DETAILS = self.BASE_URL + '/?details'
        self.URL_LANGUAGE = self.BASE_URL + '/language/'

        self.COMMAND_BASE = 'curl -L --user ' + self.ID + ' -X GET '

        self.languages = []
        self.translators = []
