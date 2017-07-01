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

from os import makedirs, path
from shutil import rmtree

from helpers import (convert_JSON_to_dict, read_file, save_dict_to_JSON,
                     write_file)
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

    def execute_save_cmd(self, command, destination):
        """Execute and save the result of a command into a defined file.

        :param command: A string, the command to execute in shell format
        :param destination: A string, the location where we're going to save the result(s)
        """

        result = Process(command).execute()
        destination = self.QUERY_OUTPUT_DESTINATION + destination

        write_file(result, destination)
        return

    def get_translated_languages(self):
        """Get the list of translated languages in the project."""

        cmd = self.COMMAND_BASE + self.URL_DETAILS
        destination = 'details.json'

        self.execute_save_cmd(cmd, destination)

        content = read_file(self.QUERY_OUTPUT_DESTINATION + destination)
        if content != "Authorization Required":
            self.languages = convert_JSON_to_dict(content)['teams']
            return True
        return False

    def get_list_translators(self):
        """Get the list of translators of the project."""

        if self.languages != []:
            for language in self.languages:
                cmd = self.COMMAND_BASE + self.URL_LANGUAGE + language

                self.execute_save_cmd(cmd, language + '.json')

                content = read_file(
                    self.QUERY_OUTPUT_DESTINATION + language + '.json')

                translators_dict = convert_JSON_to_dict(content)
                self.translators.extend(translators_dict['translators'])
                print('List of %s translators obtained' % language)

            translators_formated_list = sorted(
                list(set(self.translators)), key=str.lower)
            result = {'translators': translators_formated_list}
            save_dict_to_JSON(result, self.OUTPUT_DESTINATION)

            return True
        return False

    def get(self):
        """Get language, then get the list of translators.
        In between, we return an error in case we can't get information from transifex
        """

        if not path.exists(self.QUERY_OUTPUT_DESTINATION):
            makedirs(self.QUERY_OUTPUT_DESTINATION)

        if self.get_translated_languages():
            if self.get_list_translators():
                rmtree(self.QUERY_OUTPUT_DESTINATION)
                print('You can find your list of translators into %s =)' %
                      path.abspath(self.OUTPUT_DESTINATION))
                exit()
        rmtree(self.QUERY_OUTPUT_DESTINATION)
        print('Authorization Required or Wrong project slug')
        exit()
