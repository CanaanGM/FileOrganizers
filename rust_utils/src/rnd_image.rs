use std::path::{PathBuf, Path};
use std::{fs};
use rand::prelude::*;


fn get_all_images_in_dir(path: &Path, extensions: &[&str]) -> Vec<PathBuf> {
    let mut all_images = vec![];

    if let Ok(parent_dir) = fs::read_dir(path) {
        for sub_dir in parent_dir.flatten() {
            let file_type = sub_dir.file_type().ok();

            if file_type.map(|ft| ft.is_dir()).unwrap_or(false) {
                let sub_dir_path = sub_dir.path();
                let sub_dir_images = get_all_images_in_dir(&sub_dir_path, extensions);
                all_images.extend(sub_dir_images);
            } else if let Some(extension) = sub_dir.path().extension() {
                if extensions.contains(&extension.to_str().unwrap().to_lowercase().as_str()) {
                    all_images.push(sub_dir.path());
                }
            }
        }
    }
    all_images
}

pub fn get_random_image_from_dir(dir_path: &str) -> String {
    let path_to_dir = Path::new(dir_path);

    let mut rng = thread_rng();

    // can be taken from args
    let extensions: [&str; 4] = ["jpeg", "png", "gif", "jpg"];
    let all_images_in_dir: Vec<_> = get_all_images_in_dir(path_to_dir, &extensions);
    // println!(" all images : {:?}", all_images_in_dir);
   
    let  choice = all_images_in_dir
                                            .choose(&mut rng)
                                            .unwrap();

    String::from(choice.to_owned().to_string_lossy())
    
} 