from ..fields.chart_field import ChartField
from ..fields.title_field import TitleField
from ..fields.axis_field import AxisField
from ..fields.series_field import SeriesField
from ..fields.series.series import Series
from highchart import HighChart

class ScatterChart(HighChart):

    def __init__(self, title, data, x_title=None, y_title=None):
        '''

        :param title:
        :param data:    The data is represented in the following form:
                        [ ('First Series', [[x1, y1], [x2, y2], ..., [xn, yn]]),
                          ('Second Series', [[x1, y1], [x2, y2], ..., [xn, yn]]),
                          ... ]
                         where x, y represent the numerical values for the x axis and y axis respectively.
        '''
        self.chart_field = ChartField()
        self.chart_field.set_type('scatter')

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


    def to_javascript(self):
        jsc = "{"
        jsc += self.chart_field.to_javascript() + ", "
        jsc += self.title_field.to_javascript() + ", "
        jsc += self.x_axis_field.to_javascript() + ", "
        jsc += self.y_axis_field.to_javascript() + ", "
        jsc += self.series_field.to_javascript()
        jsc += "}"

        return jsc
