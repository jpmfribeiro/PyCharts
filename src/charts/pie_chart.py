from ..fields.chart_field import ChartField
from ..fields.title_field import TitleField

class PieChart(object):

    def __init__(self, title, data):
        self.title_field = TitleField(text=title)
        self.data = data # TODO represent as series field

        self.chart_field = ChartField()
        self.chart_field.set_type('pie')

    def to_javascript(self):
        # TODO

