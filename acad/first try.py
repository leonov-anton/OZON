from pyautocad import Autocad, APoint, distance


acad = Autocad()
# acad.prompt("Hello, Autocad from Python\n")
# print(acad.doc.Name)

# p1 = APoint(0, 0)
# p2 = APoint(50, 25)
# # acad.model.AddMText(p1, 2.5, "Hello, World!")
#
# for i in range(5):
#     text = acad.model.AddText('Hi %s!' % i, p1, 2.5)
#     acad.model.AddLine(p1, p2)
#     acad.model.AddCircle(p1, 10)
#     p1.y += 10
#
# dp = APoint(10, 0)
# for text in acad.iter_objects('Text'):
#     print(text.InsertionPoint)
#     text.InsertionPoint = APoint(text.InsertionPoint) + dp
#
# for i in range(4):
#     text = acad.model.AddMText('Hi %s!' % i, p1, 2.5)
#
points = []
for obj in acad.iter_objects('Circle'):
    if obj.Layer == 'СИП С1-85 пром':
        points.append(obj.Center)
print(points)

    # print(obj.Layer)
#     points.append(obj.Name)
# print(points)

# a = 0
# for i in range(len(points)):
#     if distance(points[a], (points[a+1]) < 60:
#         print(distance(points[a], (points[a+1])
#         try:
#             acad.model.AddLine(APoint(points[a]), APoint(points[a+1]))
#             a += 1
#         except IndexError:
#             print("Готово!")
#
# a = 0
# for lines in acad.iter_objects('Line'):
#     a += (lines.Length)
#     print(lines.Length)
# print(a)
#
# b = 0
# for lines in acad.iter_objects('Polyline'):
#     b += (lines.Length)
# print(b)
#
# pp = APoint(407531, 6108260)
# acad.model.AddTable(pp, 5, 5, 8, 45)
#
# n = 1
# for table in acad.iter_objects('Table'):
#     table.SetText(1, 0, 'номер по опорядку')
#     table.SetText(1, 1, 'номер по')
#     table.SetText(1, 2, 'номер ')
#     for lines in acad.iter_objects('Polyline'):
#         n += 1
#         table.SetText(n, 0, 'H1'+str(n))
#         print(lines.Length)
#         table.SetText(n, 3, str(lines.Length))