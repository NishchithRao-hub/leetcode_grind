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
    public ListNode oddEvenList(ListNode head) {
        if (head == null) return head;
        if (head.next == null) return head;
        if(head.next.next == null) return head;
        ListNode oddHead = head;
        ListNode evenHead = head.next;
        ListNode oddCurrent = oddHead;
        ListNode evenCurrent = evenHead;
        while (oddCurrent != null){
            ListNode tempEven = oddCurrent.next;
            if (oddCurrent.next != null) {
                oddCurrent.next = oddCurrent.next.next;
            }

            evenCurrent.next = tempEven;
            evenCurrent = evenCurrent.next;
            if(oddCurrent.next == null) break;
            oddCurrent = oddCurrent.next;
        }
        oddCurrent.next = evenHead;
        return oddHead;
    }
}
