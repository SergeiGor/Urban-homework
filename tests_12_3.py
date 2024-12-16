import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


# Декоратор для пропуска тестов, когда is_frozen == True
def skip_if_frozen(func):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        else:
            return func(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False  # Тесты не будут заморожены

    @skip_if_frozen
    def test_challenge(self):
        runner = Runner("Усэйн", speed=10)
        self.assertEqual(runner.speed, 10)

    @skip_if_frozen
    def test_run(self):
        runner = Runner("Андрей", speed=9)
        self.assertEqual(runner.speed, 9)

    @skip_if_frozen
    def test_walk(self):
        runner = Runner("Ник", speed=3)
        self.assertEqual(runner.speed, 3)

class TournamentTest(unittest.TestCase):
    is_frozen = True  # Тесты будут заморожены

    @skip_if_frozen
    def test_first_tournament(self):
        usain = Runner("Усэйн", speed=10)
        nick = Runner("Ник", speed=3)
        tournament = Tournament(90, usain, nick)
        results = tournament.start()
        self.assertEqual(list(results.values())[0].name, "Усэйн")

    @skip_if_frozen
    def test_second_tournament(self):
        andrey = Runner("Андрей", speed=9)
        nick = Runner("Ник", speed=3)
        tournament = Tournament(90, andrey, nick)
        results = tournament.start()
        self.assertEqual(list(results.values())[0].name, "Андрей")

    @skip_if_frozen
    def test_third_tournament(self):
        usain = Runner("Усэйн", speed=10)
        andrey = Runner("Андрей", speed=9)
        nick = Runner("Ник", speed=3)
        tournament = Tournament(90, usain, andrey, nick)
        results = tournament.start()
        self.assertEqual(list(results.values())[0].name, "Усэйн")


if __name__ == '__main__':
    unittest.main()
