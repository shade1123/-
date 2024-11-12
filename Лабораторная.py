import xml.etree.ElementTree as ET
import json

def xml_to_json(xml_file, json_file):
    # Читаем XML файл
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Рекурсивная функция для преобразования XML в словарь
    def xml_to_dict(element):
        result = {}
        for child in element:
            result[child.tag] = xml_to_dict(child) if len(child) > 0 else child.text
        return result

    # Преобразуем корень XML в словарь
    xml_dict = xml_to_dict(root)

    # Записываем словарь в JSON файл
    with open(json_file, 'w') as json_f:
        json.dump(xml_dict, json_f, indent=4)

xml_file = 'Каталог.xml'
json_file = 'Каталог1.json'

xml_to_json(xml_file, json_file)
