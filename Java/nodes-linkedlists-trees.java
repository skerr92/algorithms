// Java nodes and whatnot
public static void main(String args[]) {
  System.out.println("Hello World");
}

static class node {
  private int data;
  private node next;
  node(int d) {
    data = d;
    next = null;
  }
  
  node(int d, node p) {
    data = d;
    next = p;
  }
  
  public void setNext(node p) {
    next = p;
  }
  
}

static class LinkedList {
  private node head;
  private node tail;
  
  LinkedList(node p) {
    head = p;
    tail = null;
  }
  
  LinkedList(node p, node r) {
    head = p;
    tail = r;
  }
  
  public void insertAtHead(node p) {
    p.setNext(head);
  }
 
}
