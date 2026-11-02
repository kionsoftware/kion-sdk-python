from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_app_api_key_response_200 import GetAppAPIKeyResponse200
from ...models.get_app_api_key_response_401 import GetAppAPIKeyResponse401
from ...models.get_app_api_key_response_403 import GetAppAPIKeyResponse403
from ...models.get_app_api_key_response_404 import GetAppAPIKeyResponse404
from ...models.get_app_api_key_response_500 import GetAppAPIKeyResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/app-api-key/{id}".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetAppAPIKeyResponse200 | GetAppAPIKeyResponse401 | GetAppAPIKeyResponse403 | GetAppAPIKeyResponse404 | GetAppAPIKeyResponse500 | None:
    if response.status_code == 200:
        response_200 = GetAppAPIKeyResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetAppAPIKeyResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetAppAPIKeyResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetAppAPIKeyResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetAppAPIKeyResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetAppAPIKeyResponse200 | GetAppAPIKeyResponse401 | GetAppAPIKeyResponse403 | GetAppAPIKeyResponse404 | GetAppAPIKeyResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetAppAPIKeyResponse200 | GetAppAPIKeyResponse401 | GetAppAPIKeyResponse403 | GetAppAPIKeyResponse404 | GetAppAPIKeyResponse500]:
    r""" Finds an App API Key metadata by ID in the application.

     Metadata does not contain the App API Key secret. A user with the \"Manage App
    API Keys\" permission can manage the metadata for all users. A user with the
    \"Browse App API Keys\" permission can view the metadata for all users.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAppAPIKeyResponse200 | GetAppAPIKeyResponse401 | GetAppAPIKeyResponse403 | GetAppAPIKeyResponse404 | GetAppAPIKeyResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,

) -> GetAppAPIKeyResponse200 | GetAppAPIKeyResponse401 | GetAppAPIKeyResponse403 | GetAppAPIKeyResponse404 | GetAppAPIKeyResponse500 | None:
    r""" Finds an App API Key metadata by ID in the application.

     Metadata does not contain the App API Key secret. A user with the \"Manage App
    API Keys\" permission can manage the metadata for all users. A user with the
    \"Browse App API Keys\" permission can view the metadata for all users.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAppAPIKeyResponse200 | GetAppAPIKeyResponse401 | GetAppAPIKeyResponse403 | GetAppAPIKeyResponse404 | GetAppAPIKeyResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetAppAPIKeyResponse200 | GetAppAPIKeyResponse401 | GetAppAPIKeyResponse403 | GetAppAPIKeyResponse404 | GetAppAPIKeyResponse500]:
    r""" Finds an App API Key metadata by ID in the application.

     Metadata does not contain the App API Key secret. A user with the \"Manage App
    API Keys\" permission can manage the metadata for all users. A user with the
    \"Browse App API Keys\" permission can view the metadata for all users.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAppAPIKeyResponse200 | GetAppAPIKeyResponse401 | GetAppAPIKeyResponse403 | GetAppAPIKeyResponse404 | GetAppAPIKeyResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,

) -> GetAppAPIKeyResponse200 | GetAppAPIKeyResponse401 | GetAppAPIKeyResponse403 | GetAppAPIKeyResponse404 | GetAppAPIKeyResponse500 | None:
    r""" Finds an App API Key metadata by ID in the application.

     Metadata does not contain the App API Key secret. A user with the \"Manage App
    API Keys\" permission can manage the metadata for all users. A user with the
    \"Browse App API Keys\" permission can view the metadata for all users.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAppAPIKeyResponse200 | GetAppAPIKeyResponse401 | GetAppAPIKeyResponse403 | GetAppAPIKeyResponse404 | GetAppAPIKeyResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
