# coding: utf-8
"""
    Wikimedia

    This API provides cacheable and straightforward access to Wikimedia content and data, in machine-readable formats. ### Global Rules - Limit your clients to no more than 200 requests/s to this API.   Each API endpoint's documentation may detail more specific usage limits. - Set a unique `User-Agent` or `Api-User-Agent` header that   allows us to contact you quickly. Email addresses or URLs   of contact pages work well.  By using this API, you agree to Wikimedia's  [Terms of Use](https://wikimediafoundation.org/wiki/Terms_of_Use) and [Privacy Policy](https://wikimediafoundation.org/wiki/Privacy_policy). Unless otherwise specified in the endpoint documentation below, content accessed via this API is licensed under the [CC-BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)  and [GFDL](https://www.gnu.org/copyleft/fdl.html) licenses, and you irrevocably agree to release modifications or additions made through this API under these licenses.  See https://www.mediawiki.org/wiki/REST_API for background and details. ### Endpoint documentation Please consult each endpoint's documentation for details on: - Licensing information for the specific type of content   and data served via the endpoint. - Stability markers to inform you about development status and   change policy, according to   [our API version policy](https://www.mediawiki.org/wiki/API_versioning). - Endpoint specific usage limits. 

    The version of the OpenAPI document: 1.0.0
    Created by: http://mediawiki.org/wiki/REST_API
"""

import typing
import inspect
from datetime import date, datetime
from wikimedia_python_sdk.client_custom import ClientCustom
from wikimedia_python_sdk.configuration import Configuration
from wikimedia_python_sdk.api_client import ApiClient
from wikimedia_python_sdk.type_util import copy_signature
from wikimedia_python_sdk.apis.tags.bytes_difference_data_api import BytesDifferenceDataApi
from wikimedia_python_sdk.apis.tags.edited_pages_data_api import EditedPagesDataApi
from wikimedia_python_sdk.apis.tags.editors_data_api import EditorsDataApi
from wikimedia_python_sdk.apis.tags.edits_data_api import EditsDataApi
from wikimedia_python_sdk.apis.tags.feed_content_availability_api import FeedContentAvailabilityApi
from wikimedia_python_sdk.apis.tags.legacy_data_api import LegacyDataApi
from wikimedia_python_sdk.apis.tags.math_api import MathApi
from wikimedia_python_sdk.apis.tags.pageviews_data_api import PageviewsDataApi
from wikimedia_python_sdk.apis.tags.registered_users_data_api import RegisteredUsersDataApi
from wikimedia_python_sdk.apis.tags.transform_api import TransformApi
from wikimedia_python_sdk.apis.tags.unique_devices_data_api import UniqueDevicesDataApi



class Wikimedia(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.bytes_difference_data: BytesDifferenceDataApi = BytesDifferenceDataApi(api_client)
        self.edited_pages_data: EditedPagesDataApi = EditedPagesDataApi(api_client)
        self.editors_data: EditorsDataApi = EditorsDataApi(api_client)
        self.edits_data: EditsDataApi = EditsDataApi(api_client)
        self.feed_content_availability: FeedContentAvailabilityApi = FeedContentAvailabilityApi(api_client)
        self.legacy_data: LegacyDataApi = LegacyDataApi(api_client)
        self.math: MathApi = MathApi(api_client)
        self.pageviews_data: PageviewsDataApi = PageviewsDataApi(api_client)
        self.registered_users_data: RegisteredUsersDataApi = RegisteredUsersDataApi(api_client)
        self.transform: TransformApi = TransformApi(api_client)
        self.unique_devices_data: UniqueDevicesDataApi = UniqueDevicesDataApi(api_client)
