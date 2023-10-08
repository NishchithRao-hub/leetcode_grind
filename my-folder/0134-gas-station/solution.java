class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int totalFuel=0;
        int totalCost=0;
        int n = gas.length;
        for(int i=0;i<n;i++){
            totalFuel+=gas[i];
            totalCost+=cost[i];
        }
        if(totalFuel < totalCost)
            return -1;
        int start=0;
        int currFuel=0;
        for(int i=0;i<n;i++){
            if(currFuel<0){
                currFuel=0;
                start=i;
            }
            currFuel += gas[i]-cost[i];
        }
        return start;
    }
}
