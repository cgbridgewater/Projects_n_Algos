// Add Front
// Write a method that accepts a value and create a new node, assign it to the list head, and return a pointer to the new head node.

class Node{
    constructor(val){
        this.val = val
        this.next = null
    }
}

class SLL {
    constructor(head= null){
        this.head = head
    }

    addFront(val){
        let newNode = new Node(val)
        newNode.next = this.head 
        this.head = newNode 
        return this
    }

    removeFront(){
        let runner = this.head
        runner = runner.next
        this.head = runner
        return this
    }

    front(){
        if (this.head ===null){
            return null
        }
        return this.head.val
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

let SLL1 = new SLL()
SLL1.addFront(18).addFront(5).addFront(73)

SLL1.printValue()

console.log("take out the front");
SLL1.removeFront()
SLL1.printValue()

console.log("sll2");
let SLL2 = new SLL()
SLL2.addFront(18)
SLL2.printValue()
SLL2.removeFront()
SLL2.printValue()
let front = SLL2.front()
console.log("front:", front);