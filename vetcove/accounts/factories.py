from __future__ import absolute_import

import factory

from .models import *


class BasicUserFactory(factory.DjangoModelFactory):
    '''
    Generates a BasicUser with unique username and password:test
    '''
    class Meta:
        model = BasicUser

    username = factory.Sequence(lambda n: 'user_%d@test.com' % n)
    password = 'test'

    @factory.lazy_attribute
    def email(self):
        ''' Set the email equal to the username'''
        return self.username


class AddressFactory(factory.DjangoModelFactory):
    '''
    Generates an address factory
    '''
    class Meta:
        model = Address

    name = factory.Sequence(lambda n: 'address_name_%d' % n)
    address_one = '1 Main Street'
    city = 'Colts Neck'
    state = 'NJ'
    country = 'usa'
    postalcode = '07722'


class GroupFactory(factory.DjangoModelFactory):
    '''
    Generates a Group object
    '''
    class Meta:
        model = Group

    name = 'joe'
    slug = 'colts-neck-equine'
    administrator = factory.SubFactory(BasicUserFactory)
    contact_name = "contact_name"
    contact_position = "contact_position"
    address = factory.SubFactory(AddressFactory)
    referral_id = factory.Sequence(lambda n: 'referral_%d' % n)
    group_type = 'clinic'
