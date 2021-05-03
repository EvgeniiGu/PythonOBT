from tkinter import *
#раскомментировать для чтения из файла
'''
number_of_numbers = 12
number = [0 for i in range(number_of_numbers)]
number_of_1 = [0 for i in range(number_of_numbers)]
f = open('E:\\Flan\\text.txt')                          #расположение файла
ij = 0

for line in f:
    number[ij] = str(format(int(line), '0>4b'))
#for i in range(number_of_numbers):
#    number[i] = str(format(int(input()), '0>4b'))
#    number_of_1[i] = number[i].count('1')
    number_of_1[ij] = number[ij].count('1')
    ij += 1
'''
def cliked():
    window1.destroy()
flag_btn = [0]*16
window1 = Tk()
number_T  = [None]*16
btn_submit = [Button(master=window1) for i in range(16)]
def btn_all(num):
    if flag_btn[num] == 0:
        number_T[num] = num
        btn_submit[num].config(relief=SUNKEN)
        btn_submit[num].pack()
        flag_btn[num] = 1
        window1.update()
        return 0
    elif flag_btn[num] == 1:
        number_T[num] = None
        btn_submit[num].config(relief=RAISED)
        btn_submit[num].pack()
        flag_btn[num] = 0
        window1.update()
        return 0

btn_submit[0].config(text=0, command=lambda: btn_all(0))
btn_submit[0].pack()
btn_submit[1].config(text=1, command=lambda: btn_all(1))
btn_submit[1].pack()
btn_submit[2].config(text=2, command=lambda: btn_all(2))
btn_submit[2].pack()
btn_submit[3].config(text=3, command=lambda: btn_all(3))
btn_submit[3].pack()
btn_submit[4].config(text=4, command=lambda: btn_all(4))
btn_submit[4].pack()
btn_submit[5].config(text=5, command=lambda: btn_all(5))
btn_submit[5].pack()
btn_submit[6].config(text=6, command=lambda: btn_all(6))
btn_submit[6].pack()
btn_submit[7].config(text=7, command=lambda: btn_all(7))
btn_submit[7].pack()
btn_submit[8].config(text=8, command=lambda: btn_all(8))
btn_submit[8].pack()
btn_submit[9].config(text=9, command=lambda: btn_all(9))
btn_submit[9].pack()
btn_submit[10].config(text=10, command=lambda: btn_all(10))
btn_submit[10].pack()
btn_submit[11].config(text=11, command=lambda: btn_all(11))
btn_submit[11].pack()
btn_submit[12].config(text=12, command=lambda: btn_all(12))
btn_submit[12].pack()
btn_submit[13].config(text=13, command=lambda: btn_all(13))
btn_submit[13].pack()
btn_submit[14].config(text=14, command=lambda: btn_all(14))
btn_submit[14].pack()
btn_submit[15].config(text=15, command=lambda: btn_all(15))
btn_submit[15].pack()

btn = Button(master=window1, command=cliked, text="Submit").pack()
window1.mainloop()
number_of_numbers = 0
for i in number_T:
    if i == None:
        continue
    else:
        number_of_numbers += 1
number = [0 for i in range(number_of_numbers)]
number_of_1 = [0 for i in range(number_of_numbers)]
j = 0
for i in range(16):
    if number_T[i] == None:
        continue
    else:
        number[j] = str(format(int(number_T[i]), '0>4b'))
        number_of_1[j] = number[j].count('1')
        j += 1
        

m_0 = [0]
m_1 = [0]*4
m_2 = [0]*6
m_3 = [0]*4
m_4 = [0]

flag_m_1 = m_1.copy()
flag_m_2 = m_2.copy()
flag_m_3 = m_3.copy()

t_0 = 0
t_1 = 0
t_2 = 0
t_3 = 0
t_4 = 0

for j in range(number_of_numbers):
    if number_of_1[j] == 0:
        m_0[t_0] = number[j]
        t_0 += 1
    elif number_of_1[j] == 1:
        m_1[t_1] = number[j]
        t_1 += 1
    elif number_of_1[j] == 2:
        m_2[t_2] = number[j]
        t_2 += 1
    elif number_of_1[j] == 3:
        m_3[t_3] = number[j]
        t_3 += 1
    elif number_of_1[j] == 4:
        m_4[t_4] = number[j]
        t_4 += 1

if t_0 == 0:
    m_0.remove(0)
for i in range(4-t_1):
    m_1.remove(0)
for i in range(6-t_2):
    m_2.remove(0)
for i in range(4-t_3):
    m_3.remove(0)
if t_4 == 0:
    m_4.remove(0)

m2_0 = [0]*t_0*t_1
m2_1 = [0]*t_1*t_2
m2_2 = [0]*t_2*t_3
m2_3 = [0]*t_3*t_4

flag_m2_0 = [1 for i in range(len(m2_0))]
flag_m2_1 = [1 for i in range(len(m2_1))]
flag_m2_2 = [1 for i in range(len(m2_2))]
flag_m2_3 = [1 for i in range(len(m2_3))]

t2_0 = 0
t2_1 = 0
t2_2 = 0
t2_3 = 0

def first_check_for_coincidence_of_the_number_of_digits(m1, m2, i, j):
    four = m1[i][0] != m2[j][0] and m1[i][1] != m2[j][1] and m1[i][2] != m2[j][2] and m1[i][3] != m2[j][3]
    if four == True:
        return True
    for k1 in range(4):
        for k2 in range(4):
            for k3 in range(4):
                three = m1[i][k1] != m2[j][k1] and m1[i][k2] != m2[j][k2] and m1[i][k3] != m2[j][k3]
                if three == True and k1 != k2 != k3:
                    return True
    for k1 in range(4):
        for k2 in range(4):
            two = m1[i][k1] != m2[j][k1] and m1[i][k2] != m2[j][k2]
            if two == True and k1 != k2:
                    return True



def second_check_for_coincidence_of_the_number_of_digits(m1, m2, i, j):
    four = m1[i][0] != m2[j][0] and m1[i][1] != m2[j][1] and m1[i][2] != m2[j][2] and m1[i][3] != m2[j][3]
    if four == True:
        return True
    for k1 in range(4):
        for k2 in range(4):
            for k3 in range(4):
                three = m1[i][k1] != m2[j][k1] and m1[i][k2] != m2[j][k2] and m1[i][k3] != m2[j][k3]
                if three == True and k1 != k2 != k3:
                    return True


if t_0 != 0:
    for i in range(t_1):
        m2_0[t2_0] = m_1[i]
        for k in range(4):
            if m_0[0][k] != m_1[i][k]: 
                m2_0[t2_0] = m2_0[t2_0][:k] + '~' + m2_0[t2_0][k+1:]
                t2_0 += 1
                break
if t_1 != 0 and t_2 != 0:
    for i in range(t_1):
        for j in range(t_2):
            m2_1[t2_1] = m_2[j]
            if first_check_for_coincidence_of_the_number_of_digits(m_1, m_2, i, j):
                continue
            else:
                for k in range(4):
                    if m_1[i][k] != m_2[j][k]: 
                        temporary_variable = m2_1[t2_1][:k] + '~' + m2_1[t2_1][k+1:]
                        flag_m_1[i] = 1
                        flag_m_2[j] = 1
                        if temporary_variable in m2_1:
                            break
                        else:
                            m2_1[t2_1] = temporary_variable
                            flag_m2_1[t2_1] = 1
                            t2_1 += 1
                            break
if t_2 != 0 and t_3 != 0:
    for i in range(t_2):
        for j in range(t_3):
            m2_2[t2_2] = m_3[j]
            if first_check_for_coincidence_of_the_number_of_digits(m_2, m_3, i, j):
                continue
            else:
                for k in range(4):
                    if m_2[i][k] != m_3[j][k]: 
                        temporary_variable = m2_2[t2_2][:k] + '~' + m2_2[t2_2][k+1:]
                        flag_m_2[i] = 1
                        flag_m_3[j] = 1
                        if temporary_variable in m2_2:
                            break
                        else:
                            m2_2[t2_2] = temporary_variable 
                            t2_2 += 1
                            break
if t_3 != 0 and t_4 != 0:
    for i in range(t_3):
        for j in range(t_4):
            m2_3[t2_3] = m_4[j]
            if first_check_for_coincidence_of_the_number_of_digits(m_3, m_4, i, j):
                continue
            else:
                for k in range(4):
                    if m_3[i][k] != m_4[j][k]: 
                        temporary_variable = m2_3[t2_3][:k] + '~' + m2_3[t2_3][k+1:]
                        flag_m_3[i] = 1
                        if temporary_variable in m2_3:
                            break
                        else:
                            m2_3[t2_3] = temporary_variable
                            t2_3 += 1
                            break
for i in range(4-t2_0):
    if 0 in m2_0:
        m2_0.remove(0)
for i in range(24-t2_1):
    if 0 in m2_1:
        m2_1.remove(0)
for i in range(24-t2_2):
    if 0 in m2_2:
        m2_2.remove(0)
for i in range(4-t2_3):
    if 0 in m2_3:
        m2_3.remove(0)

m3_0 = [0]*t2_0*t2_1
m3_1 = [0]*t2_1*t2_2
m3_2 = [0]*t2_2*t2_3

flag_m3_0 = m3_0.copy()
flag_m3_1 = m3_1.copy()
flag_m3_2 = m3_2.copy()

t3_0 = 0
t3_1 = 0
t3_2 = 0

if t2_0 != 0 and t2_1 != 0:
    for i in range(t2_0):
        for j in range(t2_1):
            if second_check_for_coincidence_of_the_number_of_digits(m2_0, m2_1, i, j):
                continue
            else:
                for k in range(4):
                    if m2_0[i][k] == '~' and m2_1[j][k] == '~':
                        for n in range(4):
                            if n == k:
                                continue
                            else:
                                if m2_0[i][n] != m2_1[j][n]:
                                    m3_0[t3_0] = m2_0[i]
                                    temporary_variable = m3_0[t3_0][:n] + '~' + m3_0[t3_0][n+1:]
                                    flag_m2_0[i] = 0
                                    flag_m2_1[j] = 0
                                    if temporary_variable in m3_0:
                                        m3_0[t3_0] = 0
                                        break
                                    else:
                                        m3_0[t3_0] = temporary_variable
                                        t3_0 += 1
                                        break
                        
if t2_1 != 0 and t2_2 != 0:
    for i in range(t2_1):
        for j in range(t2_2):
            if second_check_for_coincidence_of_the_number_of_digits(m2_1, m2_2, i, j):
                continue
            else:
                for k in range(4):
                    if m2_1[i][k] == '~' and m2_2[j][k] == '~':
                        for n in range(4):
                            if n == k:
                                continue
                            else:
                                if m2_1[i][n] != m2_2[j][n]:
                                    m3_1[t3_1] = m2_1[i]
                                    temporary_variable = m3_1[t3_1][:n] + '~' + m3_1[t3_1][n+1:]
                                    flag_m2_1[i] = 0
                                    flag_m2_2[j] = 0
                                    if temporary_variable in m3_1:
                                        m3_1[t3_1] = 0
                                        break
                                    else:
                                        m3_1[t3_1] = temporary_variable
                                        t3_1 += 1
                                        break
if t2_2 != 0 and t2_3 != 0:
    for i in range(t2_2):
        for j in range(t2_3):
            if second_check_for_coincidence_of_the_number_of_digits(m2_2, m2_3, i, j):
                continue
            else:
                for k in range(4):
                    if m2_2[i][k] == '~' and m2_3[j][k] == '~':
                        for n in range(4):
                            if n == k:
                                continue
                            else:
                                if m2_2[i][n] != m2_3[j][n]:
                                    m3_2[t3_2] = m2_2[i]
                                    temporary_variable = m3_2[t3_2][:n] + '~' + m3_2[t3_2][n+1:]
                                    flag_m2_2[i] = 0
                                    flag_m2_3[j] = 0
                                    if temporary_variable in m3_2:
                                        m3_2[t3_2] = 0
                                        break
                                    else:
                                        m3_2[t3_2] = temporary_variable
                                        t3_2 += 1
                                        break

for i in range(50):
    if 0 in m3_0:
        m3_0.remove(0)
for i in range(180):
    if 0 in m3_1:
        m3_1.remove(0)
for i in range(50):
    if 0 in m3_2:
        m3_2.remove(0)

flag_printed_m_0 = 0
flag_printed_m_1 = 0
flag_printed_m_2 = 0
flag_printed_m_3 = 0
flag_printed_m_4 = 0

flag_printed_m2_0 = 0
flag_printed_m2_1 = 0
flag_printed_m2_2 = 0
flag_printed_m2_3 = 0

flag_printed_m3_0 = 0
flag_printed_m3_1 = 0
flag_printed_m3_2 = 0


window2 = Tk()
canvas = Canvas(window2, height=600, width=1000, bg="#ccf9ff")
canvas.pack()
#canvas.create_rectangle(180,320, 310, 370)

first_column_rows = 0
second_column_rows = 0
third_column_rows = 0

while first_column_rows <= (t_0+t_1+t_2+t_3+t_4)*20:
    first_column_rows += 20
    if t_0 != 0 and flag_printed_m_0 == 0:
        first_column_rows -= 20
        canvas.create_text(5, first_column_rows, text = m_0, anchor = NW, font = "Verdana 14")
        first_column_rows += 20
        canvas.create_line(0, first_column_rows, 55, first_column_rows)
        flag_printed_m_0 = 1
        continue
    if t_1 > 0 and flag_printed_m_1 == 0:
        first_column_rows -= 20
        for i in range(t_1):
            canvas.create_text(5, first_column_rows, text=m_1[i], anchor=NW, font="Verdana 14")
            first_column_rows += 20
            if i == t_1-1:
                canvas.create_line(0, first_column_rows, 55, first_column_rows)
                flag_printed_m_1 = 1
        continue
    if t_2 > 0 and flag_printed_m_2 == 0:
        first_column_rows -= 20
        for i in range(t_2):
            canvas.create_text(5, first_column_rows, text=m_2[i], anchor=NW, font="Verdana 14")
            first_column_rows += 20
            if i == t_2-1:
                canvas.create_line(0, first_column_rows, 55, first_column_rows)
                flag_printed_m_2 = 1
        continue
    if t_3 > 0 and flag_printed_m_3 == 0:
        first_column_rows -= 20
        for i in range(t_3):
            canvas.create_text(5, first_column_rows, text=m_3[i], anchor=NW, font="Verdana 14")
            first_column_rows += 20
            if i == t_3-1:
                canvas.create_line(0, first_column_rows, 55, first_column_rows)
                flag_printed_m_3 = 1
        continue
    if t_4 != 0 and flag_printed_m_4 == 0:
        first_column_rows -= 20
        canvas.create_text(5, first_column_rows, text = m_4, anchor = NW, font = "Verdana 14")
        flag_printed_m_4 = 1
        continue
    canvas.create_line(55, 0, 55, (t2_0+t2_1+t2_2+t2_3)*20)

while second_column_rows <= (t2_0+t2_1+t2_2+t2_3)*20:
    second_column_rows += 20
    if t2_0 > 0 and flag_printed_m2_0 == 0:
        second_column_rows -= 20
        for i in range(t2_0):
            canvas.create_text(60, second_column_rows, text=m2_0[i], anchor=NW, font="Verdana 14")
            if flag_m2_0[i] == 0:
                canvas.create_oval(55, second_column_rows, 115, second_column_rows + 20, outline='red', width=2)
            second_column_rows += 20
            if i == t2_0-1:
                canvas.create_line(55, second_column_rows, 115, second_column_rows)
                flag_printed_m2_0 = 1
        continue
    if t2_1 > 0 and flag_printed_m2_1 == 0:
        second_column_rows -= 20
        for i in range(t2_1):
            canvas.create_text(60, second_column_rows, text=m2_1[i], anchor=NW, font="Verdana 14")
            if flag_m2_1[i] == 0:
                canvas.create_oval(55, second_column_rows, 115, second_column_rows + 20, outline='red', width=2)
            second_column_rows += 20
            if i == t2_1-1:
                canvas.create_line(55, second_column_rows, 115, second_column_rows)
                flag_printed_m2_1 = 1
        continue
    if t2_2 > 0 and flag_printed_m2_2 == 0:
        second_column_rows -= 20
        for i in range(t2_2):
            canvas.create_text(60, second_column_rows, text=m2_2[i], anchor=NW, font="Verdana 14")
            if flag_m2_2[i] == 0:
                canvas.create_oval(55, second_column_rows, 115, second_column_rows + 20, outline='red', width=2)
            second_column_rows += 20
            if i == t2_2-1:
                canvas.create_line(55, second_column_rows, 115, second_column_rows)
                flag_printed_m2_2 = 1
        continue
    if t2_3 > 0 and flag_printed_m2_3 == 0:
        second_column_rows -= 20
        for i in range(t2_3):
            canvas.create_text(60, second_column_rows, text=m2_3[i], anchor=NW, font="Verdana 14")
            if flag_m2_3[i] == 0:
                canvas.create_oval(55, second_column_rows, 115, second_column_rows + 20, outline='red', width=2)
            second_column_rows += 20
            flag_printed_m2_3 = 1
        continue
    canvas.create_line(115, 0, 115, (t3_0+t3_1+t3_2)*20)

while third_column_rows <= (t3_0+t3_1+t3_2)*20:
    third_column_rows += 20
    if t3_0 > 0 and flag_printed_m3_0 == 0:
        third_column_rows -= 20
        for i in range(t3_0):
            canvas.create_text(120, third_column_rows, text=m3_0[i], anchor=NW, font="Verdana 14")
            third_column_rows += 20
            if i == t3_0-1:
                canvas.create_line(115, third_column_rows, 180, third_column_rows)
                flag_printed_m3_0 = 1
        continue
    if t3_1 > 0 and flag_printed_m3_1 == 0:
        third_column_rows -= 20
        for i in range(t3_1):
            canvas.create_text(120, third_column_rows, text=m3_1[i], anchor=NW, font="Verdana 14")
            third_column_rows += 20
            if i == t3_1-1:
                canvas.create_line(115, third_column_rows, 180, third_column_rows)
                flag_printed_m3_1 = 1
        continue
    if t3_2 > 0 and flag_printed_m3_2 == 0:
        third_column_rows -= 20
        for i in range(t3_2):
            canvas.create_text(120, third_column_rows, text=m3_2[i], anchor=NW, font="Verdana 14")
            third_column_rows += 20
            if i == t3_2-1:
                canvas.create_line(115, third_column_rows, 180, third_column_rows)
                flag_printed_m3_2 = 1
        continue
numbers = []
numbers.extend(m_0)
numbers.extend(m_1)
numbers.extend(m_2)
numbers.extend(m_3)
numbers.extend(m_4)
M_3 = []
M_3.extend(m3_0)
M_3.extend(m3_1)
M_3.extend(m3_2)
def not_involved_variables(t_, flag_, m_):
    for i in range(t_):
        if flag_[i] == 1:
            M_3.append(m_[i])
not_involved_variables(t2_0, flag_m2_0, m2_0)
not_involved_variables(t2_1, flag_m2_1, m2_1)
not_involved_variables(t2_2, flag_m2_2, m2_2)
not_involved_variables(t2_3, flag_m2_3, m2_3)
column = 350
#+(50*len(numbers))
row = 50
for i in numbers:
    canvas.create_text(column, row, text=i, anchor=NW, font="Verdana 14")
    column += 50
column = 300
for j in M_3:
    row += 20
    canvas.create_text(column, row, text=j, anchor=NW, font="Verdana 12")
for i in range(column, (len(numbers))*50+column+50, 50):
    for j in range(50, row+20, 20):
        canvas.create_line(i, j, i, j+20)
        canvas.create_line(i, j, i+50, j)
canvas.create_line(i+50, 50, i+50, j+20)
canvas.create_line(column, j+20, i+50, j+20)

array_of_asterisks = [[0 for i in range(len(M_3))] for j in range(len(numbers))]
def check_for_coincidence_of_digits(m1, m2, i, j):
    if m2[j].count('~') > 1:
        for k1 in range(4):
            if m2[j][k1] == '~':
                continue
            else:
                for k2 in range(4):
                    if m2[j][k2] == '~':
                        continue
                    else:
                        two = m1[i][k1] == m2[j][k1] and m1[i][k2] == m2[j][k2]
                        if two == True and k1 != k2:
                                return True
    else:
        for k1 in range(4):
            if m2[j][k1] == '~':
                continue
            else:
                for k2 in range(4):
                    if m2[j][k2] == '~':
                        continue
                    else:
                        for k3 in range(4):
                            if m2[j][k3] == '~':
                                continue
                            else:
                                three = m1[i][k1] == m2[j][k1] and m1[i][k2] == m2[j][k2] and m1[i][k3] == m2[j][k3]
                                if three == True and k1 != k2 and k1 != k3 and k2 != k3:
                                    return True
    return False
for i in range(len(numbers)):
   for j in range(len(M_3)):
       if check_for_coincidence_of_digits(numbers, M_3, i, j):
           array_of_asterisks[i][j] = 1
for i in range(len(array_of_asterisks)):
    for j in range(len(array_of_asterisks[i])):
        if array_of_asterisks[i][j] == 1:
            canvas.create_text(column+50+i*50, 70+j*20, text="  *", anchor=NW, font="Verdana 18")
window2.mainloop()