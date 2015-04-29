
class DataLabels(object):

    def __init__(self, enabled=True):
        self.enabled = enabled

    def show_labels(self, enable):
        if not type(enable) is bool:
             raise TypeError('enable should be a boolean (True or False).')
        self.enabled = enable

    def to_javascript(self):
        jsc = "dataLabels: {"
        jsc += "enabled: "
        if self.enabled:
            jsc += "true"
        else:
            jsc += "false"
        jsc += "}"
        return jsc
