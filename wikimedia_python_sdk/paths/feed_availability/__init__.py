# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from wikimedia_python_sdk.paths.feed_availability import Api

from wikimedia_python_sdk.paths import PathValues

path = PathValues.FEED_AVAILABILITY