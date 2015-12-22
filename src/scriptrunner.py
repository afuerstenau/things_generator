import subprocess

class Scriptrunner:

    def __init__(self, script):
        self.script = script

    def run_script(self):
        scriptcall = "osascript " + self.script
        process = subprocess.Popen([scriptcall], stdout=subprocess.PIPE, shell=True)
        result = process.stdout.read()
        print ("result: ", result)
        if (result.decode("utf-8").startswith("to do id")):
            return True
        return False
