#!/bin/env python
from core import Core

def get_translators(username,password,project_slug):
    """Send data and perform Core()"""

    return Core(username,password,project_slug).get()
