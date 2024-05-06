import tkinter as tk

class Game(tk.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)    
        lives = 3
        self.width = 600
        self.height = 400
        self.bg = "#AAAAFF"
        self.canvas = tk.Canvas(self, bg= self.bg, width = self.width, height = self.height)
        self.canvas.pack()
        self.pack()

def GameObject(object):
    def __init__(self, canvas, item):
         self.canvas = canvas 
         self.item = item

    def get_positions(self):
        return self.canvas.coords(self.item)   

    def move(self, x, y):
        self.canvas.move(self.item, x, y)

    def delete(self):
        self.canvas.delete(self.item)  



if __name__ == '__main__':
    root = tk.Tk()
    root.title("BREAKOUT")
    game = Game(root)

    item = game.canvas.create_rectangle(10, 10, 100, 80, fill = "green")
    game_object = GameObject(game.canvas, item)
    game_object.move(50,50)




    root.mainloop()