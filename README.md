## Nolan Terminal Helper
Nolan terminal help a tool for fixing our worngs, let me explain about it, well seeing you always in your terminal running bad command, for example `la,cleat,helm' all of them a mistake because maybe you fast type or some other thing but this is tool help to our! when we run a bad command so that showing us a error **No command a found, did you mean...** this is very bad and now NTH saying "do you think this commnd needing to be save? Yes/no" if you answer **yes** we went next step,  it is saying "write it correctly" and yours answer it and in the nexts time even writing wrong, tool somehow running by defaulty correct command! , and now else if what that our answer no? well simply it is commnd don't needing something and running default

### how it works
Very simple and easy without memory leaking! In yours terminal bashrc, it added this part of code:
```bash
command_not_found_handle() {
    python /usr/local/bin/nth/nth.py "$@"
}
```
now somehow running python code, for more understanding please reading the code.
and next step it is running by auto and closed

### examples

```bash
# in default
#~: la
#No command la found, did you mean.....

#by nth
#~: la
#do you this command is wrongs(y/n): y
#Please write corecct command: ls
#~: la
# myfile2 myfile2
```

### installing
1. clone it and install

```bash
git clone https://github.com/theNolanG/NolanTerminalHelp-NTH.git

python install.py
```

#### contributor
yours can contributor in the project! and we can better than this and upgrades, yours pull request accepting. thank

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

