impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
     
        let str_number = x.to_string(); 
        let num_length = str_number.len();

        for idx in 0..str_number.len()/2{
            let num_as_byte_front: u8 = str_number.as_bytes()[idx]; 
            let num_front: char = num_as_byte_front as char; 

            let num_as_byte_back:u8 = str_number.as_bytes()[num_length - idx-1]; 
            let num_back: char = num_as_byte_back as char; 
            if num_front != num_back {
                return false; 
            }
        }
        true 
    }
}