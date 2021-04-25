// Implementation of Queue using Linked Lists

#include <iostream>
using namespace std;

// Node class
class Node{
    public:
    int data;
    Node *next;
    public:
    Node(int x){
        data = x;
        next = NULL;
    }
};

// Implementing Queue
class Queue{
    public:
    int size, maxlen; // size and max length of the queue
    Node *front, *rear; // Node pointers to point to front and rear nodes
    public:
    Queue(int m){
        // Initially Queue is empty
        size = 0;
        maxlen = m;
        front = rear = NULL; 
    }
    // Insert an element at Rear (Enqueue operation)
    void enqueue(int data){
        // check if the queue is full
        if(size == maxlen){
            cout << "Queue Overflow Error" << endl;
        }
        else{
            // insert element at rear pointer
            Node *new_node = new Node(data);
            new_node->next = rear;
            rear = new_node; // rear is always newly inserted node
            if(size == 0){
                // make front pointer the first inserted node
                front = new_node;
            }
        }
        size++;
    }
    // display Rear of the Queue
    void displayRear(){
        cout << rear->data << endl;
    }
    // display Front of the Queue
    void displayFront()
    {
        cout << front->data << endl;
    }
    // Delete an element from the front of the Queue (Dequeue operation)
    void dequeue(){
        Node *curr = rear;
        Node *prev;
        while (curr != front){
            prev = curr;
            curr = curr->next;
        }
        cout << curr->data << " has been deleted" << endl;
        front = prev; // front is always node to be removed
        prev->next = NULL;
        size--;
    }
};

int main(){
    Queue q(5);
    q.enqueue(1);
    q.enqueue(2);
    q.enqueue(3);
    q.enqueue(4);
    q.displayRear();
    q.displayFront();
    q.dequeue();
    q.displayRear();
    q.displayFront();
    return 0;
}