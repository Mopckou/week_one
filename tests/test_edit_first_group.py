from model.group import Group
def test_group_add(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="name", header="header", footer="footer"))
    app.session.logout()