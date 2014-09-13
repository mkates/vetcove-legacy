from django.test import TestCase
from .misc import *

class convertIntegerDollarsToFloatDollarsTests(TestCase):

	'Tests the function convertIntegerDollarsToFloatDollars'

    def test_noInput(self):
        """A None value for a dollar amount"""
        self.assertEqual('$0.00', convertIntegerDollarsToFloatDollars(None))

    def test_zeroDollars(self):
        """A dollar amount with 0 dollars"""
        self.assertEqual('$0.00', convertIntegerDollarsToFloatDollars(0))

    def test_standardDollars(self):
        """A standard value for a dollar amount"""
        self.assertEqual('$123.45', convertIntegerDollarsToFloatDollars(12345))

    def test_commaDollars(self):
        """A dollar amount with multiple commas"""
        self.assertEqual('$1,234,567.89', convertIntegerDollarsToFloatDollars(123456789))

    def test_cents(self):
        """A dollar amount with only cents"""
        self.assertEqual('$0.68', convertIntegerDollarsToFloatDollars(68))