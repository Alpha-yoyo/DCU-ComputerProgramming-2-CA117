#!/usr/bin/env python3

class Employee(object):
    next_employee_number = 0

    def __init__(self, name, employee_number=next_employee_number, hourly_rate=9.25, hours_worked=0):
        self.name = name
        self.employee_number = Employee.next_employee_number
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        Employee.next_employee_number += 1

    def add_hours(self, other):
        self.hours_worked += other

    def __str__(self):
        wages = self.hourly_rate * self.hours_worked
        return 'Name: {:s}\nID: {:d}\nHours: {:.2f}\nRate: {:.2f}\nWages: {:.2f}'.format(self.name, self.employee_number, self.hours_worked, self.hourly_rate, wages)
