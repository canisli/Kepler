import math

import manim.utils.color as c
from manim import *

ellipse = Ellipse(width=2, height=1.5)
planet = Dot(color=c.BLUE)
sun = Dot(radius=0.15, color=c.YELLOW)
sun2 = sun.copy().shift(np.array([-0.661, 0, 0]))
planet2 = planet.copy().shift(RIGHT)


class Kepler(Scene):
    def construct(self):
        self.play(GrowFromCenter(ellipse))
        self.add(planet)
        self.play(Transform(planet, planet2))
        self.add(sun)
        self.play(Transform(sun, sun2))
        self.play(MoveAlongPath(planet, ellipse), run_time=7, rate_func=vis_viva)


def vis_viva(t: float) -> float:
    pla_x = planet.get_x()
    pla_y = planet.get_y()
    sun_x = sun.get_x()
    sun_y = sun.get_y()
    r = math.sqrt((pla_x - sun_x) ** 2 + (pla_y - sun_y) ** 2)
    a = max(ellipse.width, ellipse.height) / 2
    return 2 / r - 1 / a
