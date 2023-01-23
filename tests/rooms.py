from ._base_test_case import BaseTestCase, zoom_client_test

import unittest
from dotenv import load_dotenv
load_dotenv('test.env')


class RoomsTestCase( BaseTestCase ):
    @zoom_client_test
    def test1_list_rooms(self):
        return self.zc.rooms.list_rooms()
    

if __name__ == '__main__':
    unittest.main()