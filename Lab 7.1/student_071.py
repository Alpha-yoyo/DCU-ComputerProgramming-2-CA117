#!/usr/bin/env python3

class Student(object):

    def __init__(self, surname, forename, id, modlist=[]):
        self.surname = surname
        self.forename = forename
        self.id = id
        self.modlist = modlist

    def add_module(self, module):
        self.modlist.append(module)
        self.module = ' '.join(self.modlist)

    def del_module(self, module):
        if module not in self.modlist:
            self.modlist.append(module)
        self.modlist.remove(module)
        self.module = ' '.join(self.modlist)

    def print_details(self):
        print('ID: {:d}'.format(self.id))
        print('Surname: {:s}'.format(self.surname))
        print('Forename: {:s}'.format(self.forename))
        print('Modules: {}'.format(self.module))
