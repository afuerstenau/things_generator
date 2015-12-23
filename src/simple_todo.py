import subprocess

class SimpleTodo:
    tags = []

    def __init__(self, name="New to do"):
        self.name = name

    def get_todo_as_script(self):
        return "-e 'tell app \"Things\"' -e 'set newToDo to make new to do with properties {name:\""+self.name+"\", tag names:\""+self.get_tags_as_text()+"\"}' -e 'end'"

    def add_tag(self, tag):
        self.tags.append(tag)

    def get_tags_as_text(self):
        tags_as_text = ""
        for tag in self.tags:
            tags_as_text += tag + ","

        tags_as_text = tags_as_text[:-1]
        return tags_as_text
