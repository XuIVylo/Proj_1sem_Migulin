from tkinter import *

window = Tk()
window.title('Example')
width = 700
height = 466
window.geometry(f'{width}x{height}+500+500')
window.resizable(False, False)

Canvas(window, bg='#356aa0', width=700, height=466, highlightbackground='#356aa0').place(x=0, y=0)
canvas = Canvas(window, height=440, width=670, bg='#356aa0', highlightbackground='#356aa0')
canvas.pack()
canvas.create_rectangle(2, 30, 670, 436, outline='white', width=1)

Label(text='Registration Details', bg='#356aa0', fg='white', font='Times 18').place(x=25, y=15)
Label(text='University:', bg='#356aa0', fg='white', font='Times 15').place(x=180, y=70)
Entry(bg='white', width=45, fg='black').place(x=280,y=73)
Label(text='Institute:', bg='#356aa0', fg='white', font='Times 15').place(x=195, y=110)
Entry(bg='white', width=45, fg='black').place(x=280,y=113)
Label(text='Branch:', bg='#356aa0', fg='white', font='Times 15').place(x=199, y=150)
Label(text='Degree:', bg='#356aa0', fg='white', font='Times 15').place(x=197, y=190)
Label(text='Avarage CPI:', bg='#356aa0', fg='white', font='Times 15').place(x=152, y=230)
Label(text='Experiense:', bg='#356aa0', fg='white', font='Times 15').place(x=165, y=270)
Label(text='Your Website or Blog:', bg='#356aa0', fg='white', font='Times 15').place(x=78, y=310)
Entry(text='http://',bg='white', width=45, fg='black').place(x=270,y=314)

from tkinter.ttk import *
combo = Combobox(window, width = 20)
combo['values']= ("[ None ]", "A", "B", "C", "F", "E")
combo.current(0)  # Элемент выбранный по умолчанию
combo.place(x=280, y=153)
combo1 = Combobox(window, width = 10)
combo1['values']= ("[ None ]", "A", "B", "C", "F", "E")
combo1.current(0)
combo1.place(x=280, y=193)

from tkinter import *
Radiobutton(window, text="Pursuing", bg='#356aa0', fg='white', value=1, font='Times 12').place(x=380, y=190)
Radiobutton(window, text="Completed", bg='#356aa0', fg='white', value=0, font='Times 12').place(x=460, y=190)
Spinbox(window, width=5 ).place(x=270, y=234)
Label(text='Upto', bg='#356aa0', fg='white', font='Times 12').place(x=315, y=232)
Spinbox(window, width=5 ).place(x=360, y=234)
Label(text='Th Semester', bg='#356aa0', fg='white', font='Times 12').place(x=405, y=232)
Spinbox(window, width=5 ).place(x=270, y=274)
Label(text='Years', bg='#356aa0', fg='white', font='Times 12').place(x=320, y=272)

window.mainloop()