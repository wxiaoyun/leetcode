import java.util.*;

class Solution {
  public static char getComplementBracket(char bracket) {
    if (bracket == '(') {
      return ')';
    } else if (bracket == '[') {
      return ']';
    } else if (bracket == '{') {
      return '}';
    } else {
      return ' ';
    }
  }

  public static boolean isClosingBracket(char bracket) {
    return bracket == ')' || bracket == ']' || bracket == '}';
  }

  public boolean isValid(String s) {
    Stack<Character> stack = new Stack<>();

    for (int i = 0; i < s.length(); i++) {
      char bracket = s.charAt(i);

      if (isClosingBracket(bracket)) {
        if (stack.isEmpty()) {
          return false;
        }

        char top = stack.pop();

        if (getComplementBracket(top) != bracket) {
          return false;
        }
      } else {
        stack.push(bracket);
      }
    }
    return stack.isEmpty();
  }
}