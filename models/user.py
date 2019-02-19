class User:
    def __init__(self, name,  email_address, profile, password=None, id=0):
        self.id = id
        self.name = name
        self.email_address = email_address
        self.password = password
        self.profile = profile