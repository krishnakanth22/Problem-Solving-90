    dummy = ListNode()
    current = dummy

    # Loop until one of the lists becomes empty
    while list1 and list2:
        # Compare the values of the current nodes in both lists
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        # Move the current pointer to the next node in the merged list
        current = current.next

    # If one of the lists is not empty, append the remaining nodes
    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    # Return the head of the merged list (excluding the dummy node)
    return dummy.next
