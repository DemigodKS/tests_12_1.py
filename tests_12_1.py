from time import process_time_ns

from module12_1 import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner1 = Runner('Nik')
        for _ in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    def test_run(self):
        runner2 = Runner('Julia')
        for _ in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    def test_challenge(self):
        runner1 = Runner('Nik')
        runner2 = Runner('Julia')
        for _ in range(10):
            runner1.walk()
            runner2.run()
            if runner1.distance == runner2.distance:
                message = 'equal'
            else:
                message = 'not equal'
        self.assertNotEqual(runner1.distance, runner2.distance, message)

if __name__ == '__main__':
    unittest.main()



