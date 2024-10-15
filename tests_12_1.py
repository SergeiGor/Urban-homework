import unittest
import runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        r_walk = runner.Runner("Иван")
        for i in range(10):
            r_walk.walk()
        self.assertEqual(r_walk.distance, 50)

    def test_run(self):
        r_run = runner.Runner("Иван")
        for i in range(10):
            r_run.run()
        self.assertEqual(r_run.distance, 100)

    def test_challenge(self):
        r_1 = runner.Runner("Василий")
        r_2 = runner.Runner("Николай")
        for i in range(10):
            r_1.walk()
            r_2.run()
        self.assertNotEqual(r_1.distance, r_2.distance)

if __name__ == "__main":
        unittest.main