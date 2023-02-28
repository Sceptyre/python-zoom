import logging
import zoomclient
import unittest
import os

def zoom_client_test(func: callable):
    def inner(self, *args, **kwargs):
        self.logger.info(f"{func.__name__}")

        out = func( self, *args, **kwargs )
        if out.get('code') and out.get('message'):
            raise Exception(out['message'])

        self.assertTrue( True )

    return inner

class BaseTestCase( unittest.TestCase ):
    def setUp(self) -> None:
        self.logger = logging.getLogger( self.__class__.__name__ )
        logging.basicConfig( level=logging.INFO )
        
        self.zc = zoomclient.ZoomClient(
            os.getenv("TEST_ACCOUNT"),
            os.getenv("TEST_KEY"),
            os.getenv("TEST_SECRET")
        )