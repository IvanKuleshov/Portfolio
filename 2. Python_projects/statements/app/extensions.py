from flask_sqlalchemy import SQLAlchemy
import lxml.etree as ET

db = SQLAlchemy()




def ApplyStyle(xml):
    dom = ET.parse(xml)
    #print(dom)
    #xslt = ET.parse("XSLT.xsl")
    #transform = ET.XSLT(xslt)
    #newdom = transform(dom)
    #print(ET.tostring(newdom, pretty_print=True))
