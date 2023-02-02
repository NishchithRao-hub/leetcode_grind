class Solution {
    public int removeElement(int[] nums, int val) {
        int p=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]!=val){
                int temp=nums[p];
                nums[p]=nums[i];
                nums[i]=temp;
                p++;
            }
        }
        return p;
    }
}
