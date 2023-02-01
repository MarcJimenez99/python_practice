# Since we know both lists are sorted we can iterate using pointers and 
# read both lists from their beginnings and take the lowest value we read
# from both and use that to construct our list.

# First we will create a dummyNode that acts as a pointer to the head of 
# our output linked list so we always know the head of our newly
# constructed list. We will set it to an empty ListNode() and then create
# another pointer that we will call tail that will always point to the
# last node in our newly constructed list. For now it will begin to point 
# at the head since it is the only node in our list. Now we will iterate 
# over both of our lists until one of the list pointers reached the end of its
# list, or equals null. On each loop we will look at each current node of 
# both our list pointers and see the value that exists at both and whatever
# is lower we will point our tail's next pointer to that node and also
# point that node's list pointer at the next node in the list. At the end of
# each iteration of our while loop we will also point our tail at the new
# end of our new merged list. Now once we've reached the end of one of our
# lists, we will still have remaining nodes in the other list. We will simply
# append those nodes by setting our tail's next pointer to the list pointer
# that is still pointing to a valid node, and since we know the list is sorted
# we know the end of the remaining list has not only the correct values, 
# but also connections set until that linked list's end. 

# Finally we can return the head's next pointer to get the head or beginning
# of our newly merged linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_sorted_lists(list1, list2):
    head = ListNode()
    tail = head
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    else:
        tail.next = list2
    
    return head.next

def main():

    x = ListNode(1)
    x.next = ListNode(4)
    x.next.next = ListNode(5)
    list1 = x

    y = ListNode(1)
    y.next = ListNode(3)
    y.next.next = ListNode(4)
    list2 = y

    merged_list = merge_two_sorted_lists(list1, list2)
    output = []
    while merged_list:
        output.append(merged_list.val)
        merged_list = merged_list.next
    print(output)


if __name__ == "__main__":
    main()

