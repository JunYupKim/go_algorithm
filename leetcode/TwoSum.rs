impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut answer:Vec<i32> = Vec::new(); 
        let mut i:usize = 0; 

        while i < nums.len(){
            for idx in i+1..nums.len(){
                if nums[idx]+nums[i] == target {
                    answer.push((idx)as i32); 
                    answer.push(i as i32); 
                    return answer; 
                }
            }
            i += 1; 
        }

        return answer; 
    }
}