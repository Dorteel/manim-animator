from manim import *

# Utility: Create and display a title
def display_title(scene: Scene, text: str, font_size: int = 48, duration: float = 2):
    title = Text(text, font_size=font_size)
    scene.play(Write(title))
    scene.wait(duration)
    scene.play(FadeOut(title))

# Utility: Add a subtitle to the bottom of the screen

def add_subtitle(scene: Scene, text: str, font_size: int = 24) -> Mobject:
    subtitle = Text(text, font_size=font_size).to_edge(DOWN)
    scene.play(FadeIn(subtitle))
    return subtitle

# Utility: Animate the appearance of a group of Mobjects
def fade_in_group(scene: Scene, group: VGroup, duration: float = 2):
    scene.play(FadeIn(group), run_time=duration)

# Utility: Connect a list of points with Lines
def connect_points(points: list[list[float]]) -> VGroup:
    lines = VGroup()
    for i in range(len(points) - 1):
        lines.add(Line(points[i], points[i + 1]))
    return lines

# Utility: Add numbered labels to a list of positions
def add_numbered_labels(scene: Scene, positions: list[list[float]], font_size: int = 24) -> VGroup:
    labels = VGroup()
    for i, pos in enumerate(positions):
        label = Text(str(i + 1), font_size=font_size).move_to([pos[0], pos[1], pos[2] + 0.1])
        labels.add(label)
    scene.play(FadeIn(labels))
    return labels

# Utility: Load and position an image
def import_image(filename: str, scale: float = 1.0, position: list[float] = None) -> Mobject:
    img = ImageMobject(filename).scale(scale)
    if position:
        img.move_to(position)
    return img

# Utility: Create a pulsing effect for any Mobject
def pulse(scene: Scene, mobject: Mobject, scale_factor: float = 1.2, run_time: float = 0.5, repetitions: int = 3):
    animations = [
        mobject.animate.scale(scale_factor),
        mobject.animate.scale(1 / scale_factor)
    ]
    for _ in range(repetitions):
        for anim in animations:
            scene.play(anim, run_time=run_time)

# Utility: Rotate a group around a point
def rotate_around(scene: Scene, group: VGroup, angle: float, about_point: list[float], run_time: float = 2):
    scene.play(Rotate(group, angle=angle, about_point=about_point), run_time=run_time)

# Utility: Display a poem line by line with font variation and fit lines to screen
def show_poem_with_fonts(scene: Scene, lines: list[str], fonts: list[str], font_size: int = 32, line_spacing: float = 0.6):
    poem_group = VGroup()
    for i, line in enumerate(lines):
        text = Text(line, font_size=font_size, font=fonts[i % len(fonts)])
        text.next_to(poem_group[-1], DOWN, buff=line_spacing) if poem_group else text.to_edge(UP)
        poem_group.add(text)

    for text in poem_group:
        scene.play(Write(text))
        scene.wait(0.5)

    scene.wait(2)
    scene.play(FadeOut(poem_group))

# Demo scene to showcase utilities
class UtilsDemo(Scene):
    def construct(self):
        display_title(self, "Utility Function Demo")
        subtitle = add_subtitle(self, "Demoing various utilities")

        points = [[-3, 0, 0], [-1, 1, 0], [1, -1, 0], [3, 0, 0]]

        nodes = VGroup()
        for i, p in enumerate(points):
            circle = Circle(radius=0.3, color=BLUE, fill_opacity=1).move_to(p)
            text = Text(f"Node{i+1}", font_size=18).move_to(p)
            node = VGroup(circle, text)
            nodes.add(node)

        fade_in_group(self, nodes)
        lines = connect_points(points)
        self.play(Create(lines))
        self.wait(1)
        self.play(FadeOut(nodes), FadeOut(lines), FadeOut(subtitle))

        display_title(self, "Image Import Demo")
        subtitle = add_subtitle(self, "Image moves and scales")
        image = import_image("peppermint-butler.jpg", scale=1.5)
        self.play(FadeIn(image))
        self.wait(1)
        self.play(image.animate.scale(0.5).to_corner(UL))
        self.wait(1)
        self.play(FadeOut(image), FadeOut(subtitle))

        display_title(self, "Pulse Animation Demo")
        subtitle = add_subtitle(self, "Simple pulsing effect")
        pulse_circle = Circle(radius=0.5, color=YELLOW, fill_opacity=0.8)
        self.play(FadeIn(pulse_circle))
        pulse(self, pulse_circle)
        self.play(FadeOut(pulse_circle), FadeOut(subtitle))

        display_title(self, "Rotation Demo")
        subtitle = add_subtitle(self, "Rotate objects around a point")
        rot_group = VGroup(
            Square(side_length=1, color=GREEN).shift(LEFT),
            Square(side_length=1, color=RED).shift(RIGHT)
        )
        self.play(FadeIn(rot_group))
        rotate_around(self, rot_group, angle=PI/2, about_point=[0, 0, 0])
        self.wait(2)
        self.play(FadeOut(subtitle))

        display_title(self, "Poem in Fonts")
        subtitle = add_subtitle(self, "Each line uses a different font")
        poem_lines = [
            "The sky above was deep and blue,",
            "The grass beneath a crystal hue,",
            "The breeze it hummed a gentle song,",
            "And time itself flowed right along."
        ]
        poem_fonts = ["Arial", "Comic Sans MS", "Courier New", "Times New Roman"]
        show_poem_with_fonts(self, poem_lines, poem_fonts)
        self.play(FadeOut(subtitle))
