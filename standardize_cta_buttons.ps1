Get-ChildItem -Filter *.html | ForEach-Object {
    $content = Get-Content $_.FullName -Raw
    $changed = $false
    
    # --- Fix 1: Dedicated CTA Standardisation ---
    # Look for a cta-section or get-started section
    $ctaRegex = '(?s)(<(?:section|div)[^>]*(?:cta-section|get-started)[^>]*>.*?)<div[^>]*(?:btn-group|factors-grid|grid-3|cta-links)[^>]*>.*?(<div[^>]*footer-note|<!--|/section|/div>)'
    if ($content -match $ctaRegex) {
        $prefix = $matches[0].Groups[1].Value
        $innerBlock = $matches[0].Value
        
        # Identify links inside the block
        $links = [regex]::Matches($innerBlock, '<a [^>]*href="([^"]+)"')
        if ($links.Count -ge 2) { # If it has at least 2 contact links
            $href1 = $links[0].Groups[1].Value
            $href2 = $links[1].Groups[1].Value
            $href3 = if ($links.Count -ge 3) { $links[2].Groups[1].Value } else { "contact.html" }
            
            # The pattern provided:
            # <div class="btn-group">
            #   <a href="[existing href]" class="btn btn-primary">Book Assessment</a>
            #   <a href="[existing href]" class="btn btn-outline-light">WhatsApp Us</a>
            #   <a href="[existing href]" class="btn btn-outline-light">Call Now</a>
            # </div>
            
            $newBtnGroup = '        <div class="btn-group mt-32">
            <a href="' + $href1 + '" class="btn btn-primary">Book Assessment</a>
            <a href="' + $href2 + '" class="btn btn-outline-light">WhatsApp Us</a>
            <a href="' + $href3 + '" class="btn btn-outline-light">Call Now</a>
        </div>'
            
            # Replace the old buttons block with the new one
            # Note: We match the original block carefully
            $oldBlockRegex = '(?s)<div[^>]*?(?:btn-group|factors-grid|grid-3|cta-links)[^>]*?>.*?</div>\s*'
            # Wait, grid-3 might contain multiple divs... 
            # Safer: Look for the specific btn-group or factors-grid or grid-3 that contains the buttons
            
            if ($innerBlock -match 'factors-grid|grid-3|cta-links|btn-group') {
                $matchOld = [regex]::Match($innerBlock, '(?s)<div[^>]*?(?:factors-grid|grid-3|cta-links|btn-group)[^>]*?>.*?</div>(?!\s*</div>)')
                if ($matchOld.Success) {
                    $content = $content.Replace($matchOld.Value, ($newBtnGroup + "`n"))
                    $changed = $true
                }
            }
        }
    }
    
    # --- Fix 2: Hero Section Button Class Fixes ---
    # Find btn-group inside a hero section
    $heroRegex = '(?s)<(?:header|section)[^>]*hero[^>]*>.*?(<div class="btn-group[^>]*>.*?</div>)'
    $heroMatch = [regex]::Matches($content, $heroRegex)
    foreach ($hMatch in $heroMatch) {
       $btnGroupBlock = $hMatch.Groups[1].Value
       
       # Convert links to buttons if they aren't already
       $links = [regex]::Matches($btnGroupBlock, '<a [^>]*class="([^"]+)"[^>]*>([^<]+)</a>')
       if ($links.Count -gt 0) {
           $newBlock = $btnGroupBlock
           for ($i = 0; $i -lt $links.Count; $i++) {
              $oldLink = $links[$i].Value
              $tagContent = $links[$i].Groups[2].Value
              # If it's the first button, use btn-primary
              if ($i -eq 0) {
                 if ($oldLink -notmatch 'btn-primary') {
                    $newLink = $oldLink -replace 'class="[^"]+"', 'class="btn btn-primary"'
                    $newBlock = $newBlock.Replace($oldLink, $newLink)
                 }
              } else {
                 if ($oldLink -notmatch 'btn-outline-light') {
                    $newLink = $oldLink -replace 'class="[^"]+"', 'class="btn btn-outline-light"'
                    $newBlock = $newBlock.Replace($oldLink, $newLink)
                 }
              }
           }
           if ($newBlock -ne $btnGroupBlock) {
              $content = $content.Replace($btnGroupBlock, $newBlock)
              $changed = $true
           }
       }
    }
    
    if ($changed) {
        $content | Set-Content $_.FullName -NoNewline
        Write-Host "Updated CTA on $($_.Name)"
    }
}
