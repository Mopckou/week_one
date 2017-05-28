import time
from model.contact import Contact
class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()


    def return_to_contact_list(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()


    def create(self, contact):
        wd = self.app.wd
        self.open_new_contact()
        self.fill_field_value(contact)
        wd.find_element_by_name("submit").click()
        self.return_to_contact_list()
        self.contact_cashe = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value=\"Delete\"]").click()
        wd.switch_to_alert().accept()
        self.open_contact_page()
        self.contact_cashe = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//img[@src=\"icons/pencil.png\"]").click()
        self.fill_field_value(contact)
        wd.find_element_by_name("update").click()
        self.return_to_contact_list()
        self.contact_cashe = None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(0, contact)

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('/') and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    def fill_field_value(self, contact):
        self.change_field("firstname", contact.firstName)
        self.change_field("middlename", contact.middleName)
        self.change_field("lastname", contact.lastName)
        self.change_field("nickname", contact.nickName)
        self.change_field("title", contact.title)
        self.change_field("company", contact.company)
        self.change_field("address", contact.address)
        self.change_field("home", contact.home)
        self.change_field("mobile", contact.mobile)
        self.change_field("work", contact.work)
        self.change_field("fax", contact.fax)
        self.change_field("email", contact.email)
        self.change_field("email2", contact.email2)
        self.change_field("email3", contact.email3)
        self.change_field("homepage", contact.homepage)
        self.change_field("address2", contact.address2)
        self.change_field("phone2", contact.phone2)
        self.change_field("notes", contact.notes)

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cashe = None

    def get_contact_list(self):
        if self.contact_cashe is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cashe = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_elements_by_name("selected[]")[0].get_attribute("value")
                e = element.find_elements_by_css_selector("td")
                firstName= e[2].text
                lastName= e[1].text
                self.contact_cashe.append(Contact(firstName= firstName, lastName= lastName, id=id))
        return list(self.contact_cashe)