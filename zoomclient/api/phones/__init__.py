from .sites import PhoneSitesAPI
from .devices import PhoneDevicesAPI

from zoomclient.api.base import _BaseAPI

class PhonesAPI(_BaseAPI):
    devices: PhoneDevicesAPI
    sites: PhoneSitesAPI

    def __post_init__(self):
        self.devices    = PhoneDevicesAPI(self._s)
        self.sites      = PhoneSitesAPI(self._s)