class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length == 0)
            return 0;

        HashSet<Integer> set = new HashSet<>();
        for(int num : nums){
            set.add(num);
        }

        int count = 1;
        int longest = 0;

        for (int num : nums){
            if(!set.contains(num - 1)){
                int x = num;
                count = 1;

                while(set.contains(x+1)){
                    count++;
                    x = x + 1;
                }
            }
            longest = Math.max(longest, count);
        }
        return longest;
    }
}
