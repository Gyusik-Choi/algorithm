public class DiameterOfBinaryTree543 {
    public static int maxDiameter = 1;

    public int diameterOfBinaryTree(TreeNode root) {
        int result = traverse(root);
        int answer = maxDiameter - 1;
        // maxDiameter 초기화
        maxDiameter = 1;
        return answer;
    }

    public int traverse(TreeNode root) {
        if (root == null) return 0;
        int left = traverse(root.left);
        int right = traverse(root.right);
        // 현재 정점까지의 최대 diameter 는 max + 1 + min
        maxDiameter = Math.max(maxDiameter, Math.max(left, right) + 1 + Math.min(left, right));
        // 현재 정점의 최대 깊이는 max + 1
        return Math.max(left, right) + 1;
    }
}
