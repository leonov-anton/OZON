from pyautocad import Autocad, APoint, distance
import json


acad = Autocad()

# db_circle = []
# n = 0
# for obj in acad.iter_objects('Circle'):
#     file = open('obj_cirlces.json', 'w')
#     db_circle.append({'Number': n, 'Centre': obj.Center, 'Layer': obj.Layer, 'ObjectName': obj.ObjectName})
#     n += 1
#     json.dump(db_circle, file, indent=1)
#     file.close()

db_lines = []
m = 0
for obj in acad.iter_objects('Line'):
    file = open('obj_lines.json', 'w')
    db_lines.append({'Number': m, 'ObjectName': obj.ObjectName, 'ObjectID': obj.ObjectID,
                     'Handle': obj.Handle, 'Length': obj.Length, 'Layer': obj.Layer})
    m += 1
    json.dump(db_lines, file, indent=1)
    file.close()

pp = APoint(2210581.291, 488153.2095)
acad.model.AddTable(pp, len(db_lines) + 4, 10, 8, 45)

k = 0
for table in acad.iter_objects('Table'):
    table.SetText(3, 6, 'Длина, м')
    for line in acad.iter_objects('Polyline'):
        k += 1
        table.SetText(3 + k, 6, str("=" + "%<\AcObjProp Object(%<\_ObjId " +
                                    str(line.ObjectID) + ">%).Length>%" + "*1.2" + "+5"))

