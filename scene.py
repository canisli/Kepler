from manim import *
from numpy import product

ellipse = Ellipse(width=2, height=1.5)
planet = Dot(color=BLUE)
sun = Dot(radius=0.15, color=YELLOW)
sun2 = sun.copy().shift(np.array([-0.661, 0, 0]))
planet2 = planet.copy().shift(RIGHT)


def get_line(a, b):
    return Line(a.get_center(), b.get_center()).set_stroke(width=2)


# def vis_viva(t: float) -> float:
#     pla_x = planet.get_x()
#     pla_y = planet.get_y()
#     sun_x = sun.get_x()
#     sun_y = sun.get_y()
#     r = math.sqrt((pla_x - sun_x) ** 2 + (pla_y - sun_y) ** 2)
#     print(r)
#     a = max(ellipse.width, ellipse.height) / 2
#     return math.sqrt(2 / r - 1 / a)


class FirstLaw(Scene):
    def construct(self):
        self.play(GrowFromCenter(ellipse))
        self.add(planet)
        self.play(Transform(planet, planet2))
        self.add(sun)
        self.play(Transform(sun, sun2))
        self.play(MoveAlongPath(planet, ellipse), run_time=7,
                  rate_func=rate_functions.ease_in_out_cubic)


class SecondLaw(Scene):
    def construct(self):
        self.play(GrowFromCenter(ellipse))
        self.add(planet)
        self.play(Transform(planet, planet2))
        self.add(sun)
        self.play(Transform(sun, sun2))
        line = get_line(planet, sun)
        self.add(get_line(planet, sun))
        line.add_updater(
            self.add(get_line(planet, sun))
        )
        self.add_foreground_mobjects(planet)
        self.add(line)
        self.play(MoveAlongPath(planet, ellipse), run_time=7,
                  rate_func=rate_functions.ease_in_out_cubic)


class ThirdLaw(Scene):
    def construct(self):
        equation = MathTex(
            "T^2=\\frac{4\\pi^2}{GM}a^3"
        )
        self.play(Write(equation))


class NewtonSecondLaw(Scene):
    def construct(self):
        title = Title("Newton's Second Law of Motion")

        equation = MathTex(
            "F_{\\textrm{net}}=ma"
        ).shift(np.array([0, 2, 0]))
        m = Square(side_length=2.0, color=WHITE,
                   fill_opacity=1).shift(np.array([0, -0.5, 0]))
        force = Arrow(start=m.get_center(), end=m.get_center() +
                      RIGHT*2, buff=0, color=PURPLE)
        force_label = MathTex("F", color=PURPLE).shift(
            np.array([2.3, -0.5, 0]))

        self.play(Write(title))
        self.play(Write(equation))
        self.wait()
        self.play(GrowFromCenter(m))
        self.play(GrowArrow(force), Write(force_label))
        self.wait(5)


class GravityLaw(Scene):
    def construct(self):
        title = Title("Newton's Law of Universal Gravitation")

        equation = MathTex(
            "F=-\\frac{Gm_1m_2}{r^2}\\mathbf{\hat{r}}"
        ).shift(np.array([0, 1.5, 0]))

        G = MathTex(
            "G=6.674\\times 10^{-11}{\\textrm{m}}^3{\\textrm{kg}}^{-1}{\\textrm{s}}^{-2}"
        ).shift(np.array([0, 0.4, 0])).scale(0.5)

        m1 = Dot(radius=0.21).shift(np.array([-2.5, -0.75, 0]))
        m2 = Dot(radius=0.35).shift(np.array([+2.5, -0.75, 0]))
        m1_label = MathTex(
            "m_1"
        ).shift(np.array([-2.5, -1.5, 0]))
        m2_label = MathTex(
            "m_2"
        ).shift(np.array([+2.5, -1.5, 0]))
        m1_force = Arrow(start=m1.get_center(),
                         end=m1.get_center() + 2 * RIGHT, buff=0, color=PURPLE)
        m2_force = Arrow(start=m2.get_center(),
                         end=m2.get_center() + 2 * LEFT, buff=0, color=PURPLE)
        self.play(Write(title))
        self.wait()
        self.play(Write(equation), Write(G), GrowFromCenter(m1),
                  GrowFromCenter(m2), Write(m1_label), Write(m2_label))
        self.wait(5)
        self.play(GrowArrow(m1_force), GrowArrow(m2_force))
        self.wait(5)


class SolveAcceleration(Scene):
    def construct(self):
        equation = MathTex(
            "F=ma=-\\frac{GmM}{r^2}\\mathbf{\hat{r}}"
        )
        acceleration = MathTex(
            "a=-\\frac{GM}{r^2}\\mathbf{\hat{r}}"
        )
        self.play(Write(equation))
        self.wait()
        self.play(ReplacementTransform(equation, acceleration))


class DefineH(Scene):
    def construct(self):
        product_rule = MathTex(
            "\\vec{h}=\\vec{r}\\times\\vec{v}"
        )
        dhdt = MathTex(
            "\\frac{d\\vec{h}}{dt}=\\dot{\\vec{r}}\\times\\vec{v} + \\dot{\\vec{v}}\\times\\vec{r}"
        )
        simplified = MathTex(
            "=\\vec{v}\\times\\vec{v} + \\vec{a}\\times\\vec{r}=0"
        ).shift(np.array([0.8, -1, 0]))
        up = MathTex(
            "\\vec{h}=\\vec{r}\\times\\vec{v}"
        ).to_edge(UP)
        self.play(Write(product_rule))
        self.wait()
        self.play(ReplacementTransform(product_rule, up))
        self.play(Write(dhdt))
        self.wait()
        self.play(Write(simplified))


class dA(Scene):


class Credits(Scene):
    def construct(self):
        gh = Text("Source code for animations: \n"
                  "github.com/canisli/Kepler")
        self.play(Write(gh))
