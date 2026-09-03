$files = @(
    "C:\Users\codro\Desktop\NCIE\NCIE-001_Master_PRD_v1_3_IN_DEVELOPMENT.docx",
    "C:\Users\codro\Desktop\NCIE\NCIE-001_v1_3_Surgical_Amendment_Change_Register.docx",
    "C:\Users\codro\Desktop\NCIE\NCIE-001_v1_2_to_v1_3_Amendment_Verification_Report.docx"
)

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0

try {
    foreach ($InputPath in $files) {
        $OutputPath = [System.IO.Path]::ChangeExtension($InputPath, "pdf")
        $document = $word.Documents.Open($InputPath, $false, $false)
        try {
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
            Write-Output "pages=$pages pdf=$OutputPath"
        }
        finally {
            $document.Close($false)
        }
    }
}
finally {
    $word.Quit()
}
