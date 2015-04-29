from ..fields.chart_field import ChartField
from ..fields.title_field import TitleField
from ..fields.series_field import SeriesField
from ..fields.series.series import Series
from ..fields.plot_options_field import PlotOptionsField
from ..fields.plot_options.pie_plot_options import PiePlotOptions

class PieChart(object):

    def __init__(self, title, data_label, data):
        '''

        :param title:       e.g. 'Browser market shares at a specific website, 2014'
        :param data_label:  e.g. 'Browser shares'
        :param data:        e.g. [ ['Firefox', 45.0], ['IE', 26.8], ['Chrome', 12.8], ... ]

        '''

        self.title_field = TitleField(text=title)

        self.series_field = SeriesField()
        self.series_field.add_serie(Series(data_label, data))

        self.plot_options_field = PlotOptionsField()
        self.plot_options_field.add_plot_option(PiePlotOptions())

        self.chart_field = ChartField()
        self.chart_field.set_type('pie')

    def to_javascript(self):
        jsc = "{"
        jsc += self.chart_field.to_javascript() + ", "
        jsc += self.title_field.to_javascript() + ", "
        jsc += self.plot_options_field.to_javascript() + ", "
        jsc += self.series_field.to_javascript()
        jsc += "}"

        return jsc

