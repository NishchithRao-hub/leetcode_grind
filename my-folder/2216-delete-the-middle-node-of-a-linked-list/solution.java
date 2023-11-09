/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteMiddle(ListNode head) {
        if(head==null)
            return head;
        ListNode curr=head;
        int c=0;
        // Calculating the size of linked list
        while(curr!=null){
                c++;
                curr=curr.next;
        }
        if(c==1) // edge case if size of linked list is 1.
        {
            head=null;
            return head;
        }
        
        int mid=(c/2)-1; //0-based indexing
        c=0;
        ListNode temp=head;
        // traversing till the temp node reaches mid-1 node.
        while(c<mid)
        {   c++;
            temp=temp.next;
        }
          temp.next=temp.next.next;//skips the the middle node which is to be deleted and moves to next node.
       
        return head;
    }
}
