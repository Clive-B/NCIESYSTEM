param(
    [string]$InputPath = "C:\Users\codro\Desktop\NCIE\NCIE-002_System_Architecture_Technical_Design_v0_4_PRODUCTION_READY.docx",
    [string]$OutputPath = "C:\Users\codro\Desktop\NCIE\NCIE-002_System_Architecture_Technical_Design_v0_4_PRODUCTION_READY.pdf"
)

$word = $null
$document = $null
try {
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $word.DisplayAlerts = 0
    $document = $word.Documents.Open($InputPath, $false, $false)
    foreach ($story in $document.StoryRanges) {
        $range = $story
        while ($null -ne $range) {
            if ($range.Fields.Count -gt 0) {
                $range.Fields.Update() | Out-Null
            }
            $range = $range.NextStoryRange
        }
    }
    $document.Repaginate()
    $pages = $document.ComputeStatistics(2)
    $document.Save()
    $document.ExportAsFixedFormat($OutputPath, 17)
    Write-Output "pages=$pages"
    Write-Output "pdf=$OutputPath"
}
finally {
    if ($null -ne $document) {
        $document.Close($false)
    }
    if ($null -ne $word) {
        $word.Quit()
    }
}
