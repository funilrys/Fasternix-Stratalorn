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

from getpass import getpass

from .core import Core
from .helpers import clear_screen


def get(username, project_slug, **args):
    """
    Get the list of translators from a Transifex project.

    :param username: A string, A Transifex username. (Must be a maintainer of the project)
    :param project_slug: A string, A Transifex project_slug.
    :param return_dict: A bool, True = return a dict.
    :param return_list: A bool, True = return a list.
    :param save_in_file: A bool, True = save in file.
    """

    password = getpass('Transifex password: ')
    clear_screen()

    return Core(username, password, project_slug, **args).get()
