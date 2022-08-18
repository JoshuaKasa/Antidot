# **Antidot 💉**
Antidot is a malware written in Python, C++ and Assembly, it is very destructive so be careful on how you use it.</br>
Antidot is a very particuar malware, since by various steps it can be "disarmed", that's why it is called Antidot (antidote).

# ***How it works 📄***
Antidot is divided in 5 parts (the person who installs the malware will not install all 5 of the files, they will be wrapped in a single .zip file), each part serve a useful purpose.</br>
The main file, ``AntidotMain.pyw`` is the one who controls the whole Antidot system, it starts the ``AntidotTimer.pyw`` and is used for checking if ``AntidotCheck.pyw`` is still running.</br>
In fact, ``AntidotMain.pyw`` and ``AntidotCheck.pyw`` create a loop in which none of them can be closed, because that will cause the activation of ``AntidotDestroy.cpp`` and ``AntidotDestroy.asm``.</br>
``AntidotTimer.pyw`` is the file used for checking the time, in fact Antidot works by giving the user 3 minutes to try and deactivate the virus, this 3 minutes are checked by the timer file. Here you can actually find a way for "disarming" the virus, probably the safer and esiest one (NOTE THAT THIS IS DONE INTENTIONALLY).</br>
For the destruction, Antidot uses a simple MBR (Master Booting Record) overwriting method, it works by replacing the 512 MBR bytes with some random ones. The destruction will start when 1 of this 3 condtions are true:
```
The 3 minutes timer has reached 0.
AntidotMain.pyw is not running.
AntidotCheck.cpp is not running
```

## ***Libraries used 📚***
Python:
```
psutil
os
subprocess
win32api
time
```
C++:
```
windows.h
tlhelp.h
tchar.h
iostrean
```

# **Notes 🗒️**
Antidot has to be runned with administrator rights for working properly, and it is not configured to run (making it run is vey simple and everyone with basic Python knowledge </br>
can do it, but i haven't configured it because this project is for ⚠️ EDUCATIONAL PURPORSES ONLY ⚠️).

**⛔ WARNING, DON'T USE THIS AGAINST ANYONE AND I'M NOT RESPONSIBLE FOR ANYTHING THAT HAPPENS TO YOU OR ANYONE ELSE, I SPECIFY IT AGAIN THI IS FOR EDUCATIONAL PURPORSES ONLY ⛔**
