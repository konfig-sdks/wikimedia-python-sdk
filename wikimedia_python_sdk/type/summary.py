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

from wikimedia_python_sdk.type.originalimage import Originalimage
from wikimedia_python_sdk.type.summary_coordinates import SummaryCoordinates
from wikimedia_python_sdk.type.thumbnail import Thumbnail

class RequiredSummary(TypedDict):
    # The page title
    title: str

    # The page language direction code
    dir: str

    # First several sentences of an article in plain text
    extract: str

    # The page language code
    lang: str

class OptionalSummary(TypedDict, total=False):
    # Wikidata description for the page
    description: str

    coordinates: SummaryCoordinates

    # The page title how it should be shown to the user
    displaytitle: str

    # First several sentences of an article in simple HTML format
    extract_html: str

    originalimage: Originalimage

    # The page ID
    pageid: int

    thumbnail: Thumbnail

    # The time when the page was last editted in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format
    timestamp: str

class Summary(RequiredSummary, OptionalSummary):
    pass
