from xml.sax.xmlreader import XMLReader
from xml.sax import ContentHandler, make_parser, handler # type: ignore
from typing import Any


class XMLHandler(ContentHandler):  # type: ignore
    def __init__(self) -> None:
        self.CurrentData = ""
        self.color = ""

   # Call when an element starts
    def startElement(self, tag: str, attributes: Any) -> None:
        self.CurrentData = tag
        if(tag == "color"):
            print("*****Color*****")
            hex = attributes["hex"]
            print("Color HexCode:", hex)

   # Call when an elements ends
    def endElement(self, tag: str) -> None:
        if(self.CurrentData == "color"):
            print("Color Name:", self.color)
        self.CurrentData = ""

   # Call when a character is read
    def characters(self, content: str) -> None:
        if(self.CurrentData == "color"):
            self.color = content

# create an XMLReader
parser: XMLReader = make_parser()

# turn off namepsaces
parser.setFeature(handler.feature_namespaces, 0)  # type: ignore

# override the default ContextHandler
Handler = XMLHandler()
parser.setContentHandler( Handler )  # type: ignore
parser.parse("sample.xml")  # type: ignore