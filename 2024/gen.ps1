# Parameters
$startDay = 1
$endDay = 25  

for ($day = $startDay; $day -le $endDay; $day++) {
    $dayStr = "day" + "{0:D2}" -f $day
    
    New-Item -ItemType Directory -Path $dayStr -Force | Out-Null
    
    $srcDir = Join-Path $dayStr "src"
    New-Item -ItemType Directory -Path $srcDir -Force | Out-Null

    $cargoTomlPath = Join-Path $dayStr "Cargo.toml"
    
    $cargoTomlContent = @"
[package]
name = "$dayStr"
version = "0.1.0"
edition = "2021"

[dependencies]
utils = { path = "../utils" }
"@

    Set-Content -Path $cargoTomlPath -Value $cargoTomlContent

    $mainRsPath = Join-Path $srcDir "main.rs"

    $mainRsContent = @"
use utils;

fn main() {
    println!("Solution for Day $day");
}
"@

    Set-Content -Path $mainRsPath -Value $mainRsContent
}
