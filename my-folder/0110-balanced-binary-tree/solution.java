/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isBalanced(TreeNode root) {
        if(root==null) return true;
        if(Height(root)==-1) return false;
        return true;
    }
    public int Height(TreeNode root){
        if(root==null) return 0;
        int left_h=Height(root.left);
        int right_h=Height(root.right);
        if(left_h==-1 || right_h==-1) return -1;
        if(Math.abs(left_h-right_h)>1) return -1;
        return Math.max(left_h,right_h)+1;
    }
}
