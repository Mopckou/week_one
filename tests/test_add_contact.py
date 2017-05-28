# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contact = app.contact.get_contact_list()
    contact = Contact(firstName="5", middleName="2", lastName="3", nickName="4", title="5",
                               company="6", address="7", home="8", mobile="9", work="10", fax="11", email="12",
                               email2="13", email3="14", homepage="15", address2="16", phone2="17", notes="18")
    app.contact.create(contact)
    assert len(old_contact) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_map) == sorted(new_contact, key=Contact.id_or_map)


# def test_add_empty_contact(app):
#     old_contact = app.contact.get_contact_list()
#     contact = Contact(firstName="", middleName="", lastName="", nickName="", title="",
#                                company="", address="", home="", mobile="", work="", fax="", email="",
#                                email2="", email3="", homepage="", address2="", phone2="", notes="")
#     app.contact.create(contact)
#     new_contact = app.contact.get_contact_list()
#     assert len(old_contact) + 1 == len(new_contact)
#     old_contact.append(contact)
#     assert sorted(old_contact, key=Contact.id_or_map) == sorted(new_contact, key=Contact.id_or_map)