class Solution {
    public String longestCommonPrefix(String[] strs) {
    
    if(strs.length==0){
        return "";
    }
      String prev=strs[0];
      for(int i=1;i<strs.length;i++){
          String curr=strs[i];
          while(curr.indexOf(prev)!=0){
              prev=prev.substring(0,prev.length()-1);
          }
      }
    return prev;
    }
}
