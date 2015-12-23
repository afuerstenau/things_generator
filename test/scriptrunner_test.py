import unittest
from ..src.scriptrunner import Scriptrunner

class TestScriptrunner(unittest.TestCase):

    def test_run_script(self):
        scriptrunner = Scriptrunner("-e 'tell app \"Things\"' -e 'set newToDo to make new to do with properties {name:\"New to do\", tag names:\"test\", due date:current date}' -e 'end'")
        self.assertEqual(scriptrunner.run_script(), True)
