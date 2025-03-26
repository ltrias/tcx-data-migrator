import xml.etree.ElementTree as ET
import logging
import sys

TCX_NAMESPACE = "http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2"


class TCXFile:
    def __init__(self, filename):
        ET.register_namespace('', TCX_NAMESPACE)

        try:
            self.filename = filename
            self.tree = ET.parse(self.filename)
        except:
            print("Cannot load or parse " + self.filename)

    def save(self, filename=None, pretty_print=True):
        if filename is None:
            filename = self.filename
        
        try:
            if pretty_print:
                ET.indent(self.tree)
            self.tree.write(filename, encoding="UTF-8", xml_declaration=True)
            print("Saving " + filename)
        except:
            print("Cannot save " + filename)

    def __str__(self):
        return __name__ + " Base: " + self.filename
    