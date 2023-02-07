class Solution {
    public int lengthOfLastWord(String s) {
        String s1=s.trim();
        char[] chars=s1.toCharArray();
        int count=0;
        for(int i= chars.length-1;i>=0;i--){
            count++;
            if(chars[i]==' '){
                return count-1;
            }
        }
        return count;
    }
}
