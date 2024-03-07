# coding: utf-8

"""
    Wikimedia

    This API provides cacheable and straightforward access to Wikimedia content and data, in machine-readable formats. ### Global Rules - Limit your clients to no more than 200 requests/s to this API.   Each API endpoint's documentation may detail more specific usage limits. - Set a unique `User-Agent` or `Api-User-Agent` header that   allows us to contact you quickly. Email addresses or URLs   of contact pages work well.  By using this API, you agree to Wikimedia's  [Terms of Use](https://wikimediafoundation.org/wiki/Terms_of_Use) and [Privacy Policy](https://wikimediafoundation.org/wiki/Privacy_policy). Unless otherwise specified in the endpoint documentation below, content accessed via this API is licensed under the [CC-BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)  and [GFDL](https://www.gnu.org/copyleft/fdl.html) licenses, and you irrevocably agree to release modifications or additions made through this API under these licenses.  See https://www.mediawiki.org/wiki/REST_API for background and details. ### Endpoint documentation Please consult each endpoint's documentation for details on: - Licensing information for the specific type of content   and data served via the endpoint. - Stability markers to inform you about development status and   change policy, according to   [our API version policy](https://www.mediawiki.org/wiki/API_versioning). - Endpoint specific usage limits. 

    The version of the OpenAPI document: 1.0.0
    Created by: http://mediawiki.org/wiki/REST_API
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from wikimedia_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from wikimedia_python_sdk.api_response import AsyncGeneratorResponse
from wikimedia_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from wikimedia_python_sdk import schemas  # noqa: F401

from wikimedia_python_sdk.model.cx_dict import CxDict as CxDictSchema
from wikimedia_python_sdk.model.problem import Problem as ProblemSchema

from wikimedia_python_sdk.type.problem import Problem
from wikimedia_python_sdk.type.cx_dict import CxDict

from ...api_client import Dictionary
from wikimedia_python_sdk.pydantic.problem import Problem as ProblemPydantic
from wikimedia_python_sdk.pydantic.cx_dict import CxDict as CxDictPydantic

from . import path

# Path params
FromLangSchema = schemas.StrSchema
ToLangSchema = schemas.StrSchema
WordSchema = schemas.StrSchema


class ProviderSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "JsonDict": "JSON_DICT",
            "Dictd": "DICTD",
        }
    
    @schemas.classproperty
    def JSON_DICT(cls):
        return cls("JsonDict")
    
    @schemas.classproperty
    def DICTD(cls):
        return cls("Dictd")
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'from_lang': typing.Union[FromLangSchema, str, ],
        'to_lang': typing.Union[ToLangSchema, str, ],
        'word': typing.Union[WordSchema, str, ],
        'provider': typing.Union[ProviderSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_from_lang = api_client.PathParameter(
    name="from_lang",
    style=api_client.ParameterStyle.SIMPLE,
    schema=FromLangSchema,
    required=True,
)
request_path_to_lang = api_client.PathParameter(
    name="to_lang",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ToLangSchema,
    required=True,
)
request_path_word = api_client.PathParameter(
    name="word",
    style=api_client.ParameterStyle.SIMPLE,
    schema=WordSchema,
    required=True,
)
request_path_provider = api_client.PathParameter(
    name="provider",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ProviderSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = CxDictSchema
SchemaFor200ResponseBodyApplicationProblemjson = CxDictSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: CxDict


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: CxDict


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
        'application/problem+json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationProblemjson),
    },
)
SchemaFor0ResponseBodyApplicationJson = ProblemSchema
SchemaFor0ResponseBodyApplicationProblemjson = ProblemSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: Problem


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: Problem


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationJson),
        'application/problem+json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationProblemjson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'application/json',
    'application/problem+json',
)


class BaseApi(api_client.Api):

    def _get_dictionary_meaning_0_mapped_args(
        self,
        from_lang: str,
        to_lang: str,
        word: str,
        provider: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if from_lang is not None:
            _path_params["from_lang"] = from_lang
        if to_lang is not None:
            _path_params["to_lang"] = to_lang
        if word is not None:
            _path_params["word"] = word
        if provider is not None:
            _path_params["provider"] = provider
        args.path = _path_params
        return args

    async def _aget_dictionary_meaning_0_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Fetch the dictionary meaning of a word
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_from_lang,
            request_path_to_lang,
            request_path_word,
            request_path_provider,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/transform/word/from/{from_lang}/to/{to_lang}/{word}/{provider}',
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserializationAsync(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _get_dictionary_meaning_0_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Fetch the dictionary meaning of a word
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_from_lang,
            request_path_to_lang,
            request_path_word,
            request_path_provider,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/transform/word/from/{from_lang}/to/{to_lang}/{word}/{provider}',
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class GetDictionaryMeaning0Raw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_dictionary_meaning_0(
        self,
        from_lang: str,
        to_lang: str,
        word: str,
        provider: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_dictionary_meaning_0_mapped_args(
            from_lang=from_lang,
            to_lang=to_lang,
            word=word,
            provider=provider,
        )
        return await self._aget_dictionary_meaning_0_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get_dictionary_meaning_0(
        self,
        from_lang: str,
        to_lang: str,
        word: str,
        provider: str,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_dictionary_meaning_0_mapped_args(
            from_lang=from_lang,
            to_lang=to_lang,
            word=word,
            provider=provider,
        )
        return self._get_dictionary_meaning_0_oapg(
            path_params=args.path,
        )

class GetDictionaryMeaning0(BaseApi):

    async def aget_dictionary_meaning_0(
        self,
        from_lang: str,
        to_lang: str,
        word: str,
        provider: str,
        validate: bool = False,
        **kwargs,
    ) -> CxDictPydantic:
        raw_response = await self.raw.aget_dictionary_meaning_0(
            from_lang=from_lang,
            to_lang=to_lang,
            word=word,
            provider=provider,
            **kwargs,
        )
        if validate:
            return CxDictPydantic(**raw_response.body)
        return api_client.construct_model_instance(CxDictPydantic, raw_response.body)
    
    
    def get_dictionary_meaning_0(
        self,
        from_lang: str,
        to_lang: str,
        word: str,
        provider: str,
        validate: bool = False,
    ) -> CxDictPydantic:
        raw_response = self.raw.get_dictionary_meaning_0(
            from_lang=from_lang,
            to_lang=to_lang,
            word=word,
            provider=provider,
        )
        if validate:
            return CxDictPydantic(**raw_response.body)
        return api_client.construct_model_instance(CxDictPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        from_lang: str,
        to_lang: str,
        word: str,
        provider: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_dictionary_meaning_0_mapped_args(
            from_lang=from_lang,
            to_lang=to_lang,
            word=word,
            provider=provider,
        )
        return await self._aget_dictionary_meaning_0_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        from_lang: str,
        to_lang: str,
        word: str,
        provider: str,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_dictionary_meaning_0_mapped_args(
            from_lang=from_lang,
            to_lang=to_lang,
            word=word,
            provider=provider,
        )
        return self._get_dictionary_meaning_0_oapg(
            path_params=args.path,
        )

