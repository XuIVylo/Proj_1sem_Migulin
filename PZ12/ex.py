from tkinter import Tk, Canvas, Frame, BOTH

window = Tk()
window.title('Example')
width = 700
height = 466
window.geometry(f'{width}x{height}+500+500')
window.resizable(False, False)

class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Цвета")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_rectangle(
            30, 10, 120, 80,
            outline="#fb0", fill="#fb0"
        )

        canvas.create_rectangle(
            150, 10, 240, 80,
            outline="#f50", fill="#f50"
        )

        canvas.create_rectangle(
            270, 10, 370, 80,
            outline="#05f", fill="#05f"
        )

        canvas.pack(fill=BOTH, expand=1)


window.mainloop()