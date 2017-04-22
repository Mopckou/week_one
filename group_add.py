# -*- coding: utf-8 -*-
from group import Group
from Application import Application
import pytest

@pytest.fixture
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_group_add(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="3", header="33", footer="333"))
    app.logout()

def test_group_empty_add(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
