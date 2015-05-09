

class PlotOptionsField(object):

    def __init__(self):
        self.plot_options = []

    def add_plot_option(self, plot_option):
        self.plot_options.append(plot_option)

    def to_javascript(self):
        jsc = "plotOptions: {"
        for p in self.plot_options:
            jsc += p.to_javascript() + ","    # the last comma is accepted by javascript, no need to ignore
        jsc += "}"
        return jsc