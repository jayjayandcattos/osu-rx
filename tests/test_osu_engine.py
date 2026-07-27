import os
import tempfile
import unittest

from osu import OsuRelaxCheatsEngine


class TestOsuRelaxCheatsEngine(unittest.TestCase):
    def test_parses_simple_beatmap(self):
        content = """[General]

[TimingPoints]
0,100,4,0,0,50,1,0

[HitObjects]
256,192,1000,1,0,0:0:0:0:
128,192,2000,1,0,0:0:0:0:
"""

        with tempfile.NamedTemporaryFile("w", suffix=".osu", delete=False, encoding="utf-8") as handle:
            handle.write(content)
            path = handle.name

        try:
            engine = OsuRelaxCheatsEngine(path)
            self.assertEqual(engine.slider_multiplier, 1.4)
            self.assertEqual(len(engine.timing_points), 1)
            self.assertEqual(engine.timing_points[0]["beat_length"], 100)
            self.assertEqual(len(engine.hit_objects), 2)
            self.assertFalse(engine.hit_objects[0]["is_slider"])
        finally:
            os.unlink(path)


if __name__ == "__main__":
    unittest.main()
