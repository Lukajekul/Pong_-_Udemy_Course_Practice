from turtle import Turtle
ALIGNEMENT = "center"
FONT = ("Courier", 24, "normal")

class Score(Turtle):
    def __init__(self, stop_callback):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scorebord()
        self.stop_callback = stop_callback
    
    def update_scorebord(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))        

    def l_point(self):
        self.l_score += 1
        self.update_scorebord()

    def r_point(self):
        self.r_score += 1
        self.update_scorebord()

    def game_ower(self):
        self.goto(0,0)
        self.write(f"Game ower", align= ALIGNEMENT, font= FONT)
        self.stop_callback()

    def l_won(self):
        self.goto(0,0)
        self.write(f"Left won", align= ALIGNEMENT, font= FONT)
        self.stop_callback()

    def r_won(self):
        self.goto(0,0)
        self.write(f"Right won", align= ALIGNEMENT, font= FONT)
        self.stop_callback()