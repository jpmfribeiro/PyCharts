
class HighMap(object):

    def script_header(self):
        jsc = '''
        <script src="http://cdnjs.cloudflare.com/ajax/libs/proj4js/2.2.2/proj4.js"></script>
        <script src="http://code.highcharts.com/maps/highmaps.js"></script>
        <script src="http://code.highcharts.com/maps/modules/data.js"></script>
        '''
        return jsc