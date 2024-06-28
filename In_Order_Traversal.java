import java.util.*;

// TreeNode class definition
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    
    TreeNode(int x) {
        val = x;
        left = null;
        right = null;
    }
}

// BinaryTree class to handle parsing and traversal
class BinaryTree {
    // Function to perform inorder traversal and return result as a list
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root != null) {
            result.addAll(inorderTraversal(root.left));
            result.add(root.val);
            result.addAll(inorderTraversal(root.right));
        }
        return result;
    }
    
    // Function to build binary tree from level-order input
    public TreeNode buildTree(String[] nodes) {
        if (nodes.length == 0 || nodes[0].equals("-1")) {
            return null;
        }
        
        Queue<TreeNode> queue = new LinkedList<>();
        TreeNode root = new TreeNode(Integer.parseInt(nodes[0]));
        queue.offer(root);
        int index = 1;
        
        while (!queue.isEmpty() && index < nodes.length) {
            TreeNode node = queue.poll();
            
            // Left child
            if (!nodes[index].equals("-1")) {
                node.left = new TreeNode(Integer.parseInt(nodes[index]));
                queue.offer(node.left);
            }
            index++;
            
            // Right child
            if (index < nodes.length && !nodes[index].equals("-1")) {
                node.right = new TreeNode(Integer.parseInt(nodes[index]));
                queue.offer(node.right);
            }
            index++;
        }
        
        return root;
    }
    
    // Function to parse input and build the tree
    public TreeNode parseInputToTree(String input) {
        String[] nodes = input.trim().split("\\s+");
        return buildTree(nodes);
    }
    
    // Function to print inorder traversal result
    public void inorderPrint(TreeNode root) {
        List<Integer> result = inorderTraversal(root);
        for (int i = 0; i < result.size(); i++) {
            System.out.print(result.get(i));
            if (i < result.size() - 1) {
                System.out.print(" ");
            }
        }
        System.out.println();
    }
}

// Main class to handle input/output
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        BinaryTree binaryTree = new BinaryTree();
        
        // Parse input and build the binary tree
        TreeNode root = binaryTree.parseInputToTree(input);
        
        // Perform inorder traversal and print the result
        binaryTree.inorderPrint(root);
        
        scanner.close();
    }
}
