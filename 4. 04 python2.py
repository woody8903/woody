from tkinter import*
import xlsxwriter
window = Tk()

window = Tk()
photo = PhotoImage(file = 'C:/Users/djkang/Desktop/noname.gif')
h = photo.height()
w = photo.width()
print('이미지 크기:',h, 'x', w)

workbook = xlsxwriter.Workbook('C:/Users/djkang/Desktop/noname.gif')
photoR = [[0 for _ in range(h)] for _ in range(w)]
photoG = [[0 for _ in range(h)] for _ in range(w)]
photoB = [[0 for _ in range(h)] for _ in range(w)]

workbook = xlsxwriter.Workbook('C:/Users/djkang/Desktop/noname.gif')
worksheetR = workbook.add_worksheet('photoR')
worksheetG = workbook.add_worksheet('photoG')
worksheetB = workbook.add_worksheet('photoB')

for i in range(w):
    for k in range(h):
        r, g, b = photo.get(i,k)
        worksheetR.write(i, k, photoR[i][k])
        worksheetG.write(i, k, photoG[i][k])
        worksheetB.write(i, k, photoB[i][k])

    workbook.close()
    print('Save. Ok~')