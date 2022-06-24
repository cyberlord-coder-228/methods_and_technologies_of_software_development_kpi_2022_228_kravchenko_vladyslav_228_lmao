import unittest 
from lab2 import ListElement, DoublyLinkedList

class TestDDL(unittest.TestCase):
	def test_initiation_not_string(self):
		# Assume
		value = 1
		# Assert
		self.assertRaises(TypeError, DoublyLinkedList.__init__, value)

	def test_initiation_not_a_single_char(self):
		# Assume
		value = 'str'
		# Assert
		self.assertRaises(ValueError, DoublyLinkedList, value)

	def test_append(self):
		# Assume
		ddl = DoublyLinkedList('a')
		value = 'b'
		# Action
		ddl.append_el(value)
		# Assert
		self.assertEqual(ddl.head.next_el.value, value)

	def test_insert(self):
		# Assume
		ddl = DoublyLinkedList('b')
		value_at_zero = 'a'
		value_at_two = 'c'
		# Action
		ddl.insert_el(value=value_at_zero, pos=0)
		ddl.insert_el(value=value_at_two, pos=2)
		# Assert
		self.assertEqual(ddl.head.value, value_at_zero)
		self.assertEqual(ddl.head.next_el.next_el.value, value_at_two)

	def test_insert_invalid_pos(self):
		# Assume
		ddl = DoublyLinkedList('a')
		invalid_pos_one = -1
		invalid_pos_two = 2
		# Assert
		self.assertRaises(IndexError, lambda:ddl.insert_el(value='c', pos=invalid_pos_one))
		self.assertRaises(IndexError, lambda:ddl.insert_el(value='c', pos=invalid_pos_two))

	def test_get_length(self):
		# Assume
		ddl = DoublyLinkedList('a')
		# Assert
		self.assertEqual(ddl.get_length(), 1)
		# Action
		ddl.append_el('b')
		# Assert
		self.assertEqual(ddl.get_length(), 2)

	def test_doesnt_delete_only_element(self):
		# Assume
		ddl = DoublyLinkedList('a')
		# Assert
		self.assertRaises(RuntimeError, lambda:ddl.delete_el_by_pos(0))
		self.assertRaises(RuntimeError, lambda:ddl.delete_el_by_val('a'))

	def test_delete_by_pos(self):
		# Assume
		ddl = DoublyLinkedList('a')
		ddl.append_el('b')
		ddl.append_el('c')
		# Action
		ddl.delete_el_by_pos(1)
		# Assert
		self.assertEqual(ddl.get_length(), 2)
		self.assertEqual(ddl.head.value, 'a')
		self.assertEqual(ddl.head.next_el.value, 'c')
		self.assertEqual(ddl.head.next_el.next_el, None)

	def test_delete_by_pos_first(self):
		# Assume
		ddl = DoublyLinkedList('a')
		ddl.append_el('b')
		ddl.append_el('c')
		# Action
		ddl.delete_el_by_pos(0)
		# Assert
		self.assertEqual(ddl.get_length(), 2)
		self.assertEqual(ddl.head.value, 'b')
		self.assertEqual(ddl.head.next_el.value, 'c')
		self.assertEqual(ddl.head.next_el.next_el, None)
		self.assertEqual(ddl.tail.value, 'c')
		self.assertEqual(ddl.tail.prev_el.value, 'b')
		self.assertEqual(ddl.tail.prev_el.prev_el, None)

	def test_delete_by_pos_last(self):
		# Assume
		ddl = DoublyLinkedList('a')
		ddl.append_el('b')
		ddl.append_el('c')
		# Action
		ddl.delete_el_by_pos(2)
		# Assert
		self.assertEqual(ddl.get_length(), 2)
		self.assertEqual(ddl.head.value, 'a')
		self.assertEqual(ddl.head.next_el.value, 'b')
		self.assertEqual(ddl.head.next_el.next_el, None)
		self.assertEqual(ddl.tail.value, 'b')
		self.assertEqual(ddl.tail.prev_el.value, 'a')
		self.assertEqual(ddl.tail.prev_el.prev_el, None)

	def test_delete_by_val(self):
		# Assume
		ddl = DoublyLinkedList('a')
		ddl.append_el('b')
		ddl.append_el('b')
		ddl.append_el('c')
		# Action
		ddl.delete_el_by_val('b')
		# Assert
		self.assertEqual(ddl.get_length(), 2)
		self.assertEqual(ddl.head.value, 'a')
		self.assertEqual(ddl.head.next_el.value, 'c')
		self.assertEqual(ddl.head.next_el.next_el, None)

	def test_get_el_on_pos(self):
		# Assume
		ddl = DoublyLinkedList('a')
		ddl.append_el('b')
		ddl.append_el('c')
		# Assert
		self.assertEqual(ddl.get_el_on_pos(0).value, 'a')
		self.assertEqual(ddl.get_el_on_pos(1).value, 'b')
		self.assertEqual(ddl.get_el_on_pos(2).value, 'c')

	def test_clone(self):
		# Assume
		ddl = DoublyLinkedList('a')
		ddl.append_el('b')
		ddl.append_el('c')
		# Action
		second_ddl = ddl.clone_list()
		# Assert
		self.assertEqual(second_ddl.get_length(), 3)
		self.assertEqual(second_ddl.get_el_on_pos(0).value, 'a')
		self.assertEqual(second_ddl.get_el_on_pos(1).value, 'b')
		self.assertEqual(second_ddl.get_el_on_pos(2).value, 'c')

	def test_reverse(self):
		# Assume
		ddl = DoublyLinkedList('a')
		ddl.append_el('b')
		ddl.append_el('c')
		# Action
		ddl.reverse()
		# Assert
		self.assertEqual(ddl.get_length(), 3)
		self.assertEqual(ddl.get_el_on_pos(0).value, 'c')
		self.assertEqual(ddl.get_el_on_pos(1).value, 'b')
		self.assertEqual(ddl.get_el_on_pos(2).value, 'a')

	def test_find_first_el_by_val_value(self):
		# Assume
		ddl = DoublyLinkedList('a')
		ddl.append_el('b')
		ddl.append_el('b')
		ddl.append_el('c')
		# Assert
		self.assertEqual(ddl.find_first_el_by_val('b'), 1)

	def test_find_first_el_by_val_value_not_in_the_list(self):
		# Assume
		ddl = DoublyLinkedList('a')
		ddl.append_el('b')
		ddl.append_el('c')
		# Assert
		self.assertEqual(ddl.find_first_el_by_val('m'), -1)

	def test_find_last_el_by_val_value(self):
		# Assume
		ddl = DoublyLinkedList('a')
		ddl.append_el('b')
		ddl.append_el('b')
		ddl.append_el('c')
		# Assert
		self.assertEqual(ddl.find_last_el_by_val('b'), 2)

	def test_find_last_el_by_val_value_not_in_the_list(self):
		# Assume
		ddl = DoublyLinkedList('a')
		ddl.append_el('b')
		ddl.append_el('c')
		# Assert
		self.assertEqual(ddl.find_last_el_by_val('m'), -1)

	def test_clear(self):
		# Assume
		ddl = DoublyLinkedList('a')
		ddl.append_el('b')
		ddl.append_el('c')
		# Action
		ddl.clear()
		# Assert
		self.assertEqual(ddl.get_length(), 1)
		self.assertEqual(ddl.get_el_on_pos(0).value, '')
		self.assertEqual(ddl.tail.value, '')
		self.assertEqual(ddl.head.value, '')

	def test_extend(self):
		# Assume
		ddl_a = DoublyLinkedList('a')
		ddl_a.append_el('b')
		ddl_a.append_el('c')
		ddl_b = DoublyLinkedList('d')
		ddl_b.append_el('e')
		ddl_b.append_el('f')
		# Action
		ddl_a.extend_list(ddl_b)
		# Assert
		self.assertEqual(ddl_a.get_length(), 6)
		self.assertEqual(ddl_a.get_el_on_pos(0).value, 'a')
		self.assertEqual(ddl_a.get_el_on_pos(1).value, 'b')
		self.assertEqual(ddl_a.get_el_on_pos(2).value, 'c')
		self.assertEqual(ddl_a.get_el_on_pos(3).value, 'd')
		self.assertEqual(ddl_a.get_el_on_pos(4).value, 'e')
		self.assertEqual(ddl_a.get_el_on_pos(5).value, 'f')
		self.assertEqual(ddl_b.get_el_on_pos(0).value, 'd')
		self.assertEqual(ddl_b.get_el_on_pos(1).value, 'e')
		self.assertEqual(ddl_b.get_el_on_pos(2).value, 'f')
		self.assertEqual(ddl_a.head.value, 'a')
		self.assertEqual(ddl_a.tail.value, 'f')

	def test_extend_changes_in_second(self):
		# Assume
		ddl_a = DoublyLinkedList('a')
		ddl_a.append_el('b')
		ddl_a.append_el('c')
		ddl_b = DoublyLinkedList('d')
		ddl_b.append_el('e')
		ddl_b.append_el('f')
		# Action
		ddl_a.extend_list(ddl_b)

		ddl_b.head.value = 'j'
		ddl_b.delete_el_by_pos(2)
		ddl_b.tail.value = 'f'
		ddl_b.append_el('k')
		# Assert
		self.assertEqual(ddl_a.get_length(), 6)
		self.assertEqual(ddl_a.get_el_on_pos(0).value, 'a')
		self.assertEqual(ddl_a.get_el_on_pos(1).value, 'b')
		self.assertEqual(ddl_a.get_el_on_pos(2).value, 'c')
		self.assertEqual(ddl_a.get_el_on_pos(3).value, 'd')
		self.assertEqual(ddl_a.get_el_on_pos(4).value, 'e')
		self.assertEqual(ddl_a.get_el_on_pos(5).value, 'f')
		self.assertEqual(ddl_b.get_el_on_pos(0).value, 'j')
		self.assertEqual(ddl_b.get_el_on_pos(1).value, 'f')
		self.assertEqual(ddl_b.get_el_on_pos(2).value, 'k')
		self.assertEqual(ddl_a.head.value, 'a')
		self.assertEqual(ddl_a.tail.value, 'f')
		
		