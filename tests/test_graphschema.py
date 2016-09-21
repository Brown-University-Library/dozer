import unittest
import context

from dozer.graphschema import Domain, _validate_uri, \
	_validate_int, _validate_datetime, _validate_string

class TestDomain(unittest.TestCase):
	
	def test_validate_uri(self):
		# expects a scheme and netloc
		# technically, a url
		uri = "http://example.com"
		self.assertEqual(uri, _validate_uri(uri))
		with self.assertRaises(ValueError):
			bad_uri = "//this.is.not.a.uri"
			_validate_uri(bad_uri)

	def test_validate_datetime(self):
		# deferring to python datetime isoformat,
		# not JavaScript Date's toJSON method:
		# 2012-04-23T18:25:43.511Z
		# which includes microsecond + timezone
		dt = "1994-11-05T13:15:30"
		self.assertEqual(dt, _validate_datetime(dt))
		with self.assertRaises(ValueError):
			bad_dt = "1994-11-05"
			_validate_datetime(bad_dt)

	def test_validate_string(self):
		# requires utf-8
		# this needs to be smarter
		st = "String"
		self.assertEqual(st, _validate_string(st))
		with self.assertRaises(UnicodeError):
			bad_st = u"\u3053\n".encode('utf-16')
			_validate_string(bad_st)

	def test_validate_int(self):
		# requires python int
		itg = 9
		self.assertEqual(itg, _validate_int(itg))
		with self.assertRaises(ValueError):
			bad_itg = "9"
			_validate_int(bad_itg)

	def test_Domain_construction(self):
		uri = 'http://example.com'
		datatype = 'string'
		unit = Domain(uri, datatype)
		self.assertIn('uri', dir(unit))
		self.assertIn('datatype', dir(unit))
		self.assertIn('validator', dir(unit))
		self.assertEqual(uri, unit.uri)
		self.assertEqual(datatype, unit.datatype)
		self.assertEqual(unit.validator, _validate_string)

	def test_invalid_Domain(self):
		# Bad uri
		with self.assertRaises(ValueError):
			unit = Domain('//baduri','int')
		# Bad datatype
		with self.assertRaises(ValueError):
			unit = Domain('http://example', 'spam')

if __name__ == "__main__":
	unittest.main()