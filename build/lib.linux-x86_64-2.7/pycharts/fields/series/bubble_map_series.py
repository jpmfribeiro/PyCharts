
class BubbleMapSeries(object):

    def __init__(self, name, data, max_size=12):
        self.type = 'mapbubble'
        self.name = name
        self.data = data
        self.max_size = max_size

    def to_javascript(self):
        jsc = "{ type: '" + self.type + "', name: '" + self.name + "', "
        jsc += "maxSize: '" + str(self.max_size) + "%',"
        jsc += "data: ["

        for [z, lat, lon] in self.data:
            jsc += "{ "
            jsc += "z: " + str(z) + ","
            jsc += "lat: " + str(lat) + ","
            jsc += "lon: " + str(lon) + ","
            jsc += "}, "

        jsc += "]}"
        return jsc


