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
    $word.Options.Pagination = $false
    $document = $word.Documents.Open($InputPath, $false, $false)

    if ($document.TablesOfContents.Count -gt 0) {
        for ($index = 1; $index -le $document.TablesOfContents.Count; $index++) {
            $document.TablesOfContents.Item($index).Update() | Out-Null
        }
    }
    foreach ($section in $document.Sections) {
        foreach ($header in $section.Headers) {
            if ($header.Exists -and $header.Range.Fields.Count -gt 0) {
                $header.Range.Fields.Update() | Out-Null
            }
        }
        foreach ($footer in $section.Footers) {
            if ($footer.Exists -and $footer.Range.Fields.Count -gt 0) {
                $footer.Range.Fields.Update() | Out-Null
            }
        }
    }
    $document.Save()
    $document.ExportAsFixedFormat($OutputPath, 17)
    Write-Output "pdf=$OutputPath"
}
finally {
    if ($null -ne $document) { $document.Close($false) }
    if ($null -ne $word) { $word.Quit() }
}
