import typing_extensions

from wikimedia_python_sdk.apis.tags import TagValues
from wikimedia_python_sdk.apis.tags.transform_api import TransformApi
from wikimedia_python_sdk.apis.tags.edited_pages_data_api import EditedPagesDataApi
from wikimedia_python_sdk.apis.tags.bytes_difference_data_api import BytesDifferenceDataApi
from wikimedia_python_sdk.apis.tags.editors_data_api import EditorsDataApi
from wikimedia_python_sdk.apis.tags.pageviews_data_api import PageviewsDataApi
from wikimedia_python_sdk.apis.tags.math_api import MathApi
from wikimedia_python_sdk.apis.tags.edits_data_api import EditsDataApi
from wikimedia_python_sdk.apis.tags.feed_content_availability_api import FeedContentAvailabilityApi
from wikimedia_python_sdk.apis.tags.legacy_data_api import LegacyDataApi
from wikimedia_python_sdk.apis.tags.registered_users_data_api import RegisteredUsersDataApi
from wikimedia_python_sdk.apis.tags.unique_devices_data_api import UniqueDevicesDataApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.TRANSFORM: TransformApi,
        TagValues.EDITED_PAGES_DATA: EditedPagesDataApi,
        TagValues.BYTES_DIFFERENCE_DATA: BytesDifferenceDataApi,
        TagValues.EDITORS_DATA: EditorsDataApi,
        TagValues.PAGEVIEWS_DATA: PageviewsDataApi,
        TagValues.MATH: MathApi,
        TagValues.EDITS_DATA: EditsDataApi,
        TagValues.FEED_CONTENT_AVAILABILITY: FeedContentAvailabilityApi,
        TagValues.LEGACY_DATA: LegacyDataApi,
        TagValues.REGISTERED_USERS_DATA: RegisteredUsersDataApi,
        TagValues.UNIQUE_DEVICES_DATA: UniqueDevicesDataApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.TRANSFORM: TransformApi,
        TagValues.EDITED_PAGES_DATA: EditedPagesDataApi,
        TagValues.BYTES_DIFFERENCE_DATA: BytesDifferenceDataApi,
        TagValues.EDITORS_DATA: EditorsDataApi,
        TagValues.PAGEVIEWS_DATA: PageviewsDataApi,
        TagValues.MATH: MathApi,
        TagValues.EDITS_DATA: EditsDataApi,
        TagValues.FEED_CONTENT_AVAILABILITY: FeedContentAvailabilityApi,
        TagValues.LEGACY_DATA: LegacyDataApi,
        TagValues.REGISTERED_USERS_DATA: RegisteredUsersDataApi,
        TagValues.UNIQUE_DEVICES_DATA: UniqueDevicesDataApi,
    }
)
