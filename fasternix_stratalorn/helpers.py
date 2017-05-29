#!/bin/env python
from json import loads, dump

def write_file(content,destination):
    """Write a content in a given file

    :param content: A string, the content we have to write into the file
    :param destination: A string, A path to a file where we're going to save the content
    """

    with open(destination,'w') as file:
        file.write(content)

def read_file(file_to_read):
    """Read the content of a given file

    :param file_to_read: A string, a path to the file we have to read
    """

    with open(file_to_read,'r') as file:
        funilrys = file.read()
    return funilrys

def convert_JSON_to_dict(data):
    """Convert a JSON into a dictionary

    :param data: A string, a JSON formated string
    """

    return loads(data)

def save_dict_to_JSON(data,destination):
    """Save a dictionary into a JSON format

    :param data: A dict
    :param destination: A string, A path to a file where we're going to write the converted dict into a JSON format
    """

    with open(destination, 'w') as file:
        dump(data, file, ensure_ascii=False, indent=4, sort_keys=True)
