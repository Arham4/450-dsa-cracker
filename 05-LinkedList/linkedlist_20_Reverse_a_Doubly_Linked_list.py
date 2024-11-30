def reverseDLL(self, head):
    curr = head
    while curr:
        temp = curr.next
        curr.next = curr.prev
        curr.prev = temp
        if temp:
            curr = temp
        else:
            break
    return curr
