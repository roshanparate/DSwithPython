from Node import Node

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):

        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def print(self):
        if self.head is None:
            print('Linked List is empty')
            return

        itr = self.head
        litr = ''
        while itr:
            litr += str(itr.data) +'-->'
            itr =itr.next

        print(litr)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_count(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self,index):

        if index < 0 or index >= self.get_count():
            raise Exception("Invalid index provided")

        if index ==0:
            self.head = self.head.next

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self,index, data):
        if index < 0 or index >= self.get_count():
            raise Exception("Invalid index provided")

        if index == 0:
           self.insert_at_end(data)
           return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            print('Linked List is empty')
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert,itr.next)
                itr.next = node
                break

            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            print('Linked List is empty')
            return

        if self.head.data == data:
            self.head == self.head.next
            return

        itr = self.head
        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next



if __name__ == '__main__':
    ll = Linkedlist()
    ll.insert_at_begining(10)
    ll.insert_at_begining(112)
    ll.insert_at_begining(10156)

    ll.insert_at_end(85)
    ll.insert_at_end(95)
    ll.insert_at_end(105)

    ll.print()

    lll = Linkedlist()

    lll.insert_values(["one", "two", "three", "four"])
    lll.print()
    print(lll.get_count())
    lll.remove_at(1)
    lll.print()
    lll.insert_at(1, 'one')
    lll.insert_at(3, 'four_1')

    lll.insert_after_value('three', 'three_1')
    lll.print()
    lll.remove_by_value('three_1')
    lll.print()



