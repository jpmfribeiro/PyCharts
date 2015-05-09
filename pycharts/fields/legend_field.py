
class LegendField(object):

    def __init__(self):
        self.reversed = False

    def set_reversed(self, rev):
        self.reversed = rev

    def to_javascript(self):
        jsc = "legend: {"
        if self.reversed:
            jsc += "reversed: true"
        else:
            jsc += "reversed: false"
        jsc += "}"