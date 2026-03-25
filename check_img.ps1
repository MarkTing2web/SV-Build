Add-Type -AssemblyName System.Drawing
$images = @("cctv-overview-main.png", "cctv-planning-layout.png", "cctv-analytics-perimeter.png", "cctv-retail-heat-map.png", "cctv-face-recognition.png", "cctv-office-case.png", "cctv-maintenance-audit.png", "cctv-modern-ai.png")
foreach ($imgName in $images) {
    $path = "c:\Users\ler\OneDrive - Securevision Pte Ltd\1 SV Build\images\" + $imgName
    if (Test-Path $path) {
        $img = [System.Drawing.Image]::FromFile($path)
        Write-Output ($imgName + ": " + $img.Width + "x" + $img.Height)
        $img.Dispose()
    } else {
        Write-Output ($imgName + ": Not Found")
    }
}
