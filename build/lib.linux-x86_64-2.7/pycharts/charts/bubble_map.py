from ..fields.title_field import TitleField
from ..fields.series_field import SeriesField
from ..fields.series.map_series import MapSeries
from ..fields.series.bubble_map_series import BubbleMapSeries
from highmap import HighMap

class BubbleMap(HighMap):

    def __init__(self, title, data, country_code='ch'):
        self.title_field = TitleField(text=title)
        self.series_field = SeriesField()
        self.series_field.add_serie(MapSeries(country_code))
        for (n, d) in data:
            self.series_field.add_serie(BubbleMapSeries(name=n, data=d))
        self.country_code = country_code


    def to_javascript(self):
        jsc = "'Map', {"
        jsc += self.title_field.to_javascript() + ", "
        jsc += self.series_field.to_javascript() + ", "
        jsc += "}"
        return jsc

    def script_header(self):
        jsc = '''
        <script src="http://cdnjs.cloudflare.com/ajax/libs/proj4js/2.2.2/proj4.js"></script>
        <script src="http://code.highcharts.com/maps/highmaps.js"></script>
        <script src="http://code.highcharts.com/maps/modules/data.js"></script>
        '''

        # <script src="/home/jpedro/workspace/tools/highmaps/js/highmaps.js"></script>
        # <script src="/home/jpedro/workspace/tools/highmaps/js/modules/data.js"></script>'''
        jsc += '<script src="http://code.highcharts.com/mapdata/countries/' + \
                self.country_code + '/' + self.country_code + '-all.js"></script>'
        return jsc