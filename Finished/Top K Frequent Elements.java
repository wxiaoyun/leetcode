import java.util.PriorityQueue;
import java.util.HashMap;

class Solution {
  public int[] topKFrequent(int[] nums, int k) {
    // Count the frequency of each number
    HashMap<Integer, Integer> map = new HashMap<>();
    for (int num : nums) {
      map.put(num, map.getOrDefault(num, 0) + 1);
    }

    // Use a min heap to keep track of the top k frequent elements
    // Element is ranked by its frequency, so the least frequent element is at the
    // top
    PriorityQueue<Integer> heap = new PriorityQueue<>((a, b) -> map.get(a) - map.get(b));
    for (int key : map.keySet()) {
      heap.add(key);
      // Keep the size of the heap to k
      if (heap.size() > k) {
        // Remove the least frequent element
        heap.poll();
      }
    }

    // Return the top k frequent elements
    int[] result = new int[k];
    for (int i = 0; i < k; i++) {
      // The least frequent element is at the top of the heap
      result[i] = heap.poll();
    }
    return result;
  }
}