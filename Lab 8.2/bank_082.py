#!/usr/bin/env python3

class BankAccount(object):
    next_account_number = 16555232
    total_lodgements = 0
    interest_rate = 0.043

    def __init__(self, forename, surname, balance=0, account_number=next_account_number):
        self.forename = forename
        self.surname = surname
        self.balance = balance
        self.account_number = BankAccount.next_account_number
        BankAccount.next_account_number += 1

    def lodge(self, other):
        self.balance += other
        BankAccount.total_lodgements += 1

    def apply_interest(self):
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        BankAccount.total_lodgements += 1

    def __iadd__(self, other):
        self.balance += other
        return self

    def __str__(self):
        return 'Name: {:s} {:s}\nAccount number: {:d}\nBalance: {:.2f}'.format(self.forename, self.surname, self.account_number, self.balance)
