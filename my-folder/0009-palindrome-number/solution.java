class Solution {
    public boolean isPalindrome(int x) {
        if(x<0)
            return false;
        else if(reverseNum(x)==x)
            return true;
        else
            return false;
    }
    public int reverseNum(int num){
        int reverse=0;
        while(num!=0){
            int remainder=num%10;
            reverse=reverse*10+remainder;
            num=num/10;
        }
        return reverse;
    }
}

