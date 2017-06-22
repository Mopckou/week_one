from model.group import Group

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # int group create
        wd.find_element_by_name("new").click()
        # fill group firm
        self.fill_field_value(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()
        self.group_cashe = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        #delete first group
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cashe = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_id(id)
        #delete first group
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cashe = None

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_group_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self,id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def edit_first_group(self, group):
        self.edit_group_by_index(0, group)

    def edit_group_by_index(self, index, group):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        #edit first group
        wd.find_element_by_name("edit").click()
        #edit
        self.fill_field_value(group)
        #select update
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cashe = None

    def edit_group_by_id(self, id, group):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_id(id)
        #edit first group
        wd.find_element_by_name("edit").click()
        #edit
        self.fill_field_value(group)
        #select update
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cashe = None

    def fill_field_value(self, group):
        wd = self.app.wd
        self.change_field("group_name", group.name)
        self.change_field("group_header", group.header)
        self.change_field("group_footer", group.footer)

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('/group.php') and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cashe = None

    def get_group_list(self):
        if self.group_cashe is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cashe = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cashe.append(Group(name=text, id=id))
        return list(self.group_cashe)