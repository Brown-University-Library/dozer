import unittest
import context


from dozer.graphmap import Resource, _add_missing_keys, \
	_flag_missing_data

class TestResource(unittest.TestCase):

	def test_add_missing_keys(self):
		data = { 'abc': 123, 'def': 456 }
		missing = [ 'needed', 'omitted', 'required' ]
		filled_in = _add_missing_keys(data, missing)
		self.assertIn('abc', filled_in)
		self.assertIn('def', filled_in)
		self.assertIn('needed', filled_in)
		self.assertEqual(filled_in['omitted'], [])
		self.assertEqual(
			len(filled_in.keys()),
				len(data.keys()) + len(missing))

	def test_flag_missing_data(self):
		data = { 'abc': 123, 'def': None, 'xyz': list() }
		flagged = _flag_missing_data(data)
		self.assertEqual(len(data.keys()), len(flagged.keys()))
		self.assertEqual(data['abc'], flagged['abc'])
		self.assertNotEqual(data['def'], flagged['def'])
		self.assertEqual(flagged['def'], [None])
		self.assertEqual(flagged['def'], flagged['xyz'])


from dozer.graphmap import Collection, _rename_dictionary_keys

class TestCollection(unittest.TestCase):

	def test_rename_dictionary_keys(self):
		current = { 'abc': 'mno', 'def': 'xyz' }
		change_to = { 'abc': 123, 'def': 456 }
		renamed = _rename_dictionary_keys(current, change_to)
		self.assertNotIn('abc', renamed)
		self.assertNotIn('def', renamed)
		self.assertIn(123, renamed)
		self.assertIn(456, renamed)
		self.assertEqual(renamed[123], 'mno')
		self.assertEqual(renamed[456], 'xyz')

if __name__ == "__main__":
	unittest.main()