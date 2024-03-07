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

from wikimedia_python_sdk.model.problem import Problem as ProblemSchema
from wikimedia_python_sdk.model.transform_content_machine_translate_request import TransformContentMachineTranslateRequest as TransformContentMachineTranslateRequestSchema
from wikimedia_python_sdk.model.cx_mt import CxMt as CxMtSchema

from wikimedia_python_sdk.type.transform_content_machine_translate_request import TransformContentMachineTranslateRequest
from wikimedia_python_sdk.type.problem import Problem
from wikimedia_python_sdk.type.cx_mt import CxMt

from ...api_client import Dictionary
from wikimedia_python_sdk.pydantic.transform_content_machine_translate_request import TransformContentMachineTranslateRequest as TransformContentMachineTranslateRequestPydantic
from wikimedia_python_sdk.pydantic.problem import Problem as ProblemPydantic
from wikimedia_python_sdk.pydantic.cx_mt import CxMt as CxMtPydantic

from . import path

# Path params
FromLangSchema = schemas.StrSchema
ToLangSchema = schemas.StrSchema


class ProviderSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "Apertium": "APERTIUM",
            "Yandex": "YANDEX",
            "Youdao": "YOUDAO",
        }
    
    @schemas.classproperty
    def APERTIUM(cls):
        return cls("Apertium")
    
    @schemas.classproperty
    def YANDEX(cls):
        return cls("Yandex")
    
    @schemas.classproperty
    def YOUDAO(cls):
        return cls("Youdao")
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'from_lang': typing.Union[FromLangSchema, str, ],
        'to_lang': typing.Union[ToLangSchema, str, ],
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
request_path_provider = api_client.PathParameter(
    name="provider",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ProviderSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationXWwwFormUrlencoded = TransformContentMachineTranslateRequestSchema


request_body_transform_content_machine_translate_request = api_client.RequestBody(
    content={
        'application/x-www-form-urlencoded': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXWwwFormUrlencoded),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = CxMtSchema
SchemaFor200ResponseBodyApplicationProblemjson = CxMtSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: CxMt


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: CxMt


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

    def _content_machine_translate_0_mapped_args(
        self,
        html: str,
        from_lang: str,
        to_lang: str,
        provider: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if html is not None:
            _body["html"] = html
        args.body = _body
        if from_lang is not None:
            _path_params["from_lang"] = from_lang
        if to_lang is not None:
            _path_params["to_lang"] = to_lang
        if provider is not None:
            _path_params["provider"] = provider
        args.path = _path_params
        return args

    async def _acontent_machine_translate_0_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/x-www-form-urlencoded',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Machine-translate content
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/transform/html/from/{from_lang}/to/{to_lang}/{provider}',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_transform_content_machine_translate_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


    def _content_machine_translate_0_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/x-www-form-urlencoded',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Machine-translate content
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/transform/html/from/{from_lang}/to/{to_lang}/{provider}',
            body=body,
            headers=_headers,
        )
        serialized_data = request_body_transform_content_machine_translate_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
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


class ContentMachineTranslate0Raw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acontent_machine_translate_0(
        self,
        html: str,
        from_lang: str,
        to_lang: str,
        provider: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._content_machine_translate_0_mapped_args(
            html=html,
            from_lang=from_lang,
            to_lang=to_lang,
            provider=provider,
        )
        return await self._acontent_machine_translate_0_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def content_machine_translate_0(
        self,
        html: str,
        from_lang: str,
        to_lang: str,
        provider: str,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._content_machine_translate_0_mapped_args(
            html=html,
            from_lang=from_lang,
            to_lang=to_lang,
            provider=provider,
        )
        return self._content_machine_translate_0_oapg(
            body=args.body,
            path_params=args.path,
        )

class ContentMachineTranslate0(BaseApi):

    async def acontent_machine_translate_0(
        self,
        html: str,
        from_lang: str,
        to_lang: str,
        provider: str,
        validate: bool = False,
        **kwargs,
    ) -> CxMtPydantic:
        raw_response = await self.raw.acontent_machine_translate_0(
            html=html,
            from_lang=from_lang,
            to_lang=to_lang,
            provider=provider,
            **kwargs,
        )
        if validate:
            return CxMtPydantic(**raw_response.body)
        return api_client.construct_model_instance(CxMtPydantic, raw_response.body)
    
    
    def content_machine_translate_0(
        self,
        html: str,
        from_lang: str,
        to_lang: str,
        provider: str,
        validate: bool = False,
    ) -> CxMtPydantic:
        raw_response = self.raw.content_machine_translate_0(
            html=html,
            from_lang=from_lang,
            to_lang=to_lang,
            provider=provider,
        )
        if validate:
            return CxMtPydantic(**raw_response.body)
        return api_client.construct_model_instance(CxMtPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        html: str,
        from_lang: str,
        to_lang: str,
        provider: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._content_machine_translate_0_mapped_args(
            html=html,
            from_lang=from_lang,
            to_lang=to_lang,
            provider=provider,
        )
        return await self._acontent_machine_translate_0_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        html: str,
        from_lang: str,
        to_lang: str,
        provider: str,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._content_machine_translate_0_mapped_args(
            html=html,
            from_lang=from_lang,
            to_lang=to_lang,
            provider=provider,
        )
        return self._content_machine_translate_0_oapg(
            body=args.body,
            path_params=args.path,
        )

