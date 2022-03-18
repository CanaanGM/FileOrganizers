$source=$args[0]
$dist=$args[1]

if (!(Test-Path "$($dist)\animated")){
    New-Item "$($dist)\animated" -ItemType Directory
}


"$($source)\*.gif" , "$($source)\*.apng", "$($source)\*.avif"| Move-Item -Destination "$($dist)\animated"