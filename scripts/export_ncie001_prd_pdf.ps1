$InputPath = "C:\Users\codro\Desktop\NCIE\NCIE-001_Master_PRD_v1_3_IN_DEVELOPMENT.docx"
$OutputPath = "C:\Users\codro\Desktop\NCIE\NCIE-001_Master_PRD_v1_3_IN_DEVELOPMENT.pdf"

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0
try {
    $document = $word.Documents.Open($InputPath, $false, $false)
    try {
        $document.Repaginate()
        $pages = $document.ComputeStatistics(2)
        $document.Save()
        $document.ExportAsFixedFormat($OutputPath, 17)
        Write-Output "pages=$pages pdf=$OutputPath"
    }
    finally {
        $document.Close($false)
    }
}
finally {
    $word.Quit()
}
