from model.group import Group
from random import randrange

def test_group_add(app,db,check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="name", header="header", footer="footer")
    group.id = old_groups[index].id
    app.group.edit_group_by_id(group.id,group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_map) == sorted(new_groups, key=Group.id_or_map)
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_map) == sorted(app.group.get_group_list(), key=Group.id_or_map)
