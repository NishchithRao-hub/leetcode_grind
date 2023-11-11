class Solution {
    public String predictPartyVictory(String senate) {
        Queue<Integer> rad = new LinkedList<>();
        Queue<Integer> dir = new LinkedList<>();
        int n = senate.length();
        for(int i=0;i<n;i++){
            if(senate.charAt(i) == 'R')
                rad.offer(i);
            else
                dir.offer(i);
        }
        while(!rad.isEmpty() && !dir.isEmpty()){
            int v1 = rad.poll();
            int v2 = dir.poll();
            if(v1<v2)
                rad.offer(n+v1);
            else
                dir.offer(n+v2);
        }
        return (rad.isEmpty()) ? ("Dire") : ("Radiant");
    }
}
