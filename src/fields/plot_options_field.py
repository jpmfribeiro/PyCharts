

class PlotOptionsField(object):

    def __init__(self):
        self.plot_options = []

    def add_plot_option(self, plot_option):
        self.plot_options.append(plot_option)

    def to_javascript(self):