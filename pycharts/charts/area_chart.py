from ..fields.chart_field import ChartField
from ..fields.title_field import TitleField
from ..fields.series_field import SeriesField
from ..fields.legend_field import LegendField
from ..fields.axis_field import AxisField
from ..fields.series.series import Series
from ..fields.plot_options_field import PlotOptionsField
from ..fields.plot_options.area_plot_options import AreaPlotOptions
from highchart import HighChart

class AreaChart(HighChart):

    def __init__(self, title, data, stacking=None, x_title=None, y_title=None):
        self.chart_field = ChartField()
        self.chart_field.set_type('area')

        self.title_field = TitleField(text=title)

        self.series_field = SeriesField()
        for (n, d) in data:
            self.series_field.add_serie(Series(name=n, data=d))

        self.x_axis_field = AxisField(is_x_axis=True)
        if x_title is not None:
            self.x_axis_field.set_title(x_title)
        self.y_axis_field = AxisField(is_x_axis=False)
        if y_title is not None:
            self.y_axis_field.set_title(y_title)

        self.plot_options_field = PlotOptionsField()
        if stacking is not None:
            self.plot_options_field.add_plot_option(AreaPlotOptions(stacking=stacking))

    def to_javascript(self):
        jsc = "{"
        jsc += self.chart_field.to_javascript() + ", "
        jsc += self.title_field.to_javascript() + ", "
        jsc += self.x_axis_field.to_javascript() + ", "
        jsc += self.y_axis_field.to_javascript() + ", "
        jsc += self.plot_options_field.to_javascript() + ", "
        jsc += self.series_field.to_javascript()
        jsc += "}"

        return jsc

