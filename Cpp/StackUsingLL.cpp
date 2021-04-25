// Implementation of a stack using Linked Lists
#include <iostream>
using namespace std;

// Implementation of a node class
class Node{
    public:
    int data; // to contain data
    Node *next; // Node pointer to point to next node
    public:
    Node(int x){
        data = x;
        next = NULL;
    }
};

// Implementation of Stack
class Stack{
    public:
    int maxlen; // maximum length of a stack
    int top; // variable to denote the topmost element of the stack
    Node *head; // first node in a stack
    public:
    Stack(int m){
        maxlen = m;
        top = -1; //top is -1 (convention) for an empty stack
        head = NULL; //head is null for an empty list
    }
    // Function to insert an element into the stack
    void push(int data){
        //check if the stack is full
        if(top == maxlen - 1){
            cout << "Stack Overflow Error" << endl;
        }
        else{
            // make a new node
            Node *new_node = new Node(data);
            // if there is no node in stack, make it first node
            if(head == NULL && top == -1){head = new_node;}
            else
            {
                //traverse to the end of the stack
                Node *curr = head;
                while(curr->next != NULL){curr = curr->next;}
                //add the new node there
                curr->next = new_node;
                new_node->next = NULL;
            }
            top++;
        }
    }
    // Function to view the topmost element
    void peek(){
        Node *curr = head; //pointer to the head node
        while(curr != NULL){
            //traversing till the last node
            cout << curr->data << "-->";
            curr = curr->next;
        }
        cout<<endl;
    }
    // Function to delete the topmost element
    void pop(){
        //check if the stack is empty
        if(top == -1){cout << "Stack Underflow Error" << endl;}
        else{
            Node *curr = head; //pointer to the head node
            Node *prev; //pointer to the second last node after traversal
            while (curr->next != NULL){
                //traversing till the last node
                prev = curr;
                curr = curr->next;
            }
            // deletion of curr
            prev->next = NULL;
            top--;
        }
    }
};

int main(){
    Stack st(5);
    st.push(1);
    st.push(2);
    st.peek();
    st.pop();
    st.peek();
    return 0;
}