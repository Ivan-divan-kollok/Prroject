Class Ball:
    def __init__(self, x = 100+random.random()*100, y = 0, vx = 0, vy = 0, g = 500, rad = 10, k = 0,5, i=1):
        self.x, self.y, self.vx, self.vy, self.g, self.rad, self.k, self.i = \
                x, y, vx, vy, g, rad, k, i

    def update(self, game):
        """Update Player state"""
        r.x[0] += v.x[0] * delta
        r.x[1] += v.x[1] * delta-0.5*g*delta*delta
        v.x[1] +=0.5*g*delta
        i+=1

        """Do not let Player get out of the Game window"""
        if r.x[0] < rad:
            if v.x[0] < 0:
                v.x[0] = -v.x[0]
                r.x[0] = rad
        if r.x[1] < rad:
            if v.x[1] < 0:
                v.x[1] = -v.x[1]
                r.x[1] = -rad
        if r.x[0] > 600-rad:
            if v.x[0] > 0:
                v.x[0] = -v.x[0]
                r.x[0] = 600-rad

        if r.x[1] > 600-rad:
            if v.x[1] > 0:
                v.x[1] = -k*v.x[1]
                r.x[1] = 600-rad

    def render(self, game):
        """Draw Ball on the Game window"""
        pygame.draw.circle(game.screen,
                (self.color, self.color, self.color),
                (int(self.x), int(self.y)), self.r)