# Fasternix Stratalorn -  Python module/library for saving the list of translators of a given Transifex project into a JSON file.
# Copyright (C) 2017 Nissar Chababy <contact at funilrys dot com>
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

from .helpers import (clear_screen, convert_JSON_to_dict, execute_return_cmd,
                      execute_save_cmd, format_list, read_file,
                      save_dict_to_JSON, write_file)
from .process import Process


class Core(object):
    """
    Get the list of translators from a Transifex project.

    :param username: A string, A Transifex username. (Must be a maintainer of the project)
    :param password: A string, the password.
    :param project_slug: A string, A Transifex project_slug.
    :param return_dict: A bool, True = return a dict.
    :param return_list: A bool, True = return a list.
    :param save_in_file: A bool, True = save in file.
    """

    def __init__(self, username, password, project_slug, **args):
        self.username = username
        self.password = password
        self.project_slug = project_slug

        self.BASE_URL = 'http://www.transifex.com/api/2/project/' + self.project_slug
        self.ID = self.username + ':' + self.password

        self.OUTPUT_DESTINATION = './translators.json'
        self.QUERY_OUTPUT_DESTINATION = './query_results/'

        self.URL_DETAILS = self.BASE_URL + '/?details'
        self.URL_LANGUAGE = self.BASE_URL + '/language/'

        self.COMMAND_BASE = "curl -L --user " + self.ID + " -X GET "

        optional_arguments = {
            "return_dict": False,
            "return_list": False,
            "save_in_file": True,
        }

        for (arg, default) in optional_arguments.items():
            setattr(self, arg, args.get(arg, default))

        self.languages = []
        self.translators = []

    def get_translated_languages(self):
        """
        Get the list of translated languages in the project.
        """

        cmd = self.COMMAND_BASE + self.URL_DETAILS
        destination = self.QUERY_OUTPUT_DESTINATION + 'details.json'

        execute_save_cmd(cmd, destination)

        content = read_file(destination)

        if content != "Authorization Required" and content != "Not Found":
            self.languages = convert_JSON_to_dict(content)['teams']
            return True
        return content

    def format_result(self):
        """
        Return a formated list or a formated dict.
        """

        translators_formated_list = format_list(self.translators)
        formated_dict = {'translators': translators_formated_list}

        if self.return_list and self.return_dict or self.return_dict:
            self.result = formated_dict
        elif self.return_list:
            self.result = translators_formated_list
        else:
            self.result = formated_dict

    def save_dict(self):
        """
        Save result into a file.
        """

        if self.save_in_file and isinstance(self.result, dict):
            save_dict_to_JSON(self.result, self.OUTPUT_DESTINATION)
            return True
        return False

    def get_list_translators(self):
        """
        Get the list of translators of the project.
        """

        if self.languages != []:
            if self.return_list == False and self.return_dict == False:
                if(version_info[0] >= 3):
                    done = '✔'
                else:
                    done = '✔'.decode('utf-8')

            for language in self.languages:
                cmd = self.COMMAND_BASE + self.URL_LANGUAGE + language

                transifex_lang_output = convert_JSON_to_dict(
                    execute_return_cmd(cmd))

                self.translators.extend(transifex_lang_output['translators'])

                if self.return_list == False and self.return_dict == False:
                    print('\033[1m\033[96m%s\033[0m translators %s' %
                          (language, done))

            self.format_result()
            self.save_dict()

            return True
        return False

    def get(self):
        """
        Get language, then get the list of translators.
        In between, we return an error in case we can't get information from transifex.
        """

        if not path.exists(self.QUERY_OUTPUT_DESTINATION):
            makedirs(self.QUERY_OUTPUT_DESTINATION)

        funilrys = self.get_translated_languages()
        if funilrys:
            if self.get_list_translators():
                rmtree(self.QUERY_OUTPUT_DESTINATION)
                clear_screen()
                if self.save_dict() and self.return_list == False and self.return_dict == False:
                    print(
                        'You can find your list of translators into \033[1m\033[93m%s \033[96m=)\033[0m' %
                        path.abspath(
                            self.OUTPUT_DESTINATION))
                    exit()
                return self.result

        rmtree(self.QUERY_OUTPUT_DESTINATION)

        print(funilrys)
        exit()
