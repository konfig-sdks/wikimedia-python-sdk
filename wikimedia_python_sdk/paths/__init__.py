# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from wikimedia_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    FEED_AVAILABILITY = "/feed/availability"
    MEDIA_MATH_CHECK_TYPE = "/media/math/check/{type}"
    MEDIA_MATH_FORMULA_HASH = "/media/math/formula/{hash}"
    MEDIA_MATH_RENDER_FORMAT_HASH = "/media/math/render/{format}/{hash}"
    METRICS_BYTESDIFFERENCE_ABSOLUTE_AGGREGATE_PROJECT_EDITORTYPE_PAGETYPE_GRANULARITY_START_END = "/metrics/bytes-difference/absolute/aggregate/{project}/{editor-type}/{page-type}/{granularity}/{start}/{end}"
    METRICS_BYTESDIFFERENCE_ABSOLUTE_PERPAGE_PROJECT_PAGETITLE_EDITORTYPE_GRANULARITY_START_END = "/metrics/bytes-difference/absolute/per-page/{project}/{page-title}/{editor-type}/{granularity}/{start}/{end}"
    METRICS_BYTESDIFFERENCE_NET_AGGREGATE_PROJECT_EDITORTYPE_PAGETYPE_GRANULARITY_START_END = "/metrics/bytes-difference/net/aggregate/{project}/{editor-type}/{page-type}/{granularity}/{start}/{end}"
    METRICS_BYTESDIFFERENCE_NET_PERPAGE_PROJECT_PAGETITLE_EDITORTYPE_GRANULARITY_START_END = "/metrics/bytes-difference/net/per-page/{project}/{page-title}/{editor-type}/{granularity}/{start}/{end}"
    METRICS_EDITEDPAGES_AGGREGATE_PROJECT_EDITORTYPE_PAGETYPE_ACTIVITYLEVEL_GRANULARITY_START_END = "/metrics/edited-pages/aggregate/{project}/{editor-type}/{page-type}/{activity-level}/{granularity}/{start}/{end}"
    METRICS_EDITEDPAGES_NEW_PROJECT_EDITORTYPE_PAGETYPE_GRANULARITY_START_END = "/metrics/edited-pages/new/{project}/{editor-type}/{page-type}/{granularity}/{start}/{end}"
    METRICS_EDITEDPAGES_TOPBYABSOLUTEBYTESDIFFERENCE_PROJECT_EDITORTYPE_PAGETYPE_YEAR_MONTH_DAY = "/metrics/edited-pages/top-by-absolute-bytes-difference/{project}/{editor-type}/{page-type}/{year}/{month}/{day}"
    METRICS_EDITEDPAGES_TOPBYEDITS_PROJECT_EDITORTYPE_PAGETYPE_YEAR_MONTH_DAY = "/metrics/edited-pages/top-by-edits/{project}/{editor-type}/{page-type}/{year}/{month}/{day}"
    METRICS_EDITEDPAGES_TOPBYNETBYTESDIFFERENCE_PROJECT_EDITORTYPE_PAGETYPE_YEAR_MONTH_DAY = "/metrics/edited-pages/top-by-net-bytes-difference/{project}/{editor-type}/{page-type}/{year}/{month}/{day}"
    METRICS_EDITORS_AGGREGATE_PROJECT_EDITORTYPE_PAGETYPE_ACTIVITYLEVEL_GRANULARITY_START_END = "/metrics/editors/aggregate/{project}/{editor-type}/{page-type}/{activity-level}/{granularity}/{start}/{end}"
    METRICS_EDITORS_TOPBYABSOLUTEBYTESDIFFERENCE_PROJECT_EDITORTYPE_PAGETYPE_YEAR_MONTH_DAY = "/metrics/editors/top-by-absolute-bytes-difference/{project}/{editor-type}/{page-type}/{year}/{month}/{day}"
    METRICS_EDITORS_TOPBYEDITS_PROJECT_EDITORTYPE_PAGETYPE_YEAR_MONTH_DAY = "/metrics/editors/top-by-edits/{project}/{editor-type}/{page-type}/{year}/{month}/{day}"
    METRICS_EDITORS_TOPBYNETBYTESDIFFERENCE_PROJECT_EDITORTYPE_PAGETYPE_YEAR_MONTH_DAY = "/metrics/editors/top-by-net-bytes-difference/{project}/{editor-type}/{page-type}/{year}/{month}/{day}"
    METRICS_EDITS_AGGREGATE_PROJECT_EDITORTYPE_PAGETYPE_GRANULARITY_START_END = "/metrics/edits/aggregate/{project}/{editor-type}/{page-type}/{granularity}/{start}/{end}"
    METRICS_EDITS_PERPAGE_PROJECT_PAGETITLE_EDITORTYPE_GRANULARITY_START_END = "/metrics/edits/per-page/{project}/{page-title}/{editor-type}/{granularity}/{start}/{end}"
    METRICS_LEGACY_PAGECOUNTS_AGGREGATE_PROJECT_ACCESSSITE_GRANULARITY_START_END = "/metrics/legacy/pagecounts/aggregate/{project}/{access-site}/{granularity}/{start}/{end}"
    METRICS_PAGEVIEWS_AGGREGATE_PROJECT_ACCESS_AGENT_GRANULARITY_START_END = "/metrics/pageviews/aggregate/{project}/{access}/{agent}/{granularity}/{start}/{end}"
    METRICS_PAGEVIEWS_PERARTICLE_PROJECT_ACCESS_AGENT_ARTICLE_GRANULARITY_START_END = "/metrics/pageviews/per-article/{project}/{access}/{agent}/{article}/{granularity}/{start}/{end}"
    METRICS_PAGEVIEWS_TOPBYCOUNTRY_PROJECT_ACCESS_YEAR_MONTH = "/metrics/pageviews/top-by-country/{project}/{access}/{year}/{month}"
    METRICS_PAGEVIEWS_TOP_PROJECT_ACCESS_YEAR_MONTH_DAY = "/metrics/pageviews/top/{project}/{access}/{year}/{month}/{day}"
    METRICS_REGISTEREDUSERS_NEW_PROJECT_GRANULARITY_START_END = "/metrics/registered-users/new/{project}/{granularity}/{start}/{end}"
    METRICS_UNIQUEDEVICES_PROJECT_ACCESSSITE_GRANULARITY_START_END = "/metrics/unique-devices/{project}/{access-site}/{granularity}/{start}/{end}"
    TRANSFORM_HTML_FROM_FROM_LANG_TO_TO_LANG = "/transform/html/from/{from_lang}/to/{to_lang}"
    TRANSFORM_HTML_FROM_FROM_LANG_TO_TO_LANG_PROVIDER = "/transform/html/from/{from_lang}/to/{to_lang}/{provider}"
    TRANSFORM_LIST_TOOL_TOOL = "/transform/list/tool/{tool}"
    TRANSFORM_LIST_TOOL_TOOL_FROM = "/transform/list/tool/{tool}/{from}"
    TRANSFORM_LIST_TOOL_TOOL_FROM_TO = "/transform/list/tool/{tool}/{from}/{to}"
    TRANSFORM_WORD_FROM_FROM_LANG_TO_TO_LANG_WORD = "/transform/word/from/{from_lang}/to/{to_lang}/{word}"
    TRANSFORM_WORD_FROM_FROM_LANG_TO_TO_LANG_WORD_PROVIDER = "/transform/word/from/{from_lang}/to/{to_lang}/{word}/{provider}"
    TRANSFORM_LIST_LANGUAGEPAIRS = "/transform/list/languagepairs"
    TRANSFORM_LIST_PAIR_FROM_TO = "/transform/list/pair/{from}/{to}"
