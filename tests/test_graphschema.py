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

from dozer.graphschema import Attribute, _validate_required, \
	_validate_unique

class TestAttribute(unittest.TestCase):

	def test_Attribute_construction(self):
		# this needs more structure
		# validate Domain on Attribute?
		# Enforce assignment of alias?
		unit_domain = Domain('http://example.com','string')
		unit = Attribute(unit_domain)
		self.assertIn('uri', dir(unit))
		self.assertIn('validators', dir(unit))
		self.assertIn('conformers', dir(unit))
		self.assertEqual(unit.uri, unit_domain.uri)

	def test_required(self):
		x = ['listitem']
		self.assertEqual(x, _validate_required(x))
		with self.assertRaises(ValueError):
			badlist = []
			_validate_required(badlist)

	def test_unique(self):
		x = ['listitem']
		self.assertEqual(x, _validate_unique(x))
		with self.assertRaises(ValueError):
			badlist = ['too','many']
			_validate_unique(badlist)

	def test_always(self):
		always = ['any','values']
		unit_domain = Domain('http://example.com','string')
		unit = Attribute(unit_domain, always=always)
		# test 1
		test_1 = []
		conformed_1 = unit._conform_always(test_1)
		self.assertEqual(len(always), len(conformed_1))
		for val in always:
			self.assertIn(val, conformed_1)
		# test 2
		test_2 = [1,'other',4.00]
		conformed_2 = unit._conform_always(test_2)
		self.assertEqual(len(always) + len(test_2), len(conformed_2))
		for val in test_2:
			self.assertIn(val, conformed_2)
		for val in always:
			self.assertIn(val, conformed_2)

	def test_allowed(self):
		allowed = ['permitted','values']
		unit_domain = Domain('http://example.com','string')
		unit = Attribute(unit_domain, allowed=allowed)
		# test 1
		test_1 = []
		conformed_1 = unit._conform_allowed(test_1)
		self.assertEqual(len(test_1), len(conformed_1))
		# test 2
		test_2 = ['permitted','values',1,'other',4.00]
		conformed_2 = unit._conform_allowed(test_2)
		self.assertEqual(len(allowed), len(conformed_2))
		for val in test_2:
			if val not in allowed:
				self.assertNotIn(val, conformed_2)
		for val in test_2:
			if val in allowed:
				self.assertIn(val, conformed_2)
		for val in allowed:
			if val in test_2:
				self.assertIn(val, conformed_2)
		# test 3
		test_3 = ['permitted', 'other']
		conformed_3 = unit._conform_allowed(test_3)
		self.assertGreater(len(test_3), len(conformed_3))
		for val in test_3:
			if val not in allowed:
				self.assertNotIn(val, conformed_3)
		for val in test_3:
			if val in allowed:
				self.assertIn(val, conformed_3)
		for val in allowed:
			if val in test_3:
				self.assertIn(val, conformed_3)

	def test_only(self):
		only = ['only','values']
		unit_domain = Domain('http://example.com','string')
		unit = Attribute(unit_domain, only=only)
		# test 1
		test_1 = []
		conformed_1 = unit._conform_only(test_1)
		self.assertEqual(len(only), len(conformed_1))
		for val in only:
			self.assertIn(val, conformed_1)
		# test 2
		test_2 = [1,'other',4.00]
		conformed_2 = unit._conform_only(test_2)
		self.assertEqual(len(only), len(conformed_2))
		for val in only:
			self.assertIn(val, conformed_2)
		for val in test_2:
			self.assertNotIn(val, conformed_2)

from dozer.graphschema import Schema

class TestSchema(unittest.TestCase):

	def test_Schema_construction(self):
		pass


if __name__ == "__main__":
	unittest.main()