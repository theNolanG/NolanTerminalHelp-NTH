#!/usr/bin/python3
import json
import sys
import os

class NTH:
    def __init__(self):
        self.path="/usr/local/bin/nth/"
        self.database={}
        self._loadDatabase()
    def _loadDatabase(self):
        with open(self.path+"database.json","r") as file:
            self.database=json.load(file)
            return None
    def _updateDatabase(self):
        with open(self.path+"database.json","w") as file:
            json.dump(self.database,file)
            return None

    def remove(self,word):
        try:
            self.database.pop(word)
            self._updateDatabase()
            return True
        except Exception as e:
            print(e)
            return False
    def save(self,corecct,wrong):
        if corecct == "" or corecct == " ":
            print("Answer is empty !")
            return False
        else:
            self.database[wrong]=corecct
            self._updateDatabase()
            return True
    def saveExpection(self,word):
        self.database["expection"].append(word)
        self._updateDatabase()
        return 0

    def runCommand(self,arg):
        os.system(self.getDatabase()[arg])
        return 0

    def getDatabase(self):
        return self.database

if __name__ == "__main__":
    arg=sys.argv
    nth=NTH()
    if arg[1] in nth.getDatabase()["expection"]:
        print("This command a expection")
        sys.exit()
    elif arg[1] in nth.getDatabase():
        nth.runCommand(arg[1])
    
    if arg[1] not in nth.getDatabase():
        answer=input("do you this command is wrongs(y/n): ")
        if answer.strip() == "y":
            corecct=input("Please write corecct command: ")
            wrong=arg[1]
            nth.save(corecct,wrong)
        else:
            nth.saveExpection(arg[1])

