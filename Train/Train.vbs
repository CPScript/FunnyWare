' Replace this with the path to your train sound MP3 file
trainSoundPath = "extra\train.mp3"

Set oShell = CreateObject("WScript.Shell")

' Function to change a system sound
Sub ChangeSound(eventAlias)
    oShell.RegWrite "HKCU\AppEvents\Schemes\Apps\.Default\" & eventAlias & "\.Current", trainSoundPath, "REG_SZ"
End Sub

' List of sound events to change
soundEvents = Array("SystemAsterisk", "SystemExclamation", "SystemQuestion", "SystemStart", "SystemExit", "SystemHand")

' Change each sound event to the train sound
For Each eventAlias In soundEvents
    ChangeSound eventAlias
Next

WScript.Echo "System sounds changed to play the train sound MP3."
