#!/usr/bin/python3

class BankAccount(object):

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, other):
        self.balance += other

    def withdraw(self, other):
        if other <= self.balance and self.balance > 0:
            self.balance -= other
        else:
            print('Insufficient funds available')

    def __str__(self):
        return 'Your current balance is: {:.2f} euro'.format(self.balance)
