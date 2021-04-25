// Implement a stack using arrays in C++

#include <iostream>
using namespace std;

class Stack {
    // class variables for the stack
    private: // access specifiers so these variables cannot be accessed outside
    int maxlen, top;
    int *arr; // serves as the stack
    // constructor to initialise the stack
    public:
    Stack(int maxlength){
        maxlen = maxlength; // maximum size of the stack
        top = -1; // keeps track of the last element (-1 represents empty)
        arr = new int[maxlength]; // stack
    }
    // insert element into the "top" of the stack
    void push(int data){
        if (top != maxlen - 1) {
            // condition to check if stack is full
            arr[top] = data;
            cout << data << " has been inserted" << endl;
            top++; // one element has been added
        }
        else {
            cout << "Stack Overflow Error" << endl;
        }
    }
    // display the last entered element of the stack
    void peek(){
        cout << arr[top] << endl;
    }
    // delete an element from the "top" of the stack
    void pop(){
        if(top == -1){
            cout << "Stack Underflow Error" << endl;
        }
        else {
            cout << arr[top] << " has been deleted" << endl;
            top--; // one element has been decreased
        }
    }
};

int main(){
    Stack st(5);
    st.push(1);
    st.pop();
    st.pop();
    return 0;
}
