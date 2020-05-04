read_pass = input("Укажите путь к файлу: ")
wright_pass = input("Укажите путь к файлу для записи: ")

data = open(read_pass, 'r')
result = open(wright_pass, 'w')
int_line = [[int(i) for i in line.split()] for line in data]
m = 0
for x in int_line:
    m += 1
    summa = sum(x)
    mean = summa/len(x)
    result.write("Sum " + str(m) + " line: " +str(summa)+'\n')
    result.write("Mean " + str(m) + " line: " + str(mean)+'\n')
    print(summa, mean)
data.close()
result.close()