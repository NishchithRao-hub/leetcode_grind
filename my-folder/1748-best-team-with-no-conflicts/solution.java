class Solution {
    public int bestTeamScore(int[] scores, int[] ages) {
        final int n=ages.length;
        int[][] ageScore=new int[n][2];

        for(int i=0;i<n;i++){
            ageScore[i][0]=ages[i];
            ageScore[i][1]=scores[i];
        }

        Arrays.sort(ageScore,(a,b) -> a[0]==b[0] ? a[1]-b[1] : a[0]-b[0]);
        Integer[][] dp=new Integer[n][n];
        return findMaxScore(dp,ageScore,-1,0);
    }
    private int findMaxScore(Integer[][] dp,int[][] ageScore,int prev, int index){
        if(index>=ageScore.length){
            return 0;
        }
        if(dp[prev+1][index]!=null){
            return dp[prev+1][index];
        }
        if(prev==-1 || ageScore[index][1] >= ageScore[prev][1]){
            return dp[prev+1][index]=Math.max(findMaxScore(dp,ageScore,prev,index+1),ageScore[index][1]+findMaxScore(dp,ageScore,index,index+1));
        }
        return dp[prev+1][index]=findMaxScore(dp,ageScore,prev,index+1);
    }
}

