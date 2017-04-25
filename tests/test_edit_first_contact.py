from model.contact import Contact
def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstName="firstName", middleName="middleName", lastName="lastName", nickName="nickName", title="title",
                               company="company", address="address", home="home", mobile="mobile", work="work", fax="fax", email="email",
                               email2="email2", email3="email3", homepage="homepage",
                               birthDay="2", birthMonth="2", birthYear="1992", anniversaryDay="12", anniversaryMonth="10",
                               anniversaryYear="2222", address2="address2", phone2="phone2", notes="notes"))
    app.session.logout()