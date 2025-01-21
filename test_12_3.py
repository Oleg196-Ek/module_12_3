import unittest
from module_12_2 import Runner, Tournament

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        walker = Runner('Антон')
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50) # при замене значения 50 на 90

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_run(self):
        walker = Runner('Alex')
        for i in range(10):
            walker.run()
        self.assertEqual(walker.distance, 100)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        run1 = Runner('Елена')
        run2 = Runner('Екатерина')
        for i in range(10):
            run1.walk()
            run2.run()
        self.assertNotEqual(run1.distance, run2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f'\t{key}: {value.name}')

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_turn1(self):
        turn_1 = Tournament(90, self.runner_1, self.runner_3)
        result = turn_1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Тест первого раунда'] = result

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_turn2(self):
        turn_2 = Tournament(90, self.runner_2, self.runner_3)
        result = turn_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Тест второго раунда'] = result

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_turn3(self):
        turn_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = turn_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Тест третьего раунда'] = result

    if __name__ == '__main__':
        unittest.main()