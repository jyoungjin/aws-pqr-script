import json
import os
from openpyxl import Workbook

dir_path = "/Users/youngjin/workspace/json-data/aws-pqr"
counts = dict()

write_wb = Workbook()

for(root, directories, files) in os.walk(dir_path):
    # file 순회
    for file in files:
        if '.json' in file:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as file:
                jsonData = json.load(file)
                if 'material_spec' in jsonData['base_metals'] and 'type_and_grade' in jsonData['base_metals']:

                    material_spec = jsonData['base_metals']['material_spec']
                    to_material_spec = jsonData['base_metals']['to_material_spec']
                    type_and_grade = jsonData['base_metals']['type_and_grade']
                    to_type_and_grade = jsonData['base_metals']['to_type_and_grade']

                    key = material_spec+","+type_and_grade
                    to_key = to_material_spec+","+to_type_and_grade
                    counts[key] = counts.get(key, 0) + 1
                    counts[to_key] = counts.get(to_key, 0) + 1

write_ws = write_wb.active
write_ws['A1'] = 'material_spec'
write_ws['B1'] = 'type_and_grade'
write_ws['C1'] = 'count'

for key, val in counts.items():
    arr = key.split(',')
    write_ws.append([arr[0], arr[1], val])

write_wb.save('/Users/youngjin/Desktop/test/test.xlsx')