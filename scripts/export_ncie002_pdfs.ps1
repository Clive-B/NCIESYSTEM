$files = @(
    "C:\Users\codro\Desktop\NCIE\NCIE-002_System_Architecture_Technical_Design_v0_5_IN_DEVELOPMENT.docx",
    "C:\Users\codro\Desktop\NCIE\NCIE-002_v0_5_Surgical_Amendment_Change_Register.docx",
    "C:\Users\codro\Desktop\NCIE\NCIE-002_v0_4_to_v0_5_Amendment_Verification_Report.docx"
)

foreach ($InputPath in $files) {
    $OutputPath = [System.IO.Path]::ChangeExtension($InputPath, "pdf")
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $word.DisplayAlerts = 0
    try {
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
    finally {
        $word.Quit()
    }
}
