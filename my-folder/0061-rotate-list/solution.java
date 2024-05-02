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
    public int size(ListNode head)  {
        int s = 0;
        while (head != null) {
            s++;
            head = head.next;
        }
        return s;
    }

    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null || k == 0) return head;
        int s = size(head);
        k %= s;
        if(k == 0) return head;

        int rotate = s - k - 1;
        ListNode curr = head;
        for (int i=0; i < rotate; i++) {
            curr = curr.next;
        }
        ListNode start = curr.next;
        curr.next = null;
        curr = start;
        
        while (curr.next != null) {
            curr = curr.next;
        }
        curr.next = head;
        return start;
    }
}
