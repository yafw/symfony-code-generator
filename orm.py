#!/bin/python3

from util import *

def create(name):
    template_path = '/opt/symfony-code-generator/template/orm.template'

    table_name = '%ss' % name

    class_name = firstToUpper(name)
    class_path = 'src/AppBundle/Entity/%s.php' % class_name

    content = readFile(template_path)
    content = content.replace('<CLASS>', class_name)
    content = content.replace('<TABLE>', table_name)
    createFile(class_path, content);
