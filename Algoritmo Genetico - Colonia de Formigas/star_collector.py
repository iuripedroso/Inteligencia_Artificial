import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import math

# ===================== CONFIGURAÇÕES =====================
NUM_STARS = 400    # número de estrelas
STAR_SPEED = 0.01  # velocidade (menor = mais lento)
STAR_SIZE = 0.01    # tamanho das estrelas

# ===================== GERAR ESTRELAS =====================
class Star:
    def __init__(self):
        # posição aleatória dentro de um cubo (-1 a 1)
        self.x = random.uniform(-1, 1)
        self.y = random.uniform(-1, 1)
        self.z = random.uniform(-1, 1)

        # brilho aleatório (para efeito de twinkle)
        self.brightness = random.uniform(0.5, 1.0)
        self.twinkle_speed = random.uniform(0.005, 0.02)

    def update(self):
        # movimento no eixo Z (aproximando-se da câmera)
        self.z += STAR_SPEED
        if self.z > 1:  # quando passa, reinicia atrás
            self.z = -1
            self.x = random.uniform(-1, 1)
            self.y = random.uniform(-1, 1)

        # efeito twinkle
        self.brightness += self.twinkle_speed
        if self.brightness > 1 or self.brightness < 0.3:
            self.twinkle_speed *= -1

    def draw(self):
        glColor3f(self.brightness, self.brightness, self.brightness)

        glBegin(GL_QUADS)
        glVertex3f(self.x - STAR_SIZE, self.y - STAR_SIZE, self.z)
        glVertex3f(self.x + STAR_SIZE, self.y - STAR_SIZE, self.z)
        glVertex3f(self.x + STAR_SIZE, self.y + STAR_SIZE, self.z)
        glVertex3f(self.x - STAR_SIZE, self.y + STAR_SIZE, self.z)
        glEnd()

# ===================== MAIN =====================
def main():
    pygame.init()
    pygame.display.set_mode((900, 700), DOUBLEBUF | OPENGL)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(70, 900/700, 0.1, 50.0)
    glTranslatef(0.0, 0.0, -2.5)

    stars = [Star() for _ in range(NUM_STARS)]

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # renderizar estrelas
        for s in stars:
            s.update()
            s.draw()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
