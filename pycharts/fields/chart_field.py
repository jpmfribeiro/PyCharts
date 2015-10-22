

class ChartField(object):

    '''
            The Python class representation of the chart options, as specified in http://api.highcharts.com/highcharts#chart
            This is a reduced version with only the most important options.
    '''

    def __init__(self):
        # self.align_ticks = True  # When using multiple axis, the ticks of two or more opposite axes will automatically be aligned by adding ticks to the axis or axes with the least ticks.
        #                          # This can be prevented by setting alignTicks to false.
        #                          # If the grid lines look messy, it's a good idea to hide them for the secondary axis by setting gridLineWidth to 0. Defaults to true.

        # self.animation = True    # Set the overall animation for all chart updating.

        #self.background_color = "#FFFFFF"   # Default: white
        self.render_to = None    # The HTML element where the chart will be rendered.
        self.type = "line"       # The chart type. TODO: Create some Enum or class for chart types?

# SETTERS

    def set_type(self, chart_type):
        valid_types = ['area', 'arearange', 'areaspline', 'areasplinerange',
                       'bar', 'boxplot', 'bubble', 'column', 'columnrange',
                       'errorbar', 'funnel', 'gauge', 'heatmap', 'line',
                        'pie', 'polygon', 'pyramid', 'scatter', 'series',
                        'solidgauge', 'spline', 'treemap', 'waterfall']     # TODO: Create some Enum or class

        if chart_type not in valid_types:
            raise AttributeError('type ' + str(chart_type) + ' is not supported, it should be one of: ' + str(valid_types))
        else:
            self.type = chart_type

    # def set_align_ticks(self, align):
    #     if not type(align) is bool:
    #         raise TypeError('align should be a boolean (True or False).')
    #     else:
    #         self.align_ticks = align

    # def set_animation(self, animation):
    #     if not type(animation) is bool:
    #         raise TypeError('animation should be a boolean (True or False).')
    #     else:
    #         self.animation = animation

    def set_render_to(self, html_div):
        self.render_to = str(html_div)

    def set_background_color(self, color):
        self.background_color = color


# OUTPUT

    def to_javascript(self):
        jsc = "chart: {"
        jsc += "type: '" + self.type + "'"
        if self.render_to is not None:
            jsc += ", renderTo: '" + self.render_to + "'"
        #jsc += ", backgroundColor: '" + self.background_color + "'"
        jsc += "}"

        return jsc
