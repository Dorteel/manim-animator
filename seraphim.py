from manim import *
import shutil
print(shutil.which("manim"))

class SephirotAnimation(Scene):
    def construct(self):
        # Initial scattered positions
        initial_positions = [
            [0, 3, 0],            # Keter
            [-2, 2.5, 0], [2, 2.5, 0], # Binah, Chokhmah
            [-2.5, 0.5, 0], [2.5, 0.5, 0], # Gevurah, Chesed
            [0, 1, 0],            # Tiferet
            [-2, -1.5, 0], [2, -1.5, 0], # Hod, Netzach
            [0, -2, 0],           # Yesod
            [0, -3, 0]            # Malkuth
        ]

        # Final aligned positions (should match number of initial positions)
        aligned_positions = [
            [0, 3, 0],             # Keter
            [-1.5, 2, 0], [1.5, 2, 0],  # Binah, Chokhmah
            [-2, 1, 0], [0, 1, 0],      # Gevurah, Chesed
            [2, 1, 0],                 # Tiferet
            [-1.5, 0, 0], [1.5, 0, 0],  # Hod, Netzach
            [0, -1, 0],                # Yesod
            [0, -2, 0]                 # Malkuth
        ]

        # Create initial nodes
        nodes = VGroup(*[Dot(point=p, radius=0.15, color=BLUE) for p in initial_positions])

        # Initial wiggle animation
        self.play(Wiggle(nodes, scale_value=1.2, rotation_angle=0.05*PI), run_time=2)

        # Animation to align nodes
        self.play(*[node.animate.move_to(aligned_positions[i]) for i, node in enumerate(nodes)], run_time=3)

        # Add edges after alignment
        edges = VGroup(
            Line(aligned_positions[0], aligned_positions[1]),
            Line(aligned_positions[0], aligned_positions[2]),
            Line(aligned_positions[1], aligned_positions[3]),
            Line(aligned_positions[2], aligned_positions[5]),
            Line(aligned_positions[3], aligned_positions[4]),
            Line(aligned_positions[4], aligned_positions[5]),
            Line(aligned_positions[4], aligned_positions[6]),
            Line(aligned_positions[5], aligned_positions[7]),
            Line(aligned_positions[6], aligned_positions[8]),
            Line(aligned_positions[7], aligned_positions[8]),
            Line(aligned_positions[8], aligned_positions[9]),
        )

        # Fade in edges smoothly
        self.play(Create(edges), run_time=3)

        # Pause to display the final structure
        self.wait(2)
