import unittest
from config import config
from ok.test.TaskTestCase import TaskTestCase
from src.task.AutoCombatTask import AutoCombatTask

config['debug'] = True


def return_true():
    return True


class TestLevitator(TaskTestCase):
    task_class = AutoCombatTask
    config = config

    def test_levi(self):
        self.task.do_reset_to_false()
        self.set_image('tests/images/in_combat.png')
        self.assertTrue(self.task.ensure_leviator())

    def test_levi2(self):
        self.task.do_reset_to_false()
        self.set_image('tests/images/in_combat3.png')
        self.assertTrue(self.task.ensure_leviator())


if __name__ == '__main__':
    unittest.main()
