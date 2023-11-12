fn get_concatenation(nums: Vec<i32>) -> Vec<i32> {
    let mut vec: Vec<i32> = Vec::new();

    for i in 0..2 {
        for j in nums.iter() {
            vec.push(*j);
        }
    }
    vec
}