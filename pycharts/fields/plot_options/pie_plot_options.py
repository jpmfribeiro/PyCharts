from pycharts.fields.plot_options.data_labels import DataLabels

class PiePlotOptions(object):

    def __init__(self):
        self.allow_point_select = True
        self.cursor = 'pointer'
        self.data_labels = DataLabels(enabled=False)
        self.show_in_legend = True

    def set_allow_point_select(self, enable):
        if not type(enable) is bool:
             raise TypeError('enable should be a boolean (True or False).')
        self.allow_point_select = enable

    def show_legend(self, enable):
        if not type(enable) is bool:
             raise TypeError('enable should be a boolean (True or False).')
        self.show_in_legend = enable
        self.data_labels.show_labels(not enable)

    def to_javascript(self):
        jsc = "pie: {"
        jsc += "allowPointSelect: "
        if self.allow_point_select:
            jsc += "true"
        else:
            jsc += "false"
        jsc += ", cursor: '" + self.cursor + "'"
        jsc += ", " + self.data_labels.to_javascript()
        jsc += ", showInLegend: "
        if self.show_in_legend:
            jsc += "true"
        else:
            jsc += "false"
        jsc += "}"
        return jsc