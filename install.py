import os
import sys
import json

class NTH:
    def __init__(self):

        self.bashRcCommand="""
command_not_found_handle() {
    python /usr/local/bin/nth/nth.py $1 $2 $3 $4
}
            """
        self.way="/usr/local/bin/"
    def install(self):
        if not os.path.exists(self.way+"nth"):
            try:
                os.mkdir(self.way+"nth")
                print("created nth directory !")
                with open(self.way+"nth/"+"database.json","w") as file:
                    json.dump({},file)
                    print("created json database file !")
                    file.close()
                os.system("cp nth.py "+self.way+"nth")
                print("copy nth python file to be "+self.way)
                self._bashrc()
                print("added commands in bashrc file")
                print("Installed...")
                return True
            except Exception as e:
                print(e)
                os.system("rm -rf "+self.way+"nth")
                return False
        else:
            print("The nth installed.")
            return True
    def uninstall(self):
        try:
            if os.path.exists(self.way+"nth"):
                os.system("rm -rf "+self.way+"nth")
                print("The Nth uninstalled !")
                return True
            else:
                print("The Nth is not installed !")
                return False
        except Exception as e:
            print(e)
            return False
    def clear(self):
        os.system("clear")
        returnb0
    def _bashrc(self):
        bashrcPath=os.path.expanduser("~/.bashrc")
        with open(bashrcPath,"a") as file:
            file.write("#Nolan terminal help")
            file.write(self.bashRcCommand)
            return True


if __name__ == "__main__":
    nth=NTH()
    print("Nolan Terminal Help")
    print("1.Install\n2.Uninstall\n3.exit")
    while True:
        answer=int(input("Enter number: "))
        if answer == 1:
            nth.clear()
            nth.install()
            break
        elif answer == 2:
            nth.clear()
            nth.uninstall()
            print("!! PLEASE MANUAL REMOVE PART CODE FROM BASHRC !!")
            break
        else:
            nth.clear()
            sys.exit()
            
        
