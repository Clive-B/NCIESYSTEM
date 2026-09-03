param(
    [string]$InputPath = "C:\Users\codro\Desktop\NCIE\NCIE-001_Master_PRD_v1_2_PRODUCTION_READY.docx",
    [string]$OutputPath = "C:\Users\codro\Desktop\NCIE\NCIE-001_Master_PRD_v1_2_PRODUCTION_READY.pdf"
)

$word = $null
$document = $null
try {
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $word.DisplayAlerts = 0
    $document = $word.Documents.Open($InputPath, $false, $true)
    Write-Output "stage=open"
    $document.ExportAsFixedFormat($OutputPath, 17)
    Write-Output "stage=final_export_complete"
    Write-Output "pdf=$OutputPath"
}
finally {
    if ($null -ne $document) { $document.Close($false) }
    if ($null -ne $word) { $word.Quit() }
}
