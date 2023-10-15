class Solution {
    int long_sub = 0;
    int maxLen = 0;
    public String longestPalindrome(String s) {
        char[] input = s.toCharArray();
        if(s.length() < 2)
            return s;
        for( int i=0; i<input.length;i++){
            expandPalindrome(input,i,i);
            expandPalindrome(input,i,i+1);
        }
        return s.substring(long_sub,long_sub+maxLen);
    }

    public void expandPalindrome(char[] s,int j,int k){
        while(j>=0 && k<s.length && s[j] == s[k]){
            j--;
            k++;
        }
        if(maxLen < k-j-1){
            maxLen = k-j-1;
            long_sub = j+1;
        }
    }
}
