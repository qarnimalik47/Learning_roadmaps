# Export every slide of the CCNA module decks to 1920x1080 PNG files, ready for build_slides.py.
#
#   powershell -ExecutionPolicy Bypass -File tools\export_slides.ps1 -Decks slides -Out C:\temp\slide-png
#
# Needs Microsoft PowerPoint. Decks are opened read-only and without a window, and PowerPoint is
# only closed at the end if this script started it. On a PC where WPS Office has taken over the
# 64-bit "PowerPoint.Application" registration, run this from 32-bit PowerShell
# (C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe) so real PowerPoint does the export.
param(
  [Parameter(Mandatory = $true)][string]$Decks,
  [Parameter(Mandatory = $true)][string]$Out
)
$ErrorActionPreference = "Stop"
$Decks = (Resolve-Path $Decks).Path
New-Item -ItemType Directory -Force $Out | Out-Null
$wasRunning = @(Get-Process POWERPNT -ErrorAction SilentlyContinue).Count -gt 0
$pp = New-Object -ComObject PowerPoint.Application
"Exporting with $($pp.Name) $($pp.Version)"
foreach ($f in Get-ChildItem $Decks -Filter "Module *.pptx" | Sort-Object Name) {
  $m = [int]($f.Name -replace '^Module (\d+).*$', '$1')
  $dir = Join-Path $Out ("m{0}" -f $m)
  New-Item -ItemType Directory -Force $dir | Out-Null
  # Open(FileName, ReadOnly = msoTrue, Untitled = msoFalse, WithWindow = msoFalse)
  $p = $pp.Presentations.Open($f.FullName, -1, 0, 0)
  foreach ($s in $p.Slides) {
    $s.Export((Join-Path $dir ("{0:D3}.png" -f $s.SlideIndex)), "PNG", 1920, 1080)
  }
  "{0}: {1} slides" -f $f.Name, $p.Slides.Count
  $p.Close()
}
if (-not $wasRunning -and $pp.Presentations.Count -eq 0) { $pp.Quit() }
