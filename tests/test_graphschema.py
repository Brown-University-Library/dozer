import unittest
import context

from dozer.graphschema import Predicate, _validate_uri, \
	_validate_int, _validate_datetime, _validate_string

class TestPredicate(unittest.TestCase):

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


if __name__ == "__main__":
	unittest.main()