

class TitleField(object):

    '''
            The Python class representation of the title options, as specified in http://api.highcharts.com/highcharts#title
            This is a reduced version with only the most important options.
    '''

    def __init__(self, text=""):
        self.text = text
        self.align = 'center'

    def set_text(self, text):
        self.text = str(text)

    def set_align(self, align):
        valid_aligns = ['center', 'left', 'right']

        if align not in valid_aligns:
            raise AttributeError('align ' + str(align) + ' is not supported, it should be one of: ' + str(valid_aligns))
        else:
            self.align = align

    def to_javascript(self):
