

class SeriesField(object):

    def __init__(self):
        self.series = []

    def add_serie(self, serie):
        self.series.append(serie)

    def to_javascript(self):
        jsc = "series: ["
        for s in self.series:
            jsc += s.to_javascript() + ","    # the last comma is accepted by javascript, no need to ignore
        jsc += "]"
        return jsc

