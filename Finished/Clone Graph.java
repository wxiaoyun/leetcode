import java.util.ArrayList;
import java.util.List;
import java.util.*;

// Definition for a Node.
class Node {
  public int val;
  public List<Node> neighbors;

  public Node() {
    val = 0;
    neighbors = new ArrayList<Node>();
  }

  public Node(int _val) {
    val = _val;
    neighbors = new ArrayList<Node>();
  }

  public Node(int _val, ArrayList<Node> _neighbors) {
    val = _val;
    neighbors = _neighbors;
  }
}

class Solution {
  public void dfs(Node node, Node dup, Node[] visited) {
    visited[node.val] = dup;

    for (Node n : node.neighbors) {
      if (visited[n.val] == null) {
        Node dupNode = new Node(n.val);
        dup.neighbors.add(dupNode);
        dfs(n, dupNode, visited);
      } else {
        dup.neighbors.add(visited[n.val]);
      }
    }
  }

  public Node cloneGraph(Node node) {
    if (node == null)
      return null;
    Node dup = new Node(node.val);
    Node[] visited = new Node[101];
    Arrays.fill(visited, null);
    dfs(node, dup, visited);
    return dup;
  }
}