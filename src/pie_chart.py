
# TODO: Import highcharts_fields/chart_field

class PieChart(object):

    def __init__(self, title, data):
        self.title = title
        self.data = data

        self.chart_field = None

    def to_javascript(self):
        # TODO

