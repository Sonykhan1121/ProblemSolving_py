import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    total=0
    a = [node]
    while a:
        current_node = a.pop()
        print(current_node.attrib)
        total+=len(current_node.attrib)
        a.extend(list(current_node))
    return total

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))