import unittest
from ..src.simple_todo import SimpleTodo
from ..src.simple_todo import TagNotFound

class TestSimpleTodo(unittest.TestCase):

    def test_simple_todo(self):
        simple_todo = SimpleTodo()
        self.assertEqual(simple_todo.get_todo_as_script(), "-e 'tell app \"Things\"' -e 'set newToDo to make new to do with properties {name:\"New to do\", tag names:\"\"}' -e 'end'")

    def test_simple_todo_with_name(self):
        simple_todo = SimpleTodo("write meeting notes")
        self.assertEqual(simple_todo.get_todo_as_script(), "-e 'tell app \"Things\"' -e 'set newToDo to make new to do with properties {name:\"write meeting notes\", tag names:\"\"}' -e 'end'")

    def test_simple_todo_with_tag(self):
        simple_todo = SimpleTodo("write meeting notes", all_tags=["@Home"])
        simple_todo.add_tag("@Home")
        self.assertEqual(simple_todo.get_todo_as_script(), "-e 'tell app \"Things\"' -e 'set newToDo to make new to do with properties {name:\"write meeting notes\", tag names:\"@Home\"}' -e 'end'")

    def test_simple_todo_with_unknown_tag(self):
        simple_todo = SimpleTodo("write meeting notes")
        with self.assertRaises(TagNotFound):
          simple_todo.add_tag("@Home2")
