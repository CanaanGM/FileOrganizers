$source=$args[0]
$dist=$args[1]

"$($source)\*.jpg", "$($source)\*.png" | Move-Item -Destination $dist