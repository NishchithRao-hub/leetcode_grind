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
    public int minDepth(TreeNode root) {
        if(root==null) return 0;
        int left_h=minDepth(root.left);
        int right_h=minDepth(root.right);
        if(left_h==0 || right_h==0)
            return 1+Math.max(left_h,right_h);
        return 1+Math.min(left_h,right_h);
    }
}
