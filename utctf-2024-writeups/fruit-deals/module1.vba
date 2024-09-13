
Sub FillWithRandomBase64()
    Dim ws As Worksheet
    Dim rng As Range
    Dim i As Long
    Dim base64String As String
    
    ' Set worksheet
    Set ws = ThisWorkbook.Sheets("Sheet2") ' Change "Sheet1" to your sheet name
    
    ' Set range where you want to fill the base64 strings
    Set rng = ws.Range("A1:AA100") ' Change "A1:A100" to your desired range
    
    ' Clear previous content
    rng.ClearContents
    
    ' Seed the random number generator
    Randomize
    
    ' Loop through each cell in the range and fill with random base64 strings
    For i = 1 To rng.Cells.Count
        base64String = GenerateRandomBase64()
        rng.Cells(i).Value = base64String
    Next i
End Sub

Function GenerateRandomBase64() As String
    Dim base64Chars As String
    Dim i As Integer
    Dim base64String As String
    
    ' Define Base64 characters
    base64Chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    ' Generate random Base64 string
    For i = 1 To 8 ' Generates an 8-character Base64 string (which would correspond to 6 bytes of data)
        base64String = base64String & Mid(base64Chars, Int((Len(base64Chars) * Rnd) + 1), 1)
    Next i
    
    GenerateRandomBase64 = base64String
End Function
