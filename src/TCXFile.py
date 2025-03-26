import xml.etree.ElementTree as ET

TCX_NAMESPACE = "http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2"


class TCXFile:
    def __init__(self, filename):
        ET.register_namespace('', TCX_NAMESPACE)
        try:
            self.root = ET.parse(filename)
        except:
            print("Cannot load " + filename)
        print(self.root)

    def save(self, filename):
        pass
