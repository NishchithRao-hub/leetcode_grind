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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if(head == null || head.next== null)
            return head;
        if(left == right)
            return head;
        ListNode curr = head;
        ListNode t =null;
        ListNode prev = null;
        ListNode a = null;
        ListNode b = null;
        boolean flag = false;

        if(left == 1){
            flag=true;
            t=curr;
        }
        int s1 =1;
        while(curr!=null){
            if(s1 == left && !flag){
                b = prev;
                t = curr;
            }
            if(s1 == right){
                a = curr.next;
                curr.next = null;
                break;
            }
            prev = curr;
            curr = curr.next;
            s1++;
        }
        if (!flag) {
            b.next = null;
        }
        ListNode ans = reverseList(t);
        t.next = a;

        if (!flag) {
            b.next = ans;
        }

        if (flag) {
            head = ans;
        }

        return head;
    }
    public ListNode reverseList(ListNode head){
        if (head == null || head.next == null)
         return head;

        ListNode curr = head;
        ListNode prev = null;
        ListNode next = null;

        while (curr != null) {
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }

        return prev;
    }
}
