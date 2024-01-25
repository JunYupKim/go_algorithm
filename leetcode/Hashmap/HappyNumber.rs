impl Solution {
    pub fn is_happy(n: i32) -> bool {
        let mut temp_number:i32 = n; 
        let mut count:i32 = 0; 
        while count < 10{
            if temp_number == 1 {
                return true; 
            }
            let number:&str = &temp_number.to_string(); 
            let mut nu:i32 = 0; 
            for i in number.chars() {
                let result = i.to_digit(10).unwrap_or(0) as i32; 
                nu += (result*result);  
            }
            temp_number = nu; 
            count += 1; 
        }
        return false; 
    }
}