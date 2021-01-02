import subprocess
import time

counter = 0

while True:
    y = subprocess.check_output('powershell.exe Get-AppxPackage *NetopSolutions.NetopVisionStudent*')
    x = len(y)
    if x > 4:
        print("Programm erkannt wird deinstalliert!")
        subprocess.check_output('powershell.exe Get-AppxPackage *NetopSolutions.NetopVisionStudent* | Remove-AppxPackage')
        counter = counter+1
        print("Wurde Deinstalliert nun das ")
        print(counter)
        print("mal!")
    time.sleep(20)
