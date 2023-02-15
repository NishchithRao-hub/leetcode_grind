class Solution {
    public List<Integer> getRow(int row) {
        List<Integer> res = new ArrayList<>();
        res.add(1);
        long temp=1;
        for(int i=1,up=row,down=1; i<=row; i++,up--,down++){
            temp=temp*up/down;
            res.add((int)temp);
        }
        return res;
    }
}
