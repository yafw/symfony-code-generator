#!/bin/python3

from util import *

def create(name):
    controller_path = '/opt/symfony-code-generator/template/controller.template'

    route_name = name

    class_name = "%sController" % firstToUpper(name)
    class_path = 'src/AppBundle/Controller/%s.php' % class_name

    view_name = '\'%s/index.html.twig\'' % name

    content = readFile(controller_path)
    content = content.replace('<CLASS>', class_name)
    content = content.replace('<ROUTE>', route_name)
    content = content.replace('<VIEW>' , view_name )
    createFile(class_path, content);
