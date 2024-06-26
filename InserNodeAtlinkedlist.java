import java.util.*;
class Main
{
  static Node head = null, tail = null;
  static class Node{
    int data;
    Node next;
    Node(int val){
      data = val;
      next = null;
    }
  }
  public static void insert(int val){
    Node newNode = new Node(val);
    if(head==null){
      head = newNode;
      tail = newNode;
    }
    else{
      tail.next = newNode;
      tail = newNode;
    }
  }
  public static void display(){
    Node temp = head;
    while(temp!=null){
      System.out.println(temp.data);
      temp = temp.next;
    }
  }
  public static void main(String args[])
  {
    Scanner sc = new Scanner(System.in);
    Main ob = new Main();
    int a = 1;
    while(a!=-1){
      a = sc.nextInt();
      if(a==-1){
        break;
      }
      ob.insert(a);
    }
    ob.display();
  }
}
