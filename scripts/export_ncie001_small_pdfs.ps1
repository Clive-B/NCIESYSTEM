$files = @(
    "C:\Users\codro\Desktop\NCIE\NCIE-001_v1_3_Surgical_Amendment_Change_Register.docx",
    "C:\Users\codro\Desktop\NCIE\NCIE-001_v1_2_to_v1_3_Amendment_Verification_Report.docx"
)

foreach ($InputPath in $files) {
    $OutputPath = [System.IO.Path]::ChangeExtension($InputPath, "pdf")
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
}
