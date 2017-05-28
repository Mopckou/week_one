from model.contact import Contact
def test_add_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstName='test'))
    old_contact = app.contact.get_contact_list()
    contact = Contact(firstName="firstName", middleName="middleName", lastName="lastName", nickName="nickName", title="title",
                               company="company", address="address", home="home", mobile="mobile", work="work", fax="fax", email="email",
                               email2="email2", email3="email3", homepage="homepage", address2="address2", phone2="phone2", notes="notes")
    contact.id=old_contact[0].id
    app.contact.edit_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0]= contact
    assert sorted(old_contact, key=Contact.id_or_map) == sorted(new_contact, key=Contact.id_or_map)