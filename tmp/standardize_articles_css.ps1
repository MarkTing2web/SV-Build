$directory = "c:\Users\ler\OneDrive - Securevision Pte Ltd\1 SV Build"
$files = Get-ChildItem -Path $directory -Filter "insights-*.html"

$selectorsToRemove = @(
    '\.article-body\s*\{[^}]*\}',
    '\.prose\s+h2\s*\{[^}]*\}',
    '\.prose\s+h3\s*\{[^}]*\}',
    '\.prose\s+p\s*\{[^}]*\}',
    '\.prose\s+ul,\s*\.prose\s+ol\s*\{[^}]*\}',
    '\.prose\s+li\s*\{[^}]*\}',
    '\.callout-box\s*\{[^}]*\}',
    '\.callout-box\s+strong\s*\{[^}]*\}',
    '\.callout-box\s+p\s*\{[^}]*\}',
    '\.verdict-box\s*\{[^}]*\}',
    '\.verdict-box\s+p\s*\{[^}]*\}',
    '\.article-image-box\s*\{[^}]*\}',
    '\.article-image-box\s+img\s*\{[^}]*\}',
    '\.image-caption\s*\{[^}]*\}',
    '\.article-body\s*\{\s*padding:\s*40px\s*0;\s*\}'
)

$count = 0

foreach ($file in $files) {
    # Read the file content
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8

    # Extract the style block
    if ($content -match "(?s)<style>(.*?)</style>") {
        $originalStyles = $Matches[0]
        $styleInner = $Matches[1]
        $newStyleInner = $styleInner

        # Remove the selectors
        foreach ($selector in $selectorsToRemove) {
            $newStyleInner = $newStyleInner -replace $selector, ""
        }

        # Clean up excess whitespace and empty lines
        $newStyleInner = $newStyleInner -replace '(?m)^\s*$\n?', ''
        $newStyleInner = $newStyleInner.Trim()

        if ($newStyleInner -ne $styleInner.Trim()) {
            # Format nicely
            $formattedInner = ""
            if ($newStyleInner) {
                # Add proper indentation
                $lines = $newStyleInner -split "`n"
                foreach ($line in $lines) {
                    if ($line.Trim()) {
                        $formattedInner += "        " + $line.Trim() + "`n"
                    }
                }
            }
            
            # Reconstruction
            $newStyleBlock = "    <style>`n$formattedInner    </style>"
            $newContent = $content.Replace($originalStyles, $newStyleBlock)

            Set-Content -Path $file.FullName -Value $newContent -Encoding UTF8
            Write-Host "Cleaned up: $($file.Name)"
            $count++
        }
    }
}

Write-Host "Total files cleaned: $count"
