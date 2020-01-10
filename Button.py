class Widget :
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = [x, y, x+w, y+h]

    def detect(self, x, y):
        return (self.x < x < self.x + self.w) and (self.y < y < self.y + self.h)



class Button(Widget) :
    """Boutton de sous-widget canvas"""
    def __init__(self, canvas, x, y, w, h, name="Button", f = lambda : print("You pressed a button"), colorSchem=["#000000", "#444433", "#998755"]):
        Widget.__init__(self, x, y, w, h)
        self.cv = canvas
        self.name = name
        self.function = f
        self.thm = colorSchem

        self.wdg = self.cv.create_rectangle( self.rect, fill=self.thm[0], outline="")
        self.txt = self.cv.create_text( self.x + self.w//2, self.y + self.h//2, text=self.name, fill="#EEEEEE")
        self.selected = False
        self.pushed = False


    def onMotion(self, cursor):
        self.selected = self.detect(cursor["x"], cursor["y"])
        if not self.pushed:
            if self.selected :
                self.grow(0)
                self.render(self.thm[1])
            else:
                self.grow(0)
                self.render(self.thm[0])

    def onPress(self, cursor):
        if self.selected :
            self.pushed = True
            self.grow(5)
            self.render(self.thm[2])


    def onRelease(self, cursor):
        if self.selected:
            if self.pushed:
                self.function()
                self.grow(0)
                self.render(self.thm[1])
            else:
                self.grow(0)
                self.render(self.thm[0])
        else:
            self.grow(0)
            self.render(self.thm[0])
        self.pushed = False

    def clear(self):
        self.cv.delete(self.wdg)
        self.cv.delete(self.txt)

    def grow(self, v=0):
        self.rect = [self.x-v, self.y-v, self.x+self.w+v, self.y+self.h+v]

    def render(self, color):
        self.clear()

        self.wdg = self.cv.create_rectangle( self.rect, fill=color, outline="")
        self.txt = self.cv.create_text( self.x + self.w//2, self.y + self.h//2, text=self.name, fill="#EEEEEE")
