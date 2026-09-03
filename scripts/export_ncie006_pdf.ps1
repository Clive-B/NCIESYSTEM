param(
    [string]$InputPath = "C:\Users\codro\Desktop\NCIE\NCIE-006_Memory_Context_Architecture_Specification_v1_1_IN_DEVELOPMENT.docx",
    [string]$OutputPath = "C:\Users\codro\Desktop\NCIE\NCIE-006_Memory_Context_Architecture_Specification_v1_1_IN_DEVELOPMENT.pdf"
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
