from model.contact import Contact
def test_add_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstName='test'))
    app.contact.edit_first_contact(Contact(firstName="firstName", middleName="middleName", lastName="lastName", nickName="nickName", title="title",
                               company="company", address="address", home="home", mobile="mobile", work="work", fax="fax", email="email",
                               email2="email2", email3="email3", homepage="homepage", address2="address2", phone2="phone2", notes="notes"))
