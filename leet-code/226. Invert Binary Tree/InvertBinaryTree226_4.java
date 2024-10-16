import java.util.ArrayDeque;
import java.util.Deque;

public class InvertBinaryTree226_4 {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;

        Deque<TreeNode> deq = new ArrayDeque<>();
        deq.push(root);

        while (!deq.isEmpty()) {
            TreeNode node = deq.poll();
            TreeNode temp = node.left;
            node.left = node.right;
            node.right = temp;

            if (node.left != null) deq.push(node.left);
            if (node.right != null) deq.push(node.right);
        }

        return root;
    }
}
