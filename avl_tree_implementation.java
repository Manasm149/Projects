// AVL Tree Node
class Node {
    int key;
    Node left, right;
    int height;

    public Node(int item) {
        key = item;
        left = right = null;
        height = 1;
    }
}

public class AVLTree {
    private Node root;

    // Get the height of the tree
    private int height(Node node) {
        if (node == null)
            return 0;
        return node.height;
    }

    // Get the balance factor of a node
    private int getBalanceFactor(Node node) {
        if (node == null)
            return 0;
        return height(node.left) - height(node.right);
    }

    // Right rotate the subtree rooted with y
    private Node rightRotate(Node y) {
        Node x = y.left;
        Node T2 = x.right;

        // Perform rotation
        x.right = y;
        y.left = T2;

        // Update heights
        y.height = Math.max(height(y.left), height(y.right)) + 1;
        x.height = Math.max(height(x.left), height(x.right)) + 1;

        // Return new root
        return x;
    }

    // Left rotate the subtree rooted with x
    private Node leftRotate(Node x) {
        Node y = x.right;
        Node T2 = y.left;

        // Perform rotation
        y.left = x;
        x.right = T2;

        // Update heights
        x.height = Math.max(height(x.left), height(x.right)) + 1;
        y.height = Math.max(height(y.left), height(y.right)) + 1;

        // Return new root
        return y;
    }

    // Insert a key into the subtree rooted with node and return the new root
    public Node insert(Node node, int key) {
        // 1. Perform the normal BST insertion
        if (node == null)
            return new Node(key);

        if (key < node.key)
            node.left = insert(node.left, key);
        else if (key > node.key)
            node.right = insert(node.right, key);
        else
            return node; // Duplicate keys are not allowed

        // 2. Update the height of this ancestor node
        node.height = 1 + Math.max(height(node.left), height(node.right));

        // 3. Get the balance factor of this ancestor node to check whether this node became unbalanced
        int balance = getBalanceFactor(node);

        // If this node becomes unbalanced, then there are 4 cases

        // Left Left Case
        if (balance > 1 && key < node.left.key)
            return rightRotate(node);

        // Right Right Case
        if (balance < -1 && key > node.right.key)
            return leftRotate(node);

        // Left Right Case
        if (balance > 1 && key > node.left.key) {
            node.left = leftRotate(node.left);
            return rightRotate(node);
        }

        // Right Left Case
        if (balance < -1 && key < node.right.key) {
            node.right = rightRotate(node.right);
            return leftRotate(node);
        }

        // Return the (unchanged) node pointer
        return node;
    }

    // Insert a key into the AVL Tree
    public void insert(int key) {
        root = insert(root, key);
    }

    // Preorder traversal of the tree
    public void preOrder(Node node) {
        if (node != null) {
            System.out.print(node.key + " ");
            preOrder(node.left);
            preOrder(node.right);
        }
    }

    // Wrapper for preOrder traversal
    public void preOrder() {
        preOrder(root);
    }

    public static void main(String[] args) {
        AVLTree tree = new AVLTree();

        // Inserting nodes
        tree.insert(10);
        tree.insert(20);
        tree.insert(30);
        tree.insert(15);
        tree.insert(25);

        // Print preorder traversal of the AVL tree
        System.out.println("Preorder traversal of the constructed AVL tree:");
        tree.preOrder();
    }
}
