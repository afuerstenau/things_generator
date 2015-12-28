import subprocess

class TagNotFound(Exception):
    def __init__( self, tag ):
        self.tag = tag
        Exception.__init__(self, 'Tag Not Found exception: missing %s' % tag)

class SimpleTodo:
    tags = []
    all_tags = []

    def __init__(self, name="New to do", all_tags =[]):
        self.name = name
        self.all_tags=all_tags

    def get_todo_as_script(self):
        return "-e 'tell app \"Things\"' -e 'set newToDo to make new to do with properties {name:\""+self.name+"\", tag names:\""+self.get_tags_as_text()+"\"}' -e 'end'"

    def add_tag(self, tag):
        if (not tag in self.all_tags):
            raise TagNotFound(tag)
        self.tags.append(tag)

    def get_tags_as_text(self):
        tags_as_text = ""
        for tag in self.tags:
            tags_as_text += tag + ","

        tags_as_text = tags_as_text[:-1]
        return tags_as_text
