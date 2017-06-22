# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app,db,check_ui,json_contact):
    contact = json_contact
    old_contact = db.get_contact_list()
    app.contact.create(contact)
    new_contact = db.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_map) == sorted(new_contact, key=Contact.id_or_map)
    if check_ui:
        assert sorted(new_contact, key=Contact.id_or_map) == sorted(app.contact.get_contact_list(), key=Contact.id_or_map)