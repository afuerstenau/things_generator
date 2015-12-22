import os
class Scriptrunner:

    def __init__(self, script):
        self.script = script

    def run_script(self):
        scriptcall = "osascript " + self.script
        print("Scriptcall: ", scriptcall)
        return os.system(scriptcall)
