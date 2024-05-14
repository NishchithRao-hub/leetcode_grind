class Solution {
    public int rob(int[] nums) {
        if (nums.length == 0) return 0;
        if (nums.length == 1) return nums[0];
        if (nums.length == 2) return Math.max(nums[0], nums[1]);    
        return Math.max(robDpCircular(nums,0,nums.length-2), robDpCircular(nums,1,nums.length-1));
    }

    private int robDpCircular(int[] nums, int start, int end) {
        int score1 = 0, score2 = 0;
        for (int i = start; i <= end; i++) {
            int tempScore = Math.max(score1 + nums[i], score2);
            score1 = score2;
            score2 = tempScore;
        }
        return score2;
    }
}
