from unittest import TestCase
from main import Users

DATA = {'Name': 'Zara', 'ID': '6', 'ZipCode': '12345','State':'NY','Birthday': '01/01/2000', 'Email':'xyz@gmail.com'}


class TestUser(TestCase):
    #check age
    def test_should_return_true_for_age_greater_than_21(self):
        DATA["Birthday"]='01/01/2000'
        new_user=Users(DATA)
        result = new_user.check_age()
        self.assertTrue(result)

    def test_should_return_false_for_age_less_than_21(self):
        DATA["Birthday"]='01/06/2004'
        new_user=Users(DATA)
        result = new_user.check_age()
        self.assertFalse(result)

    #check for first Monday of the month
    def test_should_return_false_if_birthdate_is_first_Monday_of_the_month(self):
        DATA["Birthday"]='02/06/2023'
        new_user=Users(DATA)
        result = new_user.check_weekday()
        self.assertFalse(result)

    def test_should_return_true_if_birthdate_is_not_first_Monday_of_the_month(self):
        DATA["Birthday"]='03/04/1998'
        new_user=Users(DATA)
        result = new_user.check_weekday()
        self.assertTrue(result)
    
    #check zipcode
    def test_should_return_true_for_zipcode_with_no_consecutive_numbers(self):
        DATA["ZipCode"]='24796'
        new_user=Users(DATA)
        result = new_user.check_zipcode()
        self.assertTrue(result)
    
    def test_should_return_false_for_zipcode_with_consecutive_numbers(self):
        DATA["ZipCode"]='11347'
        new_user=Users(DATA)
        result = new_user.check_zipcode()
        self.assertFalse(result)

    def test_should_return_false_for_zipcode_with_reverse_consecutive_numbers(self):
        DATA["ZipCode"]='11437'
        new_user=Users(DATA)
        result = new_user.check_zipcode()
        self.assertFalse(result)

    #check state
    def test_should_return_true_for_state_if_not_prohibited(self):
        DATA["State"]='NY'
        new_user=Users(DATA)
        result = new_user.check_state()
        self.assertTrue(result)

    def test_should_return_false_for_state_if_prohibited(self):
        DATA["State"]='CT'
        new_user=Users(DATA)
        result = new_user.check_state()
        self.assertFalse(result)

    #check email
    def test_should_return_true_for_valid_email(self):
        DATA["Email"]='oqibz@abc.com'
        new_user=Users(DATA)
        result = new_user.check_email()
        self.assertTrue(result)

    def test_should_return_false_for_email_with_no_at(self):
        DATA["Email"]='xyzgmail.com'
        new_user=Users(DATA)
        result = new_user.check_email()
        self.assertFalse(result)

    def test_should_return_false_for_email_with_no_dot_in_domain(self):
        DATA["Email"]='x.yz@coin'
        new_user=Users(DATA)
        result = new_user.check_email()
        self.assertFalse(result)

    def test_should_return_false_for_email_with_no_domain(self):
        DATA["Email"]='xyz@.'
        new_user=Users(DATA)
        result = new_user.check_email()
        self.assertFalse(result)

    def test_should_return_false_for_email_with_no_username(self):
        DATA["Email"]='@gmail.com'
        new_user=Users(DATA)
        result = new_user.check_email()
        self.assertFalse(result)
