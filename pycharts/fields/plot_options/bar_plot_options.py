
class BarPlotOptions(object):

    def __init__(self, stacking=None):
        self.stacking = stacking

    def to_javascript(self):
        jsc = "bar: {"
        if self.stacking is not None:
            jsc += "stacking: '" + str(self.stacking) + "'"
        jsc += "}"

        return jsc
