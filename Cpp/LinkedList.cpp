// Implementation of a Linked List in C++
#include <iostream>
using namespace std;

// Implementation of a Node
class Node{
    public:
        Node *next; // Node pointer to point to next node
        int data; // Integer stored in each node
    public:
        Node(int x){
            data = x; // storing the data
            next = NULL; // pointer to next node is null by default
        }
};
// Implementation of a Linked List Class
class SingleLinkedList{
    private:
    int listsize; // variable to store size of list
    Node *head; // Node pointer to point to head node
    public:
    // constructor to initialise the list
    SingleLinkedList(){
        head = NULL;
        listsize = 0;
    }
    // Function to insert an element at the start
    void insertionAtHead(int data){
        Node *new_node = new Node(data); // create a new node
        // if the list is empty new node is head node
        if(head == NULL){
            head = new_node;
        }
        else{
            // link the new node to head
            new_node->next = head;
            head = new_node;
        }
        listsize++;
    }
    // Function to insert an element at the end
    void insertionAtTail(int data){
        Node *new_node = new Node(data); // Create a new node
        // if the list is empty new node is head node
        if (head == NULL){
            head = new_node;
        }
        else{
            // link the last node of the linked list to the new node
            Node *curr = head; //current pointer to head node
            while(curr->next != NULL){
                // traverse till last node is reached
                curr = curr->next;
            }
            curr->next = new_node;
            listsize++;
        }
    }
    // Function to insert at a user specified position
    void insertionAtPos(int pos, int data){
        if (pos < 0 && pos > listsize + 1){
            // check is pos is a valid position in the list
            cout << pos << " does not exist in the list" << endl;
        }
        else{
            if (pos == 0){
                // insert at head
                insertionAtHead(data);
            }
            else if (pos == listsize + 1){
                //insertion at tail
                insertionAtTail(data);
            }
            else{
                // insert anywhere else
                Node *new_node = new Node(data); // new node
                Node *curr = head; // pointer to the head node
                Node *prev = head; //pointer to store previous node
                int count = 0; //count positions till pos
                while(curr != NULL){
                    if(count == pos){break;}
                    count++;
                    prev = curr;
                    curr = curr->next;
                }
                // insertion between prev and curr if pos is found
                if (curr != NULL)
                {
                    prev->next = new_node;
                    new_node->next = curr;
                }
            }
            listsize++;
        }
    }
    //Function to delete head node of a linked list
    void deletionAtHead(){
        if(head == NULL){
            cout << "List is empty"<< endl;
        }
        else{
            cout << head->data << " has been deleted" << endl;
            Node *after = head->next; //pointer to point to next of head node
            head->next = NULL; //de-link head node from the rest of the list
            head = after; //set next node as the head node, or NULL
            listsize--;
        }   
    }
    // Function to delete the tail node of a linked list
    void deletionAtTail(){
        if (head == NULL){
            cout << "List is empty" << endl;
        }
        else{
            //traverse to the last node
            Node *curr = head; // pointer to the head node
            Node *prev; //pointer to the second last node after traversal
            while(curr->next != NULL){
                //traverses till last node
                prev = curr;
                curr = curr->next;
            }
            //deletion of curr
            cout << curr->data << " has been deleted" << endl;
            prev->next = NULL;
            listsize--;
        }
    }
    //Function to delete key specified by user
    void deleteKey(int key){
        if (head == NULL){
            cout << "List is empty" << endl;
        }
        else{
            //if key is at head
            if(head->data == key){deletionAtHead();}
            else{
                //traverse to the last node
                Node *curr = head; // pointer to the head node
                Node *prev; //pointer to the second last node after traversal
                while (curr != NULL){
                    if(curr->data == key){break;}
                    prev = curr;
                    curr = curr->next;
                }
                if(curr != NULL){
                    //deletion of curr
                    cout << curr->data << " has been deleted" << endl;
                    Node *temp = curr->next;
                    curr->next = NULL;
                    prev->next = temp;
                }
                else{
                    cout << key << " does not exist" << endl;
                }
            }
        }
    }
    // Function to display the linked list
    void display(){
        Node *curr = head;
        while(curr != NULL){
            cout << curr->data << "-->";
            curr = curr->next;
        }
        cout << "Null" << endl;
    }
};

int main(){
    SingleLinkedList L;
    L.insertionAtHead(1);
    L.insertionAtTail(2);
    L.insertionAtPos(3,3);
    L.insertionAtTail(4);
    L.display();
    L.deletionAtHead();
    L.deletionAtTail();
    L.deleteKey(3);
    L.display();
    return 0;
}