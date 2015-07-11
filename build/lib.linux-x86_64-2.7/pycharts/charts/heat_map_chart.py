from ..fields.chart_field import ChartField
from ..fields.title_field import TitleField
from ..fields.axis_field import AxisField
from ..fields.series_field import SeriesField
from ..fields.series.series import Series
from ..fields.color_axis_field import ColorAxisField
from collections import OrderedDict
from highchart import HighChart

class HeatMapChart(HighChart):

    def __init__(self, title, data):
        '''

        :param data:    The data is represented in the following form:
                        [('Series Name', [[x1, y1, z1], [x2, y2, z2], ..., [xn, yn, zn]])]
                        where x, y represent the categorical values for the x axis and y axis respectively
                        and z represents the numerical value.
        '''

        self.chart_field = ChartField()
        self.chart_field.set_type('heatmap')

        self.title_field = TitleField(text=title)

        min_value = min(min([z for [x, y, z] in data[0][1]]), 0)
        self.color_axis_field = ColorAxisField(min=min_value)

        data_preprocessed = self._preprocess_data(data)

        self.series_field = SeriesField()
        self.series_field.add_serie(Series(name=data_preprocessed['name'], data=data_preprocessed['data']))

        self.x_axis_field = AxisField(is_x_axis=True)
        self.x_axis_field.set_categories(data_preprocessed['x_categories'])
        self.y_axis_field = AxisField(is_x_axis=False)
        self.y_axis_field.set_categories(data_preprocessed['y_categories'])

    def _preprocess_data(self, data):
        data_name = data[0][0]
        data_values = data[0][1]

        x_categories = list(OrderedDict.fromkeys([x for [x, y, z] in data_values]))
        y_categories = list(OrderedDict.fromkeys([y for [x, y, z] in data_values]))

        new_data_values = [[x_categories.index(x), y_categories.index(y), z] for [x, y, z] in data_values]

        result = {'name': data_name, 'data': new_data_values, 'x_categories': x_categories, 'y_categories': y_categories}
        return result

    def to_javascript(self):
        jsc = "{"
        jsc += self.chart_field.to_javascript() + ", "
        jsc += self.title_field.to_javascript() + ", "
        jsc += self.color_axis_field.to_javascript() + ", "
        jsc += self.x_axis_field.to_javascript() + ", "
        jsc += self.y_axis_field.to_javascript() + ", "
        jsc += self.series_field.to_javascript()
        jsc += "}"

        return jsc

    def script_header(self):
        # jsc = '''
        # <script src="/home/jpedro/workspace/tools/highcharts/js/highcharts.js"></script>
        # <script src="/home/jpedro/workspace/tools/highcharts/js/modules/heatmap.js"></script>
        # <script src="/home/jpedro/workspace/tools/highcharts/js/modules/exporting.js"></script> '''

        jsc = '''
            <script src="http://code.highcharts.com/highcharts.js"></script>
            <script src="http://code.highcharts.com/modules/heatmap.js"></script>
            <script src="http://code.highcharts.com/modules/exporting.js"></script>
        '''
        return jsc