// Implementation of a Queue using Array 
#include <iostream>
using namespace std;

class Queue{
    public:
    int front, rear, size;
    int *arr; // the array used to implement the queue
    int maxlen;
    public:
    Queue(int m){
        maxlen = m;
        arr = new int[m];
        front = 0; // set to the first index of arr
        rear = m - 1; // set to the last index of arr
        size = 0;
    }
    // Insert into the Queue (EnQueue Operation)
    void enqueue(int data){
        // Check for overflow: Front reaches Rear
        if(size == maxlen){
            cout << "Queue Overflow Error" << endl; 
        }
        else{
            rear = (rear + 1) % maxlen; // Incrementing Rear
            // Item is added to the Rear of the Queue
            arr[rear] = data;
            size++;
        }
    }
    // Display front element of the queue
    void displayFront(){
        cout << arr[front] << endl;
    }
    // Display rear element of the queue
    void displayRear(){
        cout << arr[rear] << endl;
    }
    // Delete an element from the Queue (DeQueue Operation)
    void dequeue(){
        // Check for underflow: Front exceeds Rear
        if(size == 0){
            cout << "Queue Underflow Error" << endl;
        }
        else{
            // Item is removed from the Front of the Queue
            cout << arr[front] << " was deleted" << endl;
            front = (front + 1) % maxlen; // Incrementing Front
            size--;
        }
    }
};

int main(){
    Queue q(5);
    q.enqueue(1);
    q.enqueue(2);
    q.displayFront();
    q.displayRear();
    q.dequeue();
    q.enqueue(3);
    q.displayFront();
    q.displayRear();
    return 0;
}