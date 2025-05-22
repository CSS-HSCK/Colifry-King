README for Game Blocker
What is this?
This is a website blocker program that stops access to popular online gaming sites by modifying the Windows hosts file.

Why use it?
To help keep students focused during school hours.

Prevents playing games on Chrome or other browsers during breaks.

Required by the school principal to maintain discipline.

How to use?
Run the blocker program as Administrator

Right-click on blocker_watchdog.exe

Select Run as administrator
This is necessary so the program can modify the system’s hosts file.

The blocker will immediately start blocking the listed gaming sites.

To stop blocking, you will need to remove the entries manually or run an unblocker (if available).

List of blocked websites includes:
coolmathgames.com, poki.com, miniclip.com, y8.com, roblox.com, and many more popular gaming sites.

Important Notes
Make sure to keep the program running for continuous blocking.

If you restart your computer, run the blocker again with administrator rights.

Only share this program with permission from your school.



Step-by-step: Create a Scheduled Task to run your blocker on startup with admin rights
Open Notepad and paste this PowerShell script:

powershell
Copy
Edit
$action = New-ScheduledTaskAction -Execute "C:\Users\youruser\OneDrive\Desktop\printer-hostblock\dist\blocker_watchdog.exe"
$trigger = New-ScheduledTaskTrigger -AtLogOn
$principal = New-ScheduledTaskPrincipal -UserId "SYSTEM" -RunLevel Highest
$task = New-ScheduledTask -Action $action -Trigger $trigger -Principal $principal
Register-ScheduledTask -TaskName "GameBlocker" -InputObject $task -Force
Replace the path in -Execute with the full path to your built EXE file.

Save the file as create_blocker_task.ps1 (make sure extension is .ps1).

Run PowerShell as Administrator, then run:

powershell
Copy
Edit
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
.\create_blocker_task.ps1
This will create a scheduled task named GameBlocker that runs your blocker EXE as SYSTEM with highest privileges at every logon.
