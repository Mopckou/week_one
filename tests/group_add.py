# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_group_add(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="3", header="33", footer="333"))
    app.session.logout()

def test_group_empty_add(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
