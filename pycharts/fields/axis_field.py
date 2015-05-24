from title_field import TitleField

class AxisField(object):

    def __init__(self, is_x_axis=True):
        self.is_x_axis = is_x_axis
        self.title_field = TitleField()
        self.categories = []
        self.type = None

    def set_title(self, text):
        self.title_field.set_text(text)

    def set_categories(self, cat):
        self.categories = cat

    def set_type(self, t):
        self.type = t

    def to_javascript(self):
        jsc = ""
        if self.is_x_axis:
            jsc += "xAxis: {"
        else:
            jsc += "yAxis: {"

        if self.categories:
            jsc += "categories: " + str(self.categories) + ", "

        if self.type:
            jsc += "type: '" + self.type + "', "

        jsc += self.title_field.to_javascript()
        jsc += "}"

        return jsc
