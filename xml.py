import pprint
import xml.etree.ElementTree as ET
content = """<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <project name="Austria" direction="E"/>
        <project name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <project name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <project name="Costa Rica" direction="W"/>
        <project name="Colombia" direction="E"/>
    </country>
</data>
"""

# doc = xml.dom.minidom.parseString(content)

# root = doc.documentElement

# # print(root)
# for node in root.getElementsByTagName("project"):
#     if node.getAttribute("revision") == "asdf12.git":
#         node.setAttribute("revision", "123")
#         print(node.getAttribute("revision"))
        # print(node)
# print(content)
# xml.dom.minidom.

root = ET.fromstring(content)

for node in root.iter("project"):
    if node.attrib["name"] == "Colombia":
        node.attrib["direction"] = "123"

# for node in root.iter("project"):
#     print(node.attrib)

s= ET.tostring(root, encoding="utf-8", method="xml")
print(s.decode("utf-8"))
