# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string
def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstName="", lastName="", address="", home="", email="")] +[
            Contact(firstName=random_string("firstname", 10), lastName=random_string("lastname", 10),
                    address=random_string("address", 20), home=random_string("homephone", 9), email=random_string("email", 8) ,)
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contact = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contact) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_map) == sorted(new_contact, key=Contact.id_or_map)
