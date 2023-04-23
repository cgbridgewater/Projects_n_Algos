

class Node{
    constructor(val){
        this.val = val // node value
        this.next = null // node position
    }
}


class SL{
    constructor(head = null){
        this.head = head // designates this as the head
    }

    addFront(val){
        let newNode = new Node(val)
        newNode.next = this.head // points to next head
        this.head = newNode // assigns new node to head
        return this // allows chaining functions
    }

    printStringValue(){
        let result = ""
        let runner = this.head
        while(runner != null){
            // console.log(runner.val)
            result = result.concat(" ", runner.val)
            runner = runner.next
        }
        return result
    }
}

let sl = new SL()
sl.addFront(76).addFront(2)

result = sl.printStringValue()
console.log(result);

sl.addFront(11.41)

result = sl.printStringValue()
console.log(result);