#!/usr/bin/python3

import sys, os
import orm, controller, twig

command = sys.argv[1]
name = sys.argv[2]

if command == 'gen-ctl':
    controller.create(name)

if command == 'gen-orm':
    orm.create(name)

if command == 'gen-tpl':
    twig.create(name)
