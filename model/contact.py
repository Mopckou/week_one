from sys import maxsize
class Contact:
    def __init__(self,firstName=None, middleName=None, lastName=None, nickName=None, title=None, company=None,
                 address=None, home=None, mobile=None, work=None, fax=None, email=None, email2=None, email3=None, homepage=None,
                 address2=None, phone2=None, notes=None, id=None):
        self.firstName=firstName
        self.middleName=middleName
        self.lastName=lastName
        self.nickName=nickName
        self.title=title
        self.company=company
        self.address=address
        self.home=home
        self.mobile=mobile
        self.work=work
        self.fax=fax
        self.email=email
        self.email2=email2
        self.email3=email3
        self.homepage=homepage
        self.address2=address2
        self.phone2=phone2
        self.notes=notes
        self.id=id

    def __repr__(self):
        return "%s: %s %s" % (self.id, self.firstName, self.lastName)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstName == other.firstName and self.lastName == other.lastName

    def id_or_map(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize