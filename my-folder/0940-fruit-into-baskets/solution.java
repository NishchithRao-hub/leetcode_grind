class Solution {
    public int totalFruit(int[] fruits) {
        int[] counts = new int[fruits.length];
        int max=0;
        int currMax=0;
        int type=0;
        int start=0;
        for(int i=0;i<fruits.length;i++){
            if(counts[fruits[i]]==0) type++;
                counts[fruits[i]]++;
                currMax++;
            while(type>2 && start<i){
                counts[fruits[start]]--;
                if(counts[fruits[start]]==0) type--;
                    start++;
                    currMax--;
            }
            max=Math.max(max,currMax);
        }
        return max;
    }
}
