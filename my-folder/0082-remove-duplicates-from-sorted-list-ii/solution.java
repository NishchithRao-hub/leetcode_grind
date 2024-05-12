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
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null || head.next == null)
            return head;

        ListNode temp = new ListNode(0);
        temp.next = head;
        ListNode current = temp;

        while(current.next != null && current.next.next != null) {
            if(current.next.val == current.next.next.val) {
                int dup_val = current.next.val;
                while(current.next != null && current.next.val == dup_val) {
                    current.next = current.next.next;
                }
            }
            else {
                current = current.next;
            }
        }
        return temp.next;
    }
}
