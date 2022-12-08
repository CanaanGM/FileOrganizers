$source=$args[0]
$dist=$args[1]

if (!(Test-Path "$($dist)\random")){
    New-Item "$($dist)\random" -ItemType Directory
}

"$($source)\*.jpg", "$($source)\*.png", "$($source)\*.jpeg" | Move-Item -Force -Destination "$($dist)\random"