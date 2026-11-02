from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.app_api_key_create import AppAPIKeyCreate
from ...models.post_app_api_key_response_201 import PostAppAPIKeyResponse201
from ...models.post_app_api_key_response_400 import PostAppAPIKeyResponse400
from ...models.post_app_api_key_response_401 import PostAppAPIKeyResponse401
from ...models.post_app_api_key_response_403 import PostAppAPIKeyResponse403
from ...models.post_app_api_key_response_422 import PostAppAPIKeyResponse422
from ...models.post_app_api_key_response_500 import PostAppAPIKeyResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: AppAPIKeyCreate | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/app-api-key",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostAppAPIKeyResponse201 | PostAppAPIKeyResponse400 | PostAppAPIKeyResponse401 | PostAppAPIKeyResponse403 | PostAppAPIKeyResponse422 | PostAppAPIKeyResponse500 | None:
    if response.status_code == 201:
        response_201 = PostAppAPIKeyResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostAppAPIKeyResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostAppAPIKeyResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostAppAPIKeyResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostAppAPIKeyResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostAppAPIKeyResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostAppAPIKeyResponse201 | PostAppAPIKeyResponse400 | PostAppAPIKeyResponse401 | PostAppAPIKeyResponse403 | PostAppAPIKeyResponse422 | PostAppAPIKeyResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AppAPIKeyCreate | Unset = UNSET,

) -> Response[PostAppAPIKeyResponse201 | PostAppAPIKeyResponse400 | PostAppAPIKeyResponse401 | PostAppAPIKeyResponse403 | PostAppAPIKeyResponse422 | PostAppAPIKeyResponse500]:
    r""" Generates an App API Key for the application.

     Metadata does not contain the App API Key secret. A user with the \"Manage App
    API Keys\" permission can manage the metadata for all users. A user with the
    \"Browse App API Keys\" permission can view the metadata for all users.

    Args:
        body (AppAPIKeyCreate | Unset): AppAPIKeyCreate defines an App API Key creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAppAPIKeyResponse201 | PostAppAPIKeyResponse400 | PostAppAPIKeyResponse401 | PostAppAPIKeyResponse403 | PostAppAPIKeyResponse422 | PostAppAPIKeyResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: AppAPIKeyCreate | Unset = UNSET,

) -> PostAppAPIKeyResponse201 | PostAppAPIKeyResponse400 | PostAppAPIKeyResponse401 | PostAppAPIKeyResponse403 | PostAppAPIKeyResponse422 | PostAppAPIKeyResponse500 | None:
    r""" Generates an App API Key for the application.

     Metadata does not contain the App API Key secret. A user with the \"Manage App
    API Keys\" permission can manage the metadata for all users. A user with the
    \"Browse App API Keys\" permission can view the metadata for all users.

    Args:
        body (AppAPIKeyCreate | Unset): AppAPIKeyCreate defines an App API Key creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAppAPIKeyResponse201 | PostAppAPIKeyResponse400 | PostAppAPIKeyResponse401 | PostAppAPIKeyResponse403 | PostAppAPIKeyResponse422 | PostAppAPIKeyResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AppAPIKeyCreate | Unset = UNSET,

) -> Response[PostAppAPIKeyResponse201 | PostAppAPIKeyResponse400 | PostAppAPIKeyResponse401 | PostAppAPIKeyResponse403 | PostAppAPIKeyResponse422 | PostAppAPIKeyResponse500]:
    r""" Generates an App API Key for the application.

     Metadata does not contain the App API Key secret. A user with the \"Manage App
    API Keys\" permission can manage the metadata for all users. A user with the
    \"Browse App API Keys\" permission can view the metadata for all users.

    Args:
        body (AppAPIKeyCreate | Unset): AppAPIKeyCreate defines an App API Key creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAppAPIKeyResponse201 | PostAppAPIKeyResponse400 | PostAppAPIKeyResponse401 | PostAppAPIKeyResponse403 | PostAppAPIKeyResponse422 | PostAppAPIKeyResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: AppAPIKeyCreate | Unset = UNSET,

) -> PostAppAPIKeyResponse201 | PostAppAPIKeyResponse400 | PostAppAPIKeyResponse401 | PostAppAPIKeyResponse403 | PostAppAPIKeyResponse422 | PostAppAPIKeyResponse500 | None:
    r""" Generates an App API Key for the application.

     Metadata does not contain the App API Key secret. A user with the \"Manage App
    API Keys\" permission can manage the metadata for all users. A user with the
    \"Browse App API Keys\" permission can view the metadata for all users.

    Args:
        body (AppAPIKeyCreate | Unset): AppAPIKeyCreate defines an App API Key creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAppAPIKeyResponse201 | PostAppAPIKeyResponse400 | PostAppAPIKeyResponse401 | PostAppAPIKeyResponse403 | PostAppAPIKeyResponse422 | PostAppAPIKeyResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
