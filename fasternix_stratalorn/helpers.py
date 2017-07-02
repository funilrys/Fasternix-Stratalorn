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

from json import dump, loads
from os import name, system
from sys import version_info

from .process import Process


def write_file(content, destination):
    """Write a content in a given file

    :param content: A string, the content we have to write into the file
    :param destination: A string, A path to a file where we're going to save the content
    """

    with open(destination, 'w') as file:
        file.write(content)


def execute_save_cmd(command, destination):
    """Execute and save the result of a command into a defined file.

    :param command: A string, the command to execute in shell format
    :param destination: A string, the location where we're going to save the result(s)
    """

    result = Process(command).execute()

    write_file(result, destination)
    return


def execute_return_cmd(command):
    """Execute and return the result of a command.

    :param command: A string, the command to execture in shell format
    """

    return Process(command).execute()


def read_file(file_to_read):
    """Read the content of a given file

    :param file_to_read: A string, a path to the file we have to read
    """

    with open(file_to_read, 'r') as file:
        funilrys = file.read()
    return funilrys


def convert_JSON_to_dict(data):
    """Convert a JSON into a dictionary

    :param data: A string, a JSON formated string
    """

    return loads(data)


def format_list(data):
    """Sort and remove duplicate from a given list

    :param data: A list, the list to format
    """
    if(version_info[0] >= 3):
        return sorted(list(set(data)), key=str.lower)
    return sorted(list(set(data)), key=unicode.lower)


def save_dict_to_JSON(data, destination):
    """Save a dictionary into a JSON format

    :param data: A dict
    :param destination: A string, A path to a file where we're going to write the converted dict into a JSON format
    """

    with open(destination, 'w') as file:
        dump(data, file, ensure_ascii=False, indent=4, sort_keys=True)


def clear_screen():
    if name == 'posix' or name == 'mac':
        system('clear')
    elif name == 'nt':
        system("cls")
