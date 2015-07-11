
class HighChart(object):

    def to_javascript(self):
        pass

    def script_header(self):
        # jsc = '''<script src="/home/jpedro/workspace/tools/highcharts/js/highcharts.js"></script>
        # <script src="/home/jpedro/workspace/tools/highcharts/js/modules/exporting.js"></script>
        # <script src="/home/jpedro/workspace/tools/highcharts/js/highcharts-more.js"></script> '''
        jsc = '''<script src="http://code.highcharts.com/highcharts.js"></script>
        <script src="http://code.highcharts.com/modules/exporting.js"></script>
        <script src="http://code.highcharts.com/highcharts-more.js"></script>'''
        return jsc