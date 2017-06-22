# -*- coding: utf-8 -*-

from model.group import Group

def test_group_add(app,db,check_ui,json_group):
     group = json_group
     old_groups = db.get_group_list()
     app.group.create(group)
     new_groups = db.get_group_list()
     old_groups.append(group)
     assert sorted(old_groups, key=Group.id_or_map) == sorted(new_groups, key=Group.id_or_map)
     if check_ui:
          assert sorted(new_groups, key=Group.id_or_map) == sorted(app.group.get_group_list(), key=Group.id_or_map)