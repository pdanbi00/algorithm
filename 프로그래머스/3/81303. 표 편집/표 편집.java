import java.util.Stack;

class Solution {
    public String solution(int n, int k, String[] cmd) {
        Node[] node = new Node[1000001];
        Stack<Node> stack = new Stack<>();
        node[0] = new Node();
        
        for (int i = 1; i < n; i++) {
            node[i] = new Node();
            node[i].pre = node[i-1];
            node[i-1].next = node[i];
        }
        
        Node now = node[k];
        
        for (String s : cmd) {
            char ch = s.charAt(0);
            
            switch (ch) {
                case 'U' -> { // 위로 이동
                    int num = Integer.parseInt(s.substring(2));
                    for (int i = 0; i < num; i++) {
                        now = now.pre;
                    }
                }
                case 'D' -> {
                    int num = Integer.parseInt(s.substring(2));
                    for (int i = 0; i < num; i++) {
                        now = now.next;
                    }
                }
                case 'C' -> {
                    now.isDeleted = true;
                    stack.push(now);
                    
                    Node pre = now.pre;
                    Node next = now.next;
                    
                    if (pre != null) pre.next = next;
                    if (next != null) {
                        next.pre = pre;
                        now = next;
                    } else {
                        now = pre;
                    }
                }
                case 'Z' -> {
                    Node delete = stack.pop();
                    Node pre = delete.pre;
                    Node next = delete.next;
                    delete.isDeleted = false;
                    
                    if (pre != null) {
                        pre.next = delete;
                    }
                    if (next != null) {
                        next.pre = delete;
                    }
                }
            }
        }
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (node[i].isDeleted) sb.append("X");
            else sb.append("O");
        }
        return sb.toString();
    }
    
    static class Node{
    Node pre = null;
    Node next = null;
    boolean isDeleted;
}
}

