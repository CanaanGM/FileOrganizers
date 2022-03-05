$source=$args[0]
$dist=$args[1]

"$($source)\*.jpg", "$($source)\*.png", "$($source)\*.gif", "$($source)\*.jpeg" | Move-Item -Destination $dist