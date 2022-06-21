from tkinter import Canvas, Entry, Tk
from file import response_function

print(response_function())

root =Tk()
canv_size = 600
canvas = Canvas(root, width=canv_size, height=canv_size)
canvas.pack()

class Field:
    def __init__(self, task=None):
        self.task = task
        self.field_size = canv_size
        self.cell_size = canv_size//9
    def made_field(self):
        width_of_lines = 1
        for i in range(8):
            if i==2 or i ==5:
                width_of_lines = 5
            else:
                width_of_lines = 1
            canvas.create_line(0, self.cell_size*(i+1), self.field_size,self.cell_size*(i+1), fill='blue', width=width_of_lines)
            canvas.create_line(self.cell_size*(i+1), 0, self.cell_size*(i+1), self.field_size, fill='blue', width=width_of_lines)
        for i in range(len(self.task)):
            for j in range(len(self.task)):
                if self.task[i][j] !=0:
                    canvas.create_text(self.cell_size/2+ self.cell_size*j, self.cell_size/2+self.cell_size*i, text=self.task[i][j], font='Verdana 20', fill = 'green')

    def click_event(self, event):
        cell_coordinates = self.change_coords(event.x, event.y)
        a = Entry()
        a.place(x=100,y=100)
        
    
    def change_coords(self,x,y):
        row = y//self.cell_size
        column = x//self.cell_size
        return row,column


spisok = [[1,0,0,0,0,0,0,0,3], 
          [0,0,7,2,6,0,4,8,0], 
          [4,0,0,9,3,5,0,0,6],
          [0,3,0,4,8,0,2,0,0],      
          [0,4,1,6,0,9,3,0,0],
          [0,0,6,0,0,0,8,9,0],
          [5,7,8,0,4,0,0,0,2],
          [0,0,0,3,0,0,0,7,0],
          [2,0,0,0,0,0,0,0,5]]
field = Field(spisok)
field.made_field()
canvas.bind('<Button-1>', field.click_event)


# if len(spisok) !=9:
#     print('rukogop')
# for i in range(len(spisok)):
#     if len(spisok[i]) != 9:
#         print('rukogop')

# def check_digit(spisok, row, column, arg):
#     square_row = row // 3
#     square_column = column // 3
#     for i in range(square_row*3, square_row*3+3):
#         for j in range(square_column*3, square_column*3+3):
#             if arg == spisok[i][j]:
#                 return False
    
#     if arg in spisok[row]:
#         return False

#     for i in range(len(spisok)):
#         if spisok[i][column]==arg:
#             return False
    



# print(check_digit(spisok, 5, 0, 2))

# check_digit(spisok, 0, 8, 1)
# check_digit(spisok, 6, 2, 1)

root.mainloop()