from IPython.display import HTML, Javascript, display
import random
import string
import json

class HighChartsPlotter(object):
    '''
            Class responsible for plotting any Chart for HighCharts.
            Just call plot(chart).
    '''

    def _highchartify(self, chart_def = None, chart_def_json = None, script_header=None, height=400):
        assert chart_def or chart_def_json
        unique_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(15))
        if chart_def_json is None:
            chart_def_json = json.dumps(chart_def)
        html = script_header + '''
        <div id="chart_%(unique_id)s" style="min-width: 400px; height: %(height)ipx; margin: 0 auto">Re-run cell if chart is not shown ...</div>
        <script>
            do_chart_%(unique_id)s = function() {
                $('#chart_%(unique_id)s').highcharts(%(chart_def_json)s);
            }
            setTimeout("do_chart_%(unique_id)s()", 100)
        </script>
        ''' % locals()
        return HTML(html)

    def plot(self, chart):
        return self._highchartify(chart_def_json=chart.to_javascript(), script_header=chart.script_header())



