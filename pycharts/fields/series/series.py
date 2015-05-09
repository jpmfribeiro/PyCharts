

class Series(object):

    def __init__(self, name, data):
        self.name = name
        self.data = data

    def to_javascript(self):
        jsc = "{"
        jsc += "name: '" + self.name + "',"
        jsc += "data: " + str(self.data) + "}"
        return jsc