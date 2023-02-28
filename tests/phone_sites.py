from ._base_test_case import BaseTestCase, zoom_client_test
from zoomdotpy.api.phones.sites import SiteShortExtension, SiteEmergencyAddress

import unittest
from dotenv import load_dotenv
load_dotenv('test.env')

created_site = {}

class PhonesTestCase( BaseTestCase ):
    @zoom_client_test
    def test1_list_sites(self):
        out = self.zc.phones.sites.list_sites()
        print(out)

        return out

    @zoom_client_test
    def test2_create_site(self):
        global created_site

        created_site = self.zc.phones.sites.create_site(
            "TEST-RECEP",
            SiteEmergencyAddress(
                "742 Evergreen Terrace",
                "SPRINGFIELD",
                "US",
                "OR",
                "97477"
            ),
            "TEST-SITE",
            short_extension=SiteShortExtension(
                4
            )
        )
        print(created_site)

        return created_site

    @zoom_client_test
    def test3_get_site(self):
        out = self.zc.phones.sites.get_site(created_site['id'])
        print(out)

        return out
    

if __name__ == '__main__':
    unittest.main()