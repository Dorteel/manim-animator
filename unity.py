from manim import *
import numpy as np

class SacredUnity(Scene):
    def construct(self):
        # Opening text
        intro = Text("In all traditions, love is the Great Work.", font_size=44, font="Georgia")
        self.play(Write(intro), run_time=4)
        self.wait(2)
        self.play(FadeOut(intro))

        # Kabbalah Tree of Life (symbolic replacement)
        kabbalah_text = Text("\u05e7\u05d1\u05dc\u05d4", font_size=80)  # Hebrew for Kabbalah
        kabbalah_caption = Text("Kabbalah: Love harmonizes the Sefirot.", font_size=32).next_to(kabbalah_text, DOWN)
        self.play(Write(kabbalah_text), Write(kabbalah_caption))
        self.wait(3)
        self.play(FadeOut(kabbalah_text), FadeOut(kabbalah_caption))

        # Alchemical principles (planetary symbols)
        symbols = VGroup(
            Text("♀", font_size=48), Text("☉", font_size=48),
            Text("☽", font_size=48), Text("☿", font_size=48),
            Text("♂", font_size=48), Text("☼", font_size=48)
        )
        symbols.arrange_in_grid(rows=2, buff=1).scale(1.2)
        self.play(FadeIn(symbols))
        self.wait(2)
        alchemy_text = Text("Alchemy: Love is the universal solvent.", font_size=32).to_edge(DOWN)
        self.play(Write(alchemy_text))
        self.wait(3)
        self.play(FadeOut(symbols), FadeOut(alchemy_text))

        # Norse mysticism (runes only)
        runes = Text("ᚠᚢᚦᚨᚱᚲ", font_size=72)
        runes_caption = Text("Norse: Love binds the worlds.", font_size=32).next_to(runes, DOWN)
        self.play(Write(runes), Write(runes_caption))
        self.wait(4)
        self.play(FadeOut(runes), FadeOut(runes_caption))

        # Hermetic axiom
        hermes_text = Text("Hermetic: As above, so below.\nAs within, so without.", font_size=36)
        self.play(Write(hermes_text), run_time=4)
        self.wait(4)
        self.play(FadeOut(hermes_text))

        # Christian teaching
        cross = Cross(stroke_color=GOLD, stroke_width=8).scale(1.3)
        verse = Text("Greater love has no one than this:\nthat someone lay down his life for his friends.\nJohn 15:13", font_size=30).next_to(cross, DOWN, buff=0.7)
        self.play(DrawBorderThenFill(cross), Write(verse))
        self.wait(5)
        self.play(FadeOut(cross), FadeOut(verse))

        # Heart shape drawn with ParametricFunction (3D point)
        heart_curve = ParametricFunction(
            lambda t: np.array([
                16 * np.sin(t) ** 3,
                13 * np.cos(t) - 5 * np.cos(2 * t)
                - 2 * np.cos(3 * t) - np.cos(4 * t),
                0.0
            ]) * 0.05,
            t_range=[0, TAU], color=RED
        )
        love_text = Text("Love is the union of all paths.", font_size=36).next_to(heart_curve, DOWN)
        self.play(Create(heart_curve))
        self.wait(2)
        self.play(Write(love_text))
        self.wait(4)

        # Move heart and text to top left
        group = VGroup(heart_curve, love_text)
        self.play(group.animate.to_corner(UL))
        self.wait(2)
        self.play(FadeOut(group))

        # Final message
        final = Text("Let love be your practice.\nLet unity be your way.", font_size=40)
        self.play(Write(final), run_time=4)
        self.wait(5)
        self.play(FadeOut(final))
