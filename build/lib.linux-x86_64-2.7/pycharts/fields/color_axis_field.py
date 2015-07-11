
class ColorAxisField(object):

    def __init__(self, min=0):
        self.min = min

    def set_min(self, min):
        self.min = min

    def to_javascript(self):
        jsc = "colorAxis: { min: " + str(self.min) + " }"
        return jsc