import tkinter as tk
from turtle import width

class Game(tk.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)
        self.lives = 3
        self.width = 610
        self.height = 400
        self.bg = "#AAAAFF"
        self.canvas = tk.Canvas(self, width=self.width, height=self.height, bg=self.bg)        
        self.canvas.pack()
        self.pack()

        self.items = {}
        self.ball = None
        self.paddle = Paddle(self.canvas, self.width / 2, 326)
        self.items[self.paddle.item] = self.paddle

        for x in range(5, self.width - 75, 75):
            self.add_brick(x + 37.5, 50, 2)
            self.add_brick(x + 37.5, 70, 1)
            self.add_brick(x + 37.5, 90, 1)

        self.hud = None
        self.setup_game()
        self.canvas.focus_set()
        self.canvas.bind("<Left>", lambda _: self.paddle.move(-10))
        self.canvas.bind("<Right>", lambda _: self.paddle.move(10))

    def setup_game(self):
        self.add_ball()
        self.update_lives_text()
        self.text = self.draw_text(300, 200, "Press Space to start")
        self.canvas.bind("<space>", lambda _: self.start_game())

    def add_ball(self):
        if self.ball is not None:
            self.ball.delete()
        paddle_coords = self.paddle.get_position()
        x = (paddle_coords[0] + paddle_coords[2]) / 2
        self.ball = Ball(self.canvas, x, 310)
        self.paddle.set_ball(self.ball)

    def add_brick(self, x, y, hits):
        brick = Brick(self.canvas, x, y, hits)
        self.items[brick.item] = brick

    def draw_text(self, x, y, text, size="40"):
        font = ("Helvetica", size)
        return self.canvas.create_text(x, y, text=text, font=font)

    def update_lives_text(self):
        text = "Lives: %s" % self.lives
        if self.hud == None:
            self.hud = self.draw_text(50, 20, text, 15)
        else:
            self.canvas.itemconfig(self.hud, text=text)

    def start_game(self):
        self.canvas.unbind("<space>")
        self.canvas.delete(self.text)
        self.paddle.ball = None
        self.game_loop()

    def game_loop(self):
        #YOUDO-36:  call self's check_collisions method
        num_bricks = len(self.canvas.find_withtag("brick"))
        if num_bricks == 0:
            #YOUOD_37:  set self's ball's speed variable to None
            self.draw_text(300, 200, "You win!")
        elif self.ball.get_position()[3] >= self.height:
            self.ball.speed = None
            self.lives -= 1
            if self.lives < 0:
                self.draw_text(300, 200, "Game Over")
            else:
                self.after(1000, self.setup_game)
        else:
            self.ball.update()
            self.after(50, self.game_loop())

    def check_collisions(self):
        #YOUDO_38:  get the ball's coords from self.get_position and store in ball_coords
        items = self.canvas.find_overlapping(*ball_coords)
        objects = [self.items[x] for x in items if x in self.items]
        self.ball.collide(objects)
            

class GameObject(object):
    def __init__(self, canvas, item):
        self.canvas = canvas
        self.item = item

    def get_position(self):
        return self.canvas.coords(self.item)
    
    def move(self, x, y):
        self.canvas.move(self.item, x, y)

    def delete(self):
        self.canvas.delete(self.item)

class Ball(GameObject):
    def __init__(self, canvas, x, y):  #(x, y) is the center of the ball
        self.radius = 10
        self.direction = [1, -1]
        self.speed = 10
        x1 = x - self.radius
        y1 = y - self.radius
        x2 = x + self.radius
        y2 = y + self.radius
        color = "white"
        item = canvas.create_oval(x1, y1, x2, y2, fill=color)
        super(Ball, self).__init__(canvas, item)

    def update(self):
        coords = self.get_position()
        width = self.canvas.winfo_width()
        if coords[0] <= 0 or coords[2] >= width:
            self.direction[0] *= -1
        if coords[1] <= 0:
            self.direction[1] *= -1
        x = self.direction[0] * self.speed
        y = self.direction[1] * self.speed
        self.ball.move(self.item)
        #YOUDO_30:  call the move method for self passing in the appropriate arguments

    def collide(self, game_objects):
        coords = self.get_position()
        x = (coords[0] + coords[2]) / 2
        if len(game_objects) > 1:
            self.direction[1] *= -1
        elif len(game_objects) == 1:
            game_object = game_objects[0]
            # coords = self.get_position() YOUDO-34:  create a coords variable for game_object from get_position like before
            if x > coords[2]:
                self.direction[0] = 1
            elif x < coords[0]:
                self.direction[0] = -1
            else:
                self.direction[1] *= -1 
        
        for game_object in game_objects:
            if(isinstance(game_object, Brick)):
                game_object.hit()


class Paddle(GameObject):
    def __init__(self, canvas, x, y):  #(x, y) is the center of the paddle
        self.width = 80
        self.height = 10
        self.ball = None
        x1 = x - self.width / 2
        y1 = y - self.height / 2
        x2 = x + self.width / 2
        y2 = y + self.height / 2
        color = "blue"
        item = canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        super(Paddle, self).__init__(canvas, item)

    def set_ball(self, ball):
        self.ball = ball

    def move(self, offset):
        coords = self.get_position()
        width = self.canvas.winfo.width()
        x1 = coords[0]
        y1 = coords[1]
        x2 = coords[2]
        y2 = coords[3]
        if x1 + offset >= 0 and x2 + offset <= width:
            super(Paddle, self).move(offset, 0)
        if self.ball is not None:
            self.ball.move(offset, 0)

class Brick(GameObject):
    COLORS = {1 : "#999999", 2 : "#555555", 3 : "#222222"}

    def __init__(self, canvas, x, y, hits):
        self.width = 75
        self.height = 20
        self.hits = hits
        color = Brick.COLORS[hits]
        x1 = x - self.width / 2
        y1 = y - self.height / 2
        x2 = x + self.width / 2
        y2 = y + self.height / 2
        item = canvas.create_rectangle(x1, y1, x2, y2, color, tags="brick")       
        super(Brick, self).__init__(canvas, item)

    def hit(self):
        self.hits = self.hits - 1
        if self.hits == 0:
            self.delete()
        else:
            self.canvas.itemconfig(self.item, fill=Brick.COLORS[self.hits])

       
        

if __name__ == "__main__":    
    root = tk.Tk()
    game = Game(root)
    root.title("BREAKOUT")
    root.mainloop()