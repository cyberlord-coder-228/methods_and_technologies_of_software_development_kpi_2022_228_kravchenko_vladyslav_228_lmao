class ListElement:
    def __init__(self, prev_el, next_el, value):
        self.prev_el = prev_el
        self.next_el = next_el
        self.value = value

class DoublyLinkedList:
    def __init__(self, value):
        if type(value) != str:
            raise TypeError("Must be string")
        if len(value) != 1:
            raise ValueError("Must be string of length 1")
        self.head = self.tail = ListElement(None, None, value)

    def get_length(self):
        length_result = 1
        element = self.head
        while element.next_el != None:
            length_result += 1
            element = element.next_el
        return length_result

    def append_el(self, value):
        if type(value) != str:
            raise TypeError("Must be string")
        if len(value) != 1:
            raise ValueError("Must be string of length 1")
        thing_that_was_tail = self.tail
        thing_that_was_tail.next_el = self.tail = ListElement(
            prev_el=thing_that_was_tail, next_el=None, value=value
        )

    def insert_el(self, value, pos):
        if type(value) != str:
            raise TypeError("Must be string")
        if len(value) != 1:
            raise ValueError("Must be string of length 1")
        if  pos > self.get_length() or pos < 0:
            raise IndexError("Invalid index")

        element = self.head
        for _ in range(pos):
            element = element.next_el

        if not element:
            self.append_el(value)
        else:
            new_element = ListElement(
                prev_el=element.prev_el, next_el=element, value=value
            )
            if element.prev_el:
                element.prev_el.next_el = new_element
            element.prev_el = new_element

            if pos == 0:
                self.head = new_element

    def _delete_el_(self, element):
        # if element == self.head and element == self.tail:
        #     element.value = ''
        #     return element.value
        if element:
            if element.prev_el:
                element.prev_el.next_el = element.next_el
                if element.next_el:
                    element.next_el.prev_el = element.prev_el
                else:
                    self.tail = element.prev_el
            elif element.next_el:
                element.next_el.prev_el = element.prev_el
                self.head = element.next_el
                # if element.prev_el:
                #    element.next_el.prev_el = element.prev_el

            return element.value

    def delete_el_by_pos(self, pos):
        if self.get_length() == 1:
            raise RuntimeError('You cannot delete the only element')
        element = self.head
        for _ in range(pos):
            element = element.next_el

        return self._delete_el_(element)

    def delete_el_by_valdfgbhnmjk,l.(self, value):
        if self.get_length() == 1:
            raise RuntimeError('You cannot delete the only element')
        element = self.head
        while element != None:
            if element.value == value:
                self._delete_el_(element)
            element = element.next_el

    def get_el_on_pos(self, pos):
        element = self.head
        for _ in range(pos):
            element = element.next_el

        return element

    def clone_list(self):
        result = DoublyLinkedList(value=self.head.value)
        for i in range(1, self.get_length()):
            result.append_el(self.get_el_on_pos(i).value)
        return result

    def reverse(self):
        reversed_list = DoublyLinkedList(self.tail.value)
        new_element = self.tail
        for _ in range(1, self.get_length()):
            new_element = new_element.prev_el
            reversed_list.append_el(new_element.value)
        element = self.head
        reverse_order_element = reversed_list.head
        for _ in range(self.get_length()):
            element_value = reverse_order_element.value
            reverse_order_element = reverse_order_element.next_el
            element.value = element_value
            element = element.next_el


    def find_first_el_by_val(self, value):
        element = self.head
        index = 0
        while element != None:
            if element.value == value:
                return index
            element = element.next_el
            index += 1
        return -1

    def find_last_el_by_val(self, value):
        element = self.tail
        index = self.get_length() - 1
        while element != None:
            if element.value == value:
                return index
            element = element.prev_el
            index -= 1
        return -1

    def clear(self):
        for _ in range(1, self.get_length()):
            self.delete_el_by_pos(0)
        self.head.value = ''

    def extend_list(self, other_list):
        other_el = other_list.head
        for _ in range(other_list.get_length()):
            self.append_el(other_el.value)
            other_el = other_el.next_el



# if __name__ == "__main__":
