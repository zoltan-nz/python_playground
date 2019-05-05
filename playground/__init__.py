import urllib.request
from random import randint


def generate_random():
    return randint(1, 101)


def download_example_com():
    file, header = urllib.request.urlretrieve("https://example.com")
    return file, header
