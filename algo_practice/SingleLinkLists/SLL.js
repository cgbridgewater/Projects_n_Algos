// class Node {
//     constructor(data){
//         this.data=data;
//         this.next=null;
//     }
// }


// class LinkedList {
//     constructor() {
//         this.head = null;
//     }


//     addFront(val) {
//         // Creating a new node object with the value provided
//         let new_node = new Node(val);
//         // Checking to see if the current list does not have a head node (if the list is empty)
//         // If the list is empty, place the new node as the head 
//         if(!this.head) {
//             this.head = new_node;
//             return this;
//         }
//         // If the list is not empty, assign the head to be the next node to the new node (Blue Arrow in picture above)
//         new_node.next = this.head;
//         // Then finally assign the new_node to be the new head of the list (Red Arrow in picture above)
//         this.head = new_node;
//         return this;
//     }
// }


// LinkedList.addFront(18);
// console.log(LinkedList);

// Node Constructor
class Node{
    constructor(val){
        this.val = val // node value
        this.next = null // node position
    }
}

// SLL Constructor
class SLL{
    constructor(head = null){
        this.head = head // designates this as the head
    }
    //
    addFront(val){
        let newNode = new Node(val)
        newNode.next = this.head // points to next head
        this.head = newNode // assigns new node to head
        return this // allows chaining functions
    }
    // printList(){
    //     while(this.head != null){
    //         console.log(this.head.val)
    //         this.head = this.head.next
    //     }
    //     return this
    // }
    isEmpty(){
        // console.log('I work', this);
        return this.head === null
    }
    insertAtBack(val){
        let newNode = new Node(val)
        let runner = this.head
        while(runner.next){
            runner = runner.next
        }
        runner.next = newNode
        return this
    }

    printValue(){
        let runner = this.head
        while(runner != null){
            console.log(runner.val)
            runner = runner.next
        }
        return this
    }


}


const node1 = new Node(8)

let SL = new SLL(new Node(10))
SL.addFront(2).addFront(4).addFront(6).addFront(15)
// console.log('print list');
// SL.printList()
console.log('SL print value');
SL.printValue()

console.log("is empty :",SL.isEmpty(), SL.head);

let SL2 = new SLL(new Node(10))
SL2.addFront(12).addFront(14)
SL2.insertAtBack(20)
// console.log("print list");
// SL2.printList()
console.log("SL2 print value");
SL2.printValue()