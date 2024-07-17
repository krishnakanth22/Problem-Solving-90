/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution {
    public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {
        Set<Integer> valsToDelete = new HashSet<>();
        List<TreeNode> result = new ArrayList<>();

        for (int number : to_delete)
            valsToDelete.add(number);

        if (!valsToDelete.contains(root.val))
            result.add(root);
        shouldDelete(result, valsToDelete, root);
        return result;
    }
    public TreeNode shouldDelete(List<TreeNode> result, Set<Integer> valsToDelete, TreeNode root) {
        if (root == null)
            return null;

        root.left = shouldDelete(result, valsToDelete, root.left);
        root.right = shouldDelete(result, valsToDelete, root.right);

        if (valsToDelete.contains(root.val)) {
            if (root.left != null) 
                result.add(root.left);
            if (root.right != null)
                result.add(root.right);
            return null;
        }

        return root;
    }
}
