mod rnd_image;
use rnd_image::get_random_image_from_dir;

use std::{process::Command, env};


fn open_image(image_path: String) {

    Command::new("explorer".to_string())
        .arg(image_path)
        .spawn()
        .unwrap();
}

fn main () {

    let args: Vec<String> = env::args().collect();

    let dir_path = args.get(1).expect("Please provide a directory path.");

    let image_path =get_random_image_from_dir(dir_path); 
    
    println!("{:?}", image_path);
    
    open_image(image_path);
}