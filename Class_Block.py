Class Block:
    color = (255, 255, 255)
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.x2, self.y1, self.y2 = \
            x1, x1, y1, x2, y2

    def render(self):
        pygame.draw.rect(screen, color, [self.x1, self.x2, self.y1, self.y2)


def collideWithBlock(self, Block):
    if (r.x>block.x1)and(r.x<block.x2)and(r.y>block.y1)and(r.y<block.y2):
        v.x = 50
        v.x = 0
        r.x +=v.x * delta








