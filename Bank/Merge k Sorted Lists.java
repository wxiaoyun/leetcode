import java.util.PriorityQueue;

class Solution {

  public class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
      this.val = val;
    }

    ListNode(int val, ListNode next) {
      this.val = val;
      this.next = next;
    }
  }

  public class Pair {
    public int value;
    public int index;

    public Pair(int h, int t) {
      this.value = h;
      this.index = t;
    }

  }

  public ListNode mergeKLists(ListNode[] lists) {
    if (lists.length == 0) {
      return null;
    }

    PriorityQueue<Pair> pq = new PriorityQueue<>(
        lists.length,
        (p1, p2) -> Integer.compare(p1.value, p2.value));
    for (int i = 0; i < lists.length; i++) {
      if (lists[i] != null) {
        pq.add(new Pair(lists[i].val, i));
        lists[i] = lists[i].next;
      }
    }

    ListNode dummyHead = new ListNode();
    ListNode curr = dummyHead;

    while (!pq.isEmpty()) {
      Pair nextMin = pq.poll();

      curr.next = new ListNode(nextMin.value);
      curr = curr.next;

      if (lists[nextMin.index] != null) {
        pq.add(new Pair(lists[nextMin.index].val, nextMin.index));
        lists[nextMin.index] = lists[nextMin.index].next;
      }
    }

    return dummyHead.next;
  }
}