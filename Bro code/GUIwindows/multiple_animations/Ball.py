class Ball:
    def __init__(self, canvas, x, y, diameter, xvelocity, yvelocity, color):
        self.canvas = canvas
        self.image = canvas.create_oval(x, y, diameter, diameter, fill=color)
        self.xVelocity = xvelocity
        self.yVelocity = yvelocity

    def move(self):
        coordinates = self.canvas.coords(self.image)
        print(coordinates)
        if(coordinates[2] >= self.canvas.winfo_width() or coordinates[0] < 0):
            self.xVelocity *= - 1
        if(coordinates[3] >= self.canvas.winfo_width() or coordinates[1] < 0):
            self.yVelocity *= - 1

        self.canvas.move(self.image, self.xVelocity, self.yVelocity)