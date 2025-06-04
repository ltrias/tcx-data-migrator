import xml.etree.ElementTree as ET


ns = {
    '': "http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2"
}


class TCXFile:
    def __init__(self, filename):
        ET.register_namespace('', ns[''])

        try:
            self._filename = filename
            self._tree = ET.parse(self._filename)
        except:
            print("Cannot load or parse " + self._filename)

    def save(self, filename=None, pretty_print=True):
        if filename is None:
            filename = self._filename
        
        try:
            if pretty_print:
                ET.indent(self._tree)
            self._tree.write(filename, encoding="UTF-8", xml_declaration=True)
            print("Saving " + filename)
        except:
            print("Cannot save " + filename)

    def extract_heart_rate(self):
        result = []

        for v in self.find_hr_nodes():
            result.append(int(v.text))
        return result

    def update_heart_rate_data(self, data):
        for i, n in enumerate(self.find_hr_nodes()):
            n.text = str(data[i])

    def find_hr_nodes(self):
        return self._tree.getroot().findall('./Activities/Activity/Lap/Track/Trackpoint/HeartRateBpm/Value', ns)

    def __str__(self):
        return __name__ + " Base: " + self._filename
