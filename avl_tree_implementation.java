import java.util.*;
import java.lang.*;
import java.io.*;
class Node{
    int val;
    Node left, right;
    int height;
    public Node(int item){
        val = item;
        height = 1;
        left = right = null;
    }
}
class AVLTree
{
    private Node root;
    private int height(Node node){
        if(node == null) return 0;
        return node.height;
    }
    private int getBalanceFactor(Node node){
        if(node == null) return 0;
        return height(node.left) - height(node.right);
    }
    private Node rightrotate(Node y){
        Node x = y.left;
        Node t2 = y.right;
        //perform rotation
        x.right = y;
        y.left = t2;
        y.height = Math.max(height(y.left),height(y.right))+1;
        x.height = Math.max(height(x.left),height(x.right))+1;
        return x;
        
    }
    private Node leftrotate(Node y){
        Node x  = y.right;
        Node t2 = y.left;
        //perform rotation
        x.left = y;
        y.right = t2;
        y.height = Math.max(height(y.left),height(y.right))+1;
        x.height = Math.max(height(x.left),height(x.right))+1;
        return x;
    }
    public void insert(int key) {
        root = insert(root, key);
    }
    private Node insert(Node node , int key){
       //  step 1. to perform normal bst insertion
       if(node == null) return new Node(key);
       if(node.val >  key) node.left =  insert(node.left, key);
       else if(node.val < key) node.right =  insert(node.right,key);
       else return node;
       // step 2: height Updation 
       node.height = Math.max(height(node.left),height(node.right))+1;
       int balance  = getBalanceFactor(node);
       if(balance > 1 && key < node.left.val){ // this is the left left case and so we right rotate
           return rightrotate(node);
       }
       if(balance < -1 && key > node.right.val){
           return leftrotate(node);
       }
       // now we talk about the left right case 
       if(balance > 1 && key  > node.left.val){
           node.left  = leftrotate(node.left);
           return rightrotate(node);
    }
        if(balance < -1 &&  key  < node.right.val){
            node.right = rightrotate(node.right);
            return leftrotate(node);
        }
        return node;
    }
    public void preOrder(Node node) {
        if (node != null) {
            System.out.print(node.val + " ");
            preOrder(node.left);
            preOrder(node.right);
        }
    }
    private Node minValueNode(Node node) {
        Node current = node;
        while (current.left != null) {
            current = current.left;
        }
        return current;
    }
    public void preOrder() {
        preOrder(root);
    }
    public Node delete(Node node, int key){
        if(node == null) return null;
        if(key  < node.val){
            node.left  = delete(node.left, key);
        }
        else if(key > node.val){
            node.right = delete(node.right,key);
    }
        else{
            // we first handle the case with no or 1 children
            if(node.left == null || node.right == null){
                Node temp = null;
                if(node.left != null){
                    temp  = node.left;
                }
                if(node.right != null){
                    temp = node.right;
                }
                if(temp == null){
                    node =  null;
                }
                else{
                    node = temp;
                }
            }
            else{
            Node temp = minValueNode(node.right);
            node.val = temp.val;
            node.right = delete(node.right, temp.val);
        }
        }
        if(node == null) return node;
        node.height  = Math.max(height(node.left),height(node.right))+1;
        int balance = getBalanceFactor(node);
        if(balance > 1 && getBalanceFactor(node.left) >= 0){
            return rightrotate(node);
        }
        if(balance < -1 && getBalanceFactor(node.right) <= 0){
            return leftrotate(node);
            }
        if(balance > 1 && getBalanceFactor(node.left) < 0){
            node.left = leftrotate(node.left);
            return rightrotate(node);
        }
        if(balance < -1 && getBalanceFactor(node.right) > 0){
            node.right  = rightrotate(node.right);
            return leftrotate(node);
        }
        return node;
    }
    public void delete(int key) {
        root = delete(root, key);
    }
	public static void main (String[] args) throws java.lang.Exception
	{AVLTree tree = new AVLTree();

        // Inserting nodes
        tree.insert(10);
        tree.insert(20);
        tree.insert(30);
        tree.insert(15);
        tree.insert(25);

        // Print preorder traversal of the AVL tree
        System.out.println("Preorder traversal of the constructed AVL tree:");
        tree.preOrder();
         tree.delete(20);

        // Print preorder traversal of the AVL tree after deletion
        System.out.println("\nPreorder traversal of the AVL tree after deletion:");
        tree.preOrder();


	}
}
