import os
import sys
import json

class NTH:
    def __init__(self):

        self.bashRcCommand="""
command_not_found_handle() {
    python /usr/local/bin/nth/nth.py "$@"
}
            """
        self.way="/usr/local/bin/"
        self.database={"expection":[],"bashrcbackup":""}
    def install(self):
        if not os.path.exists(self.way+"nth"):
            try:
                os.mkdir(self.way+"nth")
                print("created nth directory !")
                self._bashrc()
                print("added commands in bashrc file")
                with open(self.way+"nth/"+"database.json","w") as file:
                    json.dump(self.database,file)
                    print("created json database file !")
                    file.close()
                os.system("cp nth.py "+self.way+"nth")
                print("copy nth python file to be "+self.way+"nth")
                print("Installed...")
                os.system("unset -f command_not_found_handle")
                print("Please run 'source .bashrc' in the user home\nReady for working.")
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
                with open(self.way+"nth/"+"database.json") as file:
                    self.database=json.load(file)
                    
                bashrcpath=os.path.expanduser("~/.bashrc")
                
                with open(bashrcpath,"w") as file:
                    file.write(str(self.database["bashrcbackup"]))
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
        return 0
    def _bashrc(self):
        bashrcPath=os.path.expanduser("~/.bashrc")
        with open(bashrcPath,"r") as file:
            self.database["bashrcbackup"]=str(file.read())
        with open(bashrcPath,"a") as file:
            file.write("#Nolan terminal help")
            file.write(self.bashRcCommand)
            return True


if __name__ == "__main__":
    nth=NTH()
    print("Nolan Terminal Help")
    print("1.Install\n2.Uninstall\n3.Reinstall\n4.Exit")
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
        elif answer == 3:
            nth.clear()
            nth.uninstall()
            nth.install()
            break
        else:
            break
            
        
