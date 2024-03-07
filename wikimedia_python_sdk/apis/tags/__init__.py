# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from wikimedia_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    TRANSFORM = "Transform"
    EDITED_PAGES_DATA = "Edited pages data"
    BYTES_DIFFERENCE_DATA = "Bytes difference data"
    EDITORS_DATA = "Editors data"
    PAGEVIEWS_DATA = "Pageviews data"
    MATH = "Math"
    EDITS_DATA = "Edits data"
    FEED_CONTENT_AVAILABILITY = "Feed content availability"
    LEGACY_DATA = "Legacy data"
    REGISTERED_USERS_DATA = "Registered users data"
    UNIQUE_DEVICES_DATA = "Unique devices data"
