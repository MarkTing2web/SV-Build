$FILES = Get-ChildItem "insights-*.html" -File;

foreach ($f in $FILES) {
    # Read as UTF8
    $content = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8);

    # 1. Common corruption from PowerShell UTF-8 mismatch
    $content = $content.Replace("Â·", "·")
    $content = $content.Replace("Â ", " ")
    $content = $content.Replace("â€”", "—")
    $content = $content.Replace("ðŸ“…", "📅")
    $content = $content.Replace("ðŸ’¬", "💬")
    $content = $content.Replace("â€¢", "•")
    $content = $content.Replace("â€¦", "…")
    $content = $content.Replace("SECURET", "SECURE™")
    $content = $content.Replace("VESTAA", "VESTA")
    $content = $content.Replace("VESTA", "VESTA") # ensure single VESTA
    $content = $content.Replace("dY\".", "📅")
    $content = $content.Replace("dY'", "💬")

    # Handle the "A" separators
    $content = $content.Replace(" A  Securevision", " · Securevision")

    # Save cleanly as UTF8 (No BOM)
    $utf8NoBOM = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($f.FullName, $content, $utf8NoBOM);
    
    Write-Host "Fixed: $($f.Name)"
}
