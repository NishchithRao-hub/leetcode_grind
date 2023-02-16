class Solution {
    public int singleNumber(int[] nums) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        for(int i=0;i<nums.length;i++){
            if(list.contains(nums[i])){
                int n = list.indexOf(nums[i]);
                list.remove(n);
            }
            else if(!list.contains(nums[i])){
                list.add(nums[i]);
            }
        }
        return list.get(0);
    }
}
    /*
    2nd Solution:

    int ans=0; //since XOR with 0 returns same number 
        for(int i=0; i<nums.length; i++){
            ans ^= nums[i];  // ans = (ans) XOR (array element at i) 
        }
        return ans; */

