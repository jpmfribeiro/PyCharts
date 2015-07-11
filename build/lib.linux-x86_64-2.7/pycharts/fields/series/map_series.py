
class MapSeries(object):

    def __init__(self, country_code='ch'):
        self.country_code = country_code

    def to_javascript(self):
        jsc = ''' { type: 'map', showInLegend: false,'''
        jsc += "mapData: Highcharts.maps['countries/" + \
               self.country_code + "/" + self.country_code + "-all'] }"
        return jsc