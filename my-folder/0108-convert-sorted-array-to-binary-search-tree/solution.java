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
    public TreeNode helper(int[] arr, int start, int end){
        if(start>end) return null;
        int mid= start + (end-start)/2;
        TreeNode midNode= new TreeNode(arr[mid]);
        midNode.left=helper(arr,start,mid-1);
        midNode.right=helper(arr,mid+1,end);
        return midNode;
    }

    public TreeNode sortedArrayToBST(int[] nums) {
        return helper(nums,0,nums.length-1);
    }
}
