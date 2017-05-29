#!/bin/env python
from core import Core
from getpass import getpass

def get_translators(username,password,project_slug):
    """Send data and perform Core()"""

    return Core(username,password,project_slug).get()


username = input('Transifex username: ')
password = getpass('Transifex password: ')
project_slug = input('Transifex project_slug: ')

get_translators(username,password,project_slug)
