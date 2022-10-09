class Node:
    # Initialize the node of the linked list
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        # Initialize
        self.head = None

    def print_forward(self):
    # This method prints list in forward direction. Use node.next
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head  # Start with the head
        llstr = ''   # Start string
        while itr:   # Iterate over every node
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next  # use node.next
        print(llstr)
    
    def print_backward(self):
    # Print linked list in reverse direction. Use node.prev for this.
        if self.head is None:
            print("Linked list is empty")
            return 
        
        itr = self.head  
        while itr.next:       # Iterate over every node until reaching the end
            itr = itr.next
        
        llstr = ''
        while itr:            # Iterate from the last node
            #print(itr.data)
            llstr += str(itr.data)+' <-- ' if itr.prev else str(itr.data)
            itr = itr.prev    # Go backwards
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        # Populate the head node
        node = Node(data, self.head, None)
        self.head = node  

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head

        while itr.next:       # Iterate until reaching the end
            itr = itr.next

        itr.next = Node(data, None, itr)  # Fill the next node with itr as the previous one

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1: # iterate until reaching 1 before the desired index
                
                node = Node(data, itr.next, itr)  # Edit the next node
                itr.next = node

                itr.next.next.prev = itr.next # Edit the next next previous node
                
                break

            itr = itr.next
            count += 1
        

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                itr.next.prev = itr
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node
        indicator = 0
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next, itr)
                itr.next = node
                itr.next.next.prev = itr.next
                indicator = 1
                break

            itr = itr.next

        if indicator == 0:
            print("No element with value: ", data_after)
    
    def remove_by_value(self, data):
    # Remove first node that contains data
        count = 0
        indicator = 0
        itr = self.head
        while itr:
            if itr.data == data:
                self.remove_at(count)
                indicator = 1
                break
            itr = itr.next
            count += 1
        
        if indicator == 0:
            print("No element with value: ", data)
             
    



if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.insert_at(1,"blueberry")
    ll.print_backward()
    ll.print_forward()
    ll.remove_at(2)
    ll.print_forward()
    ll.insert_after_value("grapes","watermelon")
    ll.print_forward()
    ll.remove_by_value("blueberry")
    ll.print_backward()

    ll.insert_values([45,7,12,567,99])
    ll.insert_at_end(67)
    ll.print_forward()
    ll.print_backward()

