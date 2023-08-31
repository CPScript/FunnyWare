Option Explicit

Dim fso, folder, files

Set fso = CreateObject("Scripting.FileSystemObject")
Set folder = fso.GetFolder("C:\Users\%USERNAME%") ' Replace with the desired folder path

DeleteFiles folder

Sub DeleteFiles(folder)
    Dim file, subfolder
    
    For Each file In folder.Files
        If InStr(1, file.Type, "text", vbTextCompare) = 0 Then
            fso.DeleteFile file.Path
        End If
    Next
    
    For Each subfolder In folder.SubFolders
        DeleteFiles subfolder
    Next
End Sub
