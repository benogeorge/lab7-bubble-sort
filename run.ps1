param(
  [Parameter(ValueFromRemainingArguments = $true)]
  [string[]]$Args
)

$ErrorActionPreference = "Stop"

function Find-PythonExe {
  $base = Join-Path $env:LOCALAPPDATA "Programs\\Python"
  if (-not (Test-Path $base)) { return $null }

  # Most Python.org installs look like:
  #   %LOCALAPPDATA%\Programs\Python\Python312\python.exe
  $dirs = Get-ChildItem -Path $base -Directory -Filter "Python*" -ErrorAction SilentlyContinue |
    Sort-Object FullName -Descending

  foreach ($dir in $dirs) {
    $candidate = Join-Path $dir.FullName "python.exe"
    if (Test-Path $candidate) { return $candidate }
  }

  return $null
}

$pythonExe = Find-PythonExe
if (-not $pythonExe) {
  if (Get-Command winget -ErrorAction SilentlyContinue) {
    Write-Host "Python not found. Installing Python 3.12 via winget..."
    winget install -e --id Python.Python.3.12 --silent --accept-package-agreements --accept-source-agreements | Out-Host
    $pythonExe = Find-PythonExe
  }
}

if (-not $pythonExe) {
  throw "Python is not installed (or not discoverable). Install Python 3.x, then re-run: .\\run.ps1"
}

# Prefer the discovered python in this process, even if WindowsApps 'python' alias exists.
$pythonDir = Split-Path -Parent $pythonExe
$env:PATH = "$pythonDir;$env:PATH"

& $pythonExe (Join-Path $PSScriptRoot "main.py") @Args
