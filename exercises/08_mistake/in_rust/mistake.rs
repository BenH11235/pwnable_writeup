use std::fs::File;
use std::io;

fn main() -> Result<(),io::Error> {
    let mut fd : File;  
    if fd = File::open("password") .is_ok() {
        //do something...
    } 
    Ok(())
}

