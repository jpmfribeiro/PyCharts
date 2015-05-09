from title_field import TitleField

class AxisField(object):

    def __init__(self, is_x_axis=True):
        self.is_x_axis = is_x_axis
        self.title_field = TitleField()
        self.categories = []

    def set_title(self, text):
        self.title_field.set_text(text)

    def set_categories(self, cat):
        self.categories = cat

    def to_javascript(self):
        jsc = ""
        if self.is_x_axis:
            jsc += "xAxis: {"
        else:
            jsc += "yAxis: {"

        if self.categories:
            jsc += "categories: " + str(self.categories) + ", "

        jsc += self.title_field.to_javascript()
        jsc += "}"

        return jsc
