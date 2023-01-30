class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] Result=new int[2];
        HashMap<Integer,Integer> indexes=new HashMap<Integer,Integer>();
        for(int i=0;i<nums.length;i++){
            if(indexes.containsKey(target-nums[i])){
                Result[1]=i;
                Result[0]=indexes.get(target-nums[i]);
                return Result;
            }
        indexes.put(nums[i],i);
        }
    return Result;
    }
}

