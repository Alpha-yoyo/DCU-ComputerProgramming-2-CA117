#!/usr/bin/env python

class ContactList(object):
    def __init__(self):
        self.d = {}

    def add_contact(self, contact):
        self.d[contact.name] = contact

    def del_contact(self, name):
        if name in self.d:
            del self.d[name]

    def get_contact(self, name):
        if name in self.d:
            return self.d[name]
        else:
            return 'None'

    def __str__(self):
        return "\n".join(['Contact list', '------------'] + [str(self.d[v]) for v in sorted(self.d)])

class Contact(object):
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return '{} {} {}'.format(self.name, self.phone, self.email)
