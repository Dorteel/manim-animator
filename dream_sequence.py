from manim import *

class DreamSequence(Scene):
    def construct(self):
        # Title
        title = Text("a dream", font_size=64, font="Georgia")
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Moon rising
        moon = Circle(radius=0.5, color=WHITE, fill_opacity=0.9).shift(DOWN*3)
        self.play(FadeIn(moon))
        self.play(moon.animate.shift(UP*4), run_time=2)

        # Stars appear
        stars = VGroup(
            *[Dot(point=pos, radius=0.03, color=WHITE) for pos in [
                [-5, 2, 0], [-3, 3, 0], [-1, 2.5, 0], [1, 3.2, 0], [3, 2.8, 0], [5, 2.6, 0]
            ]]
        )
        self.play(FadeIn(stars))

        # A thought floats in
        thought = Text("Where do dreams begin?", font_size=36, font="Times New Roman")
        thought.set_color(BLUE)
        thought.shift(DOWN*2)
        self.play(Write(thought))
        self.wait(1.5)
        self.play(FadeOut(thought))

        # A shape morphs into another
        square = Square(side_length=1.5, color=TEAL, fill_opacity=0.6)
        square.shift(LEFT*2)
        circle = Circle(radius=0.75, color=PURPLE, fill_opacity=0.6)
        circle.shift(RIGHT*2)
        self.play(FadeIn(square, circle))
        self.wait(0.5)

        morph = square.copy().move_to(ORIGIN)
        self.play(Transform(morph, circle.copy().move_to(ORIGIN)), run_time=2)
        self.wait(1)

        # Fade all out, fade in text
        self.play(FadeOut(moon), FadeOut(stars), FadeOut(square), FadeOut(circle), FadeOut(morph))

        message = Text("a dream, forgotten", font_size=48, font="Courier New").shift(DOWN)
        self.play(Write(message))
        self.wait(2)
        self.play(FadeOut(message))
