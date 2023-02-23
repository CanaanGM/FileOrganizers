/// get a directory tree
/// get all the folder inside it that normall dev spawn
/// delete them recursivly; as to make sure nothing of them remains
const DIRS_TO_REMOVE: [&str; 4] = ["node_modules", "target", "bin", "obj"];
const BASE_DIR: &str = "E:/development"; // this should be dynamic

use std::{fs, path::*};
fn main() {
    let path = Path::new(BASE_DIR);

    println!("Greetings");
    println!("Cleaning {:?}", path);
    let dir_path = BASE_DIR;
    remove_dirs(Path::new(dir_path)).unwrap();
}

fn remove_dirs(dir_path: &Path) -> std::io::Result<()> {
    if dir_path.is_dir() {
        for entry in fs::read_dir(dir_path)? {
            let entry_path = entry?.path();
            if entry_path.is_dir() {
                let entry_name = entry_path.file_name().unwrap().to_str().unwrap();
                if DIRS_TO_REMOVE.contains(&entry_name) {
                    println!("++ Removed directory: {:?} ++\n", &entry_path);
                    fs::remove_dir_all(entry_path)?;
                } else {
                    remove_dirs(&entry_path)?;
                }
            }
        }
    }
    Ok(())
}
