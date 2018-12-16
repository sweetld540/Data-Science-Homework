VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "ThisWorkbook"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = True
Sub VBAHomeworkFinal()


Dim totalStockVolume As Double
Dim rowCounter As Integer

rowCounter = 2
totalStockVolume = 0


For Each ws In Worksheets

ws.Cells(1, 9).Value = "Ticker"
ws.Cells(1, 10).Value = "Total Stock Volume"

lastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row

    For i = 2 To lastRow

        If ws.Cells(i, 1).Value = ws.Cells(i + 1, 1).Value Then

        totalStockVolume = ws.Cells(i, 7).Value + totalStockVolume
    

        ElseIf ws.Cells(i, 1).Value <> ws.Cells(i + 1, 1).Value Then
    
        totalStockVolume = ws.Cells(i, 7).Value + totalStockVolume

        ws.Cells(rowCounter, 10).Value = totalStockVolume
       
        ws.Cells(rowCounter, 9).Value = ws.Cells(i, 1)
       
        rowCounter = rowCounter + 1
       
       totalStockVolume = 2
       
    
       
    End If
    
    Next i
    
    rowCounter = 2

    
Next ws



End Sub

