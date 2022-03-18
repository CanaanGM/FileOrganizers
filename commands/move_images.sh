#!/bin/bash
while getopts s:d: flag
do 
    case "${flag}" in 
        s) source_dir=${OPTARG};;
        d) target_dir=${OPTARG};;
    esac
done

function test_if_file_exists(){
    mkdir -p $target_dir;
    mkdir -p "${target_dir}/animated";
}

function move_images(){
    test_if_file_exists
    cd $source_dir;
    mv -f *.jpg *.png *.jpeg -t $target_dir ;
    mv -f *.gif *.apng *.avif -t "${target_dir}/animated"; >> nu 
}

{
    move_images 2> /dev/null
} || {
    exit 1;
}