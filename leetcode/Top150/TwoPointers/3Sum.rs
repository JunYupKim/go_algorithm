impl Solution {

    pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut answer:Vec<Vec<i32>> = Vec::new(); 
        let mut num = nums;
        num.sort(); 
        for i in (0..(num.len() as usize)-2){
            let mut x = num[i]; 
            let mut left = i+1; 
            let mut right = num.len()-1; 
            while left < right{ 
                let target = x+num[left]+num[right];
                if target == 0 {
                    let sub_vec = [x,num[left],num[right]].to_vec();
                    if !answer.contains(&sub_vec){
                        answer.append(&mut vec![sub_vec]);
                    }
                }
                if target < 0 {
                    left += 1; 
                }else { 
                    right -= 1; 
                }
            }
        }

        return answer; 
    }
}
