import tkinter as tk
from PIL import ImageGrab, ImageTk

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        # self.h1, self.w1 = tk.IntVar(), tk.IntVar()
        # self.h2, self.w2 = tk.IntVar(), tk.IntVar()
        self.bbox_r = [tk.IntVar() for i in range(4)]

        self.withdraw()
        self.attributes('-fullscreen', True)

        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill="both",expand=True)

        image = ImageGrab.grab()
        self.image = ImageTk.PhotoImage(image)
        self.photo = self.canvas.create_image(0,0,image=self.image,anchor="nw")

        self.x, self.y = 0, 0
        self.rect, self.start_x, self.start_y = None, None, None
        self.deiconify()

        self.canvas.tag_bind(self.photo,"<ButtonPress-1>", self.on_button_press)
        self.canvas.tag_bind(self.photo,"<B1-Motion>", self.on_move_press)
        self.canvas.tag_bind(self.photo,"<ButtonRelease-1>", self.on_button_release)


    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(self.x, self.y, 1, 1, outline='red')

    def on_move_press(self, event):
        curX, curY = (event.x, event.y)
        self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY)

    def on_button_release(self, event):
        self.bbox = self.canvas.bbox(self.rect)
        self.withdraw()
        self.new_image = ImageTk.PhotoImage(ImageGrab.grab(self.bbox))
        self.attributes('-fullscreen', False)
        self.title("Image grabbed")
        self.canvas.destroy()
        self.deiconify()
        self.set_vals()
        self.destroy()
    
    def set_vals(self):
        for i in range(4):
            self.bbox_r[i].set(self.bbox[i])

if __name__ == '__main__':
    root = GUI()
    root.mainloop()