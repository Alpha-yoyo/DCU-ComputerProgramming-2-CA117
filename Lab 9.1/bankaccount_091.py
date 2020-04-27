#!/usr/bin/env python3

class BankAccount(object):
    next_account_number = 16555232
    account_type = 'General'

    def __init__(self, forename, surname, balance, account_number=next_account_number):
        self.forename = forename
        self.surname = surname
        self.balance = balance
        self.account_number = BankAccount.next_account_number
        BankAccount.next_account_number += 1

    def lodge(self, other):
        self.balance += other

    def withdraw(self, other):
        if self.balance - other >= 0:
            self.balance -= other
        else:
            print('Insufficient funds available')

    def __str__(self):
        return 'Name: {} {}\nAccount number: {}\nAccount type: {}\nBalance: {:.2f}'.format(self.forename, self.surname, self.account_number, self.account_type, self.balance)

class CurrentAccount(BankAccount):
    overdraft = -1000
    account_type = 'Current'

    def withdraw(self, other):
        if other <= self.balance + 1000:
            self.balance -= other
        else:
            print('Insufficient funds available')

    def __str__(self):
        return 'Name: {} {}\nAccount number: {}\nAccount type: {}\nBalance: {:.2f}\nOverdraft: {:.2f}'.format(self.forename, self.surname, self.account_number, self.account_type, self.balance, self.overdraft)

class SavingsAccount(BankAccount):
    interest_rate = 0.01
    account_type = 'Savings'

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate

    def __str__(self):
        return 'Name: {} {}\nAccount number: {}\nAccount type: {}\nBalance: {:.2f}\nInterest rate: {}'.format(self.forename, self.surname, self.account_number, self.account_type, self.balance, self.interest_rate)
