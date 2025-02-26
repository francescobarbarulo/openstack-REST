# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestFlavorsController(BaseTestCase):
    """FlavorsController integration test stubs"""

    def test_get_flavors(self):
        """Test case for get_flavors

        Get flavors
        """
        response = self.client.open(
            '/v1/flavors',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
