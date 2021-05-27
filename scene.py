from manim import *
# from numpy import product

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

class Title(Scene):
    def construct(self):
        title = Text("Kepler's 2nd Law Derivation", color=BLUE).scale(1.3)
        self.play(Write(title))
        self.wait(5)


class FirstLaw(Scene):
    def construct(self):
        self.play(GrowFromCenter(ellipse))
        self.add(planet)
        self.play(Transform(planet, planet2))
        self.add(sun)
        self.play(Transform(sun, sun2))
        self.play(MoveAlongPath(planet, ellipse), run_time=7,
                  rate_func=rate_functions.ease_in_out_cubic)
        self.wait(5)


class SecondLaw(Scene):
    def construct(self):
        self.play(GrowFromCenter(ellipse))
        self.add(planet)
        self.play(Transform(planet, planet2))
        self.add(sun)
        self.play(Transform(sun, sun2))
        line = get_line(planet, sun)
        line.add_updater(
            lambda mob: mob.become(get_line(planet, sun))
        )
        self.add_foreground_mobjects(planet)
        self.add(line)
        self.play(MoveAlongPath(planet, ellipse), run_time=7,
                  rate_func=rate_functions.ease_in_out_cubic)
        # animate diff intervals?
        self.wait(5)


class ThirdLaw(Scene):
    def construct(self):
        equation = MathTex(
            "T^2=\\frac{4\\pi^2}{GM}a^3"
        )
        self.play(Write(equation))
        self.wait(5)


class NewtonSecondLaw(Scene):
    def construct(self):
        title = Title("Newton's Second Law of Motion")

        equation = MathTex(
            "\\vec{F}_{\\textrm{net}}=m\\vec{a}"
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
            "\\vec{F}=-\\frac{Gm_1m_2}{r^2}\\mathbf{\hat{r}}"
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
        self.wait(5)
        self.play(Write(equation), Write(G), GrowFromCenter(m1),
                  GrowFromCenter(m2), Write(m1_label), Write(m2_label))
        self.wait(5)
        self.play(GrowArrow(m1_force), GrowArrow(m2_force))
        self.wait(5)


class SolveAcceleration(Scene):
    def construct(self):
        equation = MathTex(
            "F=ma=-\\frac{GmM}{r^2}\\mathbf{\\hat{r}}"
        )
        acceleration = MathTex(
            "a=-\\frac{GM}{r^2}\\mathbf{\\hat{r}}"
        )
        self.play(Write(equation))
        self.wait(10)
        self.play(ReplacementTransform(equation, acceleration))
        self.wait(5)


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
        ).shift(UP*1.5)
        self.play(Write(product_rule))
        self.wait(10)
        self.play(ReplacementTransform(product_rule, up))
        self.play(Write(dhdt))
        self.wait(10)
        self.play(Write(simplified))
        self.wait(5)


class dA(Scene):
    def construct(self):
        diagram = ImageMobject("assets/short_sweep.jpg")
        diagram.scale(0.7)
        # diagram.to_edge(RIGHT, buff=1)
        self.play(FadeIn(diagram))
        dTheta = MathTex(
            "d\\theta"
        ).shift(np.array([-2, -1.4, 0]))
        rdTheta = MathTex(
            "\\approx{rd\\theta}"
        ).shift(np.array([1.5, 1.4, 0]))
        approxR = MathTex(
            "\\approx{r}"
        ).shift(np.array([-1.4, 0.5, 0]))
        r = MathTex(
            "r"
        ).shift(np.array([0, -1, 0]))
        self.wait()
        self.play(Write(dTheta))
        self.wait(5)
        self.play(Write(r))
        self.play(Write(rdTheta))
        self.wait(10)
        self.play(Write(approxR))
        self.wait(10)

        dA = MathTex(
            "dA=\\frac{1}{2}r^2d\\theta"
        ).shift(np.array([4, -1, 0]))
        dAdt = MathTex(
            "\\frac{dA}{dt}=\\frac{1}{2}r^2\\frac{d\\theta}{dt}"
        ).shift(np.array([4, -1, 0]))
        Adot = MathTex(
            "\\dot{A}=\\frac{1}{2}r^2\\dot{\\theta}"
        ).shift(np.array([4, -1, 0]))

        self.play(Write(dA))
        self.wait(10)
        self.play(ReplacementTransform(dA, dAdt))
        self.wait(10)
        self.play(ReplacementTransform(dAdt, Adot))
        self.wait(5)


class rxv(Scene):
    def construct(self):
        r = MathTex(
            "\\vec{r}=r\\cos\\theta\\mathbf{\hat{i}}+r\\sin\\theta\\mathbf{\\hat{j}}"
        )
        r_up = MathTex(
            "\\vec{r}=r\\cos\\theta\\mathbf{\\hat{i}}+r\\sin\\theta\\mathbf{\\hat{j}}"
        ).shift(UP)
        v = MathTex(
            """
            \\vec{v}=\\dot{\\vec{r}}=
            (\\dot{r}\\cos\\theta-r\\sin\\theta\\dot{\\theta})\\mathbf{\\hat{i}} +
            (\\dot{r}\\sin\\theta+r\\cos\\theta\\dot{\\theta})\\mathbf{\\hat{j}}
            """
        )
        g = Group(r_up, v)
        self.play(Write(r))
        self.wait(10)
        self.play(ReplacementTransform(r, r_up))
        self.play(Write(v))
        self.wait(10)
        gcopy = g.copy().shift(UP)
        self.play(ReplacementTransform(g, gcopy))
        self.wait(10)
        cross_product = Matrix([
            ["\\mathbf{\\hat{i}}", "\\mathbf{\\hat{j}}", "\\mathbf{\\hat{k}}"],
            ["\\vec{r}_x", "\\vec{r}_y", "0"],
            ["\\vec{v}_x", "\\vec{v}_y", "0"]
        ]).shift(DOWN*0.6 + RIGHT*2.5).scale(0.6)
        det = get_det_text(cross_product, initial_scale_factor=0.8)
        rxv = MathTex(
            """
            \\vec{h} = \\vec{r}\\times\\vec{v} =
            """
        ).shift(LEFT + DOWN*0.5)

        self.play(Write(rxv))
        self.play(Write(cross_product), Write(det))
        g2 = Group(rxv, det, cross_product)
        simplify = MathTex(
            """
            =[(r\\cos\\theta)(\\dot{r}\\sin\\theta+r\\cos\\theta\\dot{\\theta})-
            (r\\sin\\theta)(\\dot{r}\\cos\\theta-r\\sin\\theta\\dot{\\theta})]
            \\mathbf{\\hat{k}}
            """
        )
        simplify2 = MathTex(
            """
            =[r\\dot{r}\\cos\\theta+r^2\\cos^2(\\theta)\\dot{\\theta} - r\\dot{r}\\cos\\theta+r^2\\sin^2(\\theta)\\dot{\\theta}
            ]\\mathbf{\\hat{k}}
            """
        )
        simplify3 = MathTex(
            """
            =[r^2\\dot{\\theta}(\\sin^2\\theta+\\cos^2\\theta)]
            \\mathbf{\\hat{k}}
            """
        )
        final = MathTex(
            "\\vec{h}=r^2\\dot{\\theta}\\mathbf{\\hat{k}}"
        )
        self.play(*[FadeOut(obj) for obj in gcopy],
                  ReplacementTransform(g2, g2.copy().to_edge(UP).shift(DOWN)))
        self.wait(10)
        self.play(Write(simplify))
        self.wait(10)
        self.play(ReplacementTransform(simplify, simplify2))
        self.wait(10)
        self.play(ReplacementTransform(simplify2, simplify3))
        self.wait(10)
        self.play(ReplacementTransform(simplify3, final))
        self.wait(5)


class Proved(Scene):
    def construct(self):
        Adot = MathTex(
            "\\dot{A}=\\frac{1}{2}r^2\\dot{\\theta}"
        )
        h = MathTex(
            "\\vec{h}=r^2\\dot{\\theta}\\mathbf{\\hat{k}}"
        ).shift(DOWN*1.5)
        self.play(Write(Adot))
        self.wait(5)
        self.play(Write(h))
        self.wait(5)
        sub = MathTex(
            "\\dot{A}=\\frac{h}{2}=\mathrm{constant}"
        )
        self.play(ReplacementTransform(Adot, sub))
        self.wait(5)


class test(Scene):
    def construct(self):
        x = MathTex("x=5")
        self.play(Write(x))
        self.play(*[FadeOut(obj) for obj in x])


class Credits(Scene):
    def construct(self):
        gh = Text("Source code for animations: \n"
                  "github.com/canisli/Kepler")
        self.play(Write(gh))
        self.wait(5)
