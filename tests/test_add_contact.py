# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstName="5", middleName="2", lastName="3", nickName="4", title="5",
                               company="6", address="7", home="8", mobile="9", work="10", fax="11", email="12",
                               email2="13", email3="14", homepage="15",
                               birthDay="2", birthMonth="2", birthYear="1992", anniversaryDay="12", anniversaryMonth="10",
                               anniversaryYear="2222", group="3", address2="16", phone2="17", notes="18"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstName="", middleName="", lastName="", nickName="", title="",
                               company="", address="", home="", mobile="", work="", fax="", email="",
                               email2="", email3="", homepage="",
                               birthDay="1", birthMonth="1", birthYear="", anniversaryDay="1", anniversaryMonth="1",
                               anniversaryYear="", group="1", address2="", phone2="", notes=""))
    app.session.logout()