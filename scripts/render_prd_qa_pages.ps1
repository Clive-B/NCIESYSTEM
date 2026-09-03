param(
    [string]$InputPath = "C:\Users\codro\Desktop\NCIE\NCIE-001_Master_PRD_v1_2_PRODUCTION_READY.docx",
    [string]$OutputDirectory = "C:\Users\codro\Desktop\NCIE\qa_prd_pages"
)

New-Item -ItemType Directory -Path $OutputDirectory -Force | Out-Null
$word = $null
$document = $null
$powerPoint = $null
$presentation = $null
try {
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $word.DisplayAlerts = 0
    $document = $word.Documents.Open($InputPath, $false, $true)

    $targets = New-Object System.Collections.Generic.List[int]
    $targets.Add(1)
    foreach ($needle in @(
        "Contents",
        "Chapter 1 Expansion",
        "Chapter 6 Expansion",
        "Chapter 15 Expansion",
        "Figure 1.",
        "Figure 100.",
        "Figure 196."
    )) {
        $range = $document.Content.Duplicate
        $found = $range.Find.Execute($needle)
        if ($found) {
            $targets.Add([int]$range.Information(3))
        }
    }
    $pages = $targets | Sort-Object -Unique

    $powerPoint = New-Object -ComObject PowerPoint.Application
    $presentation = $powerPoint.Presentations.Add()
    $presentation.PageSetup.SlideWidth = 595.28
    $presentation.PageSetup.SlideHeight = 841.89

    foreach ($page in $pages) {
        $word.Selection.GoTo(1, 1, $page) | Out-Null
        $pageRange = $word.Selection.Bookmarks.Item("\Page").Range
        $pageRange.CopyAsPicture()
        Start-Sleep -Milliseconds 500
        $slide = $presentation.Slides.Add($presentation.Slides.Count + 1, 12)
        $shapeRange = $slide.Shapes.PasteSpecial(2)
        $shape = $shapeRange.Item(1)
        $shape.LockAspectRatio = -1
        if (($shape.Width / $shape.Height) -gt (595.28 / 841.89)) {
            $shape.Width = 595.28
        }
        else {
            $shape.Height = 841.89
        }
        $shape.Left = (595.28 - $shape.Width) / 2
        $shape.Top = (841.89 - $shape.Height) / 2
        $target = Join-Path $OutputDirectory ("page-{0:D4}.png" -f $page)
        $slide.Export($target, "PNG", 1191, 1684)
        Write-Output "rendered=$target"
    }
}
finally {
    if ($null -ne $presentation) { $presentation.Close() }
    if ($null -ne $powerPoint) { $powerPoint.Quit() }
    if ($null -ne $document) { $document.Close($false) }
    if ($null -ne $word) { $word.Quit() }
}
