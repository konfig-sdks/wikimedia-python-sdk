# coding: utf-8

"""
    Wikimedia

    This API provides cacheable and straightforward access to Wikimedia content and data, in machine-readable formats. ### Global Rules - Limit your clients to no more than 200 requests/s to this API.   Each API endpoint's documentation may detail more specific usage limits. - Set a unique `User-Agent` or `Api-User-Agent` header that   allows us to contact you quickly. Email addresses or URLs   of contact pages work well.  By using this API, you agree to Wikimedia's  [Terms of Use](https://wikimediafoundation.org/wiki/Terms_of_Use) and [Privacy Policy](https://wikimediafoundation.org/wiki/Privacy_policy). Unless otherwise specified in the endpoint documentation below, content accessed via this API is licensed under the [CC-BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)  and [GFDL](https://www.gnu.org/copyleft/fdl.html) licenses, and you irrevocably agree to release modifications or additions made through this API under these licenses.  See https://www.mediawiki.org/wiki/REST_API for background and details. ### Endpoint documentation Please consult each endpoint's documentation for details on: - Licensing information for the specific type of content   and data served via the endpoint. - Stability markers to inform you about development status and   change policy, according to   [our API version policy](https://www.mediawiki.org/wiki/API_versioning). - Endpoint specific usage limits. 

    The version of the OpenAPI document: 1.0.0
    Created by: http://mediawiki.org/wiki/REST_API
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from wikimedia_python_sdk.type.availability_in_the_news import AvailabilityInTheNews
from wikimedia_python_sdk.type.availability_most_read import AvailabilityMostRead
from wikimedia_python_sdk.type.availability_on_this_day import AvailabilityOnThisDay
from wikimedia_python_sdk.type.availability_picture_of_the_day import AvailabilityPictureOfTheDay
from wikimedia_python_sdk.type.availability_todays_featured_article import AvailabilityTodaysFeaturedArticle

class RequiredAvailability(TypedDict):
    in_the_news: AvailabilityInTheNews

    most_read: AvailabilityMostRead

    on_this_day: AvailabilityOnThisDay

    picture_of_the_day: AvailabilityPictureOfTheDay

    todays_featured_article: AvailabilityTodaysFeaturedArticle

class OptionalAvailability(TypedDict, total=False):
    pass

class Availability(RequiredAvailability, OptionalAvailability):
    pass
