from manim import *

class Mystical(Scene):
    def construct(self):
        # Opening title
        title = Text("In the Beginning...", font_size=60, font="Georgia")
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Light emerging from darkness
        circle = Circle(radius=3, color=WHITE, fill_opacity=1)
        circle.set_fill(BLACK)
        self.add(circle)
        self.wait(1)

        light = Circle(radius=0.1, color=YELLOW, fill_opacity=1).move_to(ORIGIN)
        self.play(FadeIn(light))
        self.play(light.animate.scale(30), run_time=5)
        self.play(FadeOut(light))

        # Cross appears slowly
        cross = Cross(stroke_color=WHITE, stroke_width=6).scale(1.5)
        self.play(DrawBorderThenFill(cross), run_time=4)
        self.wait(2)

        # Cross fades to glowing golden
        glowing_cross = Cross(stroke_color=GOLD, stroke_width=6).scale(1.5)
        self.play(Transform(cross, glowing_cross), run_time=2)
        self.wait(1)

        # Bible verse fades in
        verse = Text("In Him was life, and the life was the light of men.\nJohn 1:4", font="Times New Roman", font_size=36)
        verse.next_to(cross, DOWN, buff=1.5)
        self.play(FadeIn(verse))
        self.wait(4)

        # A dove descends
        dove = SVGMobject("dove.svg").scale(0.5).to_edge(UP)
        dove.set_fill(WHITE, opacity=1).set_stroke(WHITE)
        self.play(FadeIn(dove))
        self.play(dove.animate.move_to(ORIGIN), run_time=3)
        self.wait(2)

        # Trinity symbolism - 3 glowing circles
        self.play(FadeOut(dove), FadeOut(cross), FadeOut(verse))

        trinity = VGroup(
            Circle(radius=1.2, color=BLUE, fill_opacity=0.1).shift(LEFT*2),
            Circle(radius=1.2, color=RED, fill_opacity=0.1).shift(RIGHT*2),
            Circle(radius=1.2, color=YELLOW, fill_opacity=0.1)
        )
        self.play(*[FadeIn(circ) for circ in trinity])
        self.wait(2)

        # Labels Father, Son, Spirit
        labels = VGroup(
            Text("Father", font_size=32).next_to(trinity[0], DOWN),
            Text("Son", font_size=32).next_to(trinity[1], DOWN),
            Text("Holy Spirit", font_size=32).next_to(trinity[2], UP)
        )
        self.play(FadeIn(labels))
        self.wait(4)

        self.play(FadeOut(trinity), FadeOut(labels))

        # Closing message
        end_message = Text("Glory be to the Father,\nand to the Son,\nand to the Holy Spirit.\nAs it was in the beginning,\nis now, and ever shall be.\nAmen.", font_size=36, font="Georgia")
        self.play(Write(end_message), run_time=5)
        self.wait(8)
        self.play(FadeOut(end_message))