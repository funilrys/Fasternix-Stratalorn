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
from sys import version_info

from .helpers import (clear_screen, convert_JSON_to_dict, execute_save_cmd,
                      format_list, read_file, save_dict_to_JSON, write_file)
from .process import Process


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

    def get_translated_languages(self):
        """Get the list of translated languages in the project."""

        cmd = self.COMMAND_BASE + self.URL_DETAILS
        destination = self.QUERY_OUTPUT_DESTINATION + 'details.json'

        execute_save_cmd(cmd, destination)

        content = read_file(destination)

        if content != "Authorization Required" and content != "Not Found":
            self.languages = convert_JSON_to_dict(content)['teams']
            return True
        return content

    def get_list_translators(self):
        """Get the list of translators of the project."""

        if self.languages != []:
            if(version_info[0] >= 3):
                done = '✔'
            else:
                done = '✔'.decode('utf-8')

            for language in self.languages:
                cmd = self.COMMAND_BASE + self.URL_LANGUAGE + language

                execute_save_cmd(
                    cmd, self.QUERY_OUTPUT_DESTINATION + language + '.json')

                content = read_file(
                    self.QUERY_OUTPUT_DESTINATION + language + '.json')

                translators_dict = convert_JSON_to_dict(content)
                self.translators.extend(translators_dict['translators'])

                print('\033[1m\033[96m%s\033[0m translators %s' %
                      (language, done))

            translators_formated_list = format_list(self.translators)
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

        funilrys = self.get_translated_languages()
        if funilrys:
            if self.get_list_translators():
                rmtree(self.QUERY_OUTPUT_DESTINATION)
                clear_screen()
                print('You can find your list of translators into \033[1m\033[93m%s \033[96m=)\033[0m' %
                      path.abspath(self.OUTPUT_DESTINATION))
                exit()

        rmtree(self.QUERY_OUTPUT_DESTINATION)

        print(funilrys)
        exit()
