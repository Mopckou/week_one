from model.group import Group
def test_group_add(app):
    app.group.edit_first_group(Group(name="name", header="header", footer="footer"))
