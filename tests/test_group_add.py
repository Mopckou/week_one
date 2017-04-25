# -*- coding: utf-8 -*-

from model.group import Group


def test_group_add(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="3", header="33", footer="333"))
    app.session.logout()

def test_group_empty_add(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
