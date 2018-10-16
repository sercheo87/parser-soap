import xml.etree.ElementTree as ET

with open('/apps/example.xml', 'r') as myfile:
  countrydata = myfile.read()

ns = {'urn': 'urn:iso:std:iso:20022:tech:xsd:pacs.008.001.04'}

ET.register_namespace('urn', 'urn:iso:std:iso:20022:tech:xsd:pacs.008.001.04')
root = ET.fromstring(countrydata)

# for fito in root.findall("urn:FIToFICstmrCdtTrf", ns):
#     print('----')
#     for header in fito.findall("urn:GrpHdr", ns):
#         name = header.find('urn:MsgId', ns)
#         print(header.text)

headers = {}

def transformItem(element):
    for item in element.getchildren():
        if item.getchildren():
            transformItem(item)
        else:
            tagName = item.tag.split('}')[1]
            headers[tagName] = item.text

def eachItem(element):
    for item in element.getchildren():
        tagName = item.tag.split('}')[1]
        if(tagName == 'GrpHdr'):
            print('tag:', tagName)
            print('text:', item.text)
            print('attrib:', item.attrib)
            transformItem(item)
        # eachItem(item)

for item in root.getchildren():
    eachItem(item)

print('===========================================================')
print('HEADERS')
print('===========================================================')
for key,val in headers.items():
    print(key, "=>", val)