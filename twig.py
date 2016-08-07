#!/bin/python3

from util import *

def create(name):
    twig_path = '/opt/symfony-code-generator/template/twig.template'
    view_path = 'app/Resources/views/%s/index.html.twig' % name

    content = readFile(twig_path)
    createDirs(view_path)
    createFile(view_path, content);
