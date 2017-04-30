# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstName="5", middleName="2", lastName="3", nickName="4", title="5",
                               company="6", address="7", home="8", mobile="9", work="10", fax="11", email="12",
                               email2="13", email3="14", homepage="15", address2="16", phone2="17", notes="18"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstName="", middleName="", lastName="", nickName="", title="",
                               company="", address="", home="", mobile="", work="", fax="", email="",
                               email2="", email3="", homepage="", address2="", phone2="", notes=""))
