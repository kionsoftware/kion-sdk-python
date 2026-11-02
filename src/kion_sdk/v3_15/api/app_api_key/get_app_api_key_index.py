from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_app_api_key_index_response_200 import GetAppAPIKeyIndexResponse200
from ...models.get_app_api_key_index_response_401 import GetAppAPIKeyIndexResponse401
from ...models.get_app_api_key_index_response_403 import GetAppAPIKeyIndexResponse403
from ...models.get_app_api_key_index_response_500 import GetAppAPIKeyIndexResponse500
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/app-api-key",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetAppAPIKeyIndexResponse200 | GetAppAPIKeyIndexResponse401 | GetAppAPIKeyIndexResponse403 | GetAppAPIKeyIndexResponse500 | None:
    if response.status_code == 200:
        response_200 = GetAppAPIKeyIndexResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetAppAPIKeyIndexResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetAppAPIKeyIndexResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetAppAPIKeyIndexResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetAppAPIKeyIndexResponse200 | GetAppAPIKeyIndexResponse401 | GetAppAPIKeyIndexResponse403 | GetAppAPIKeyIndexResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetAppAPIKeyIndexResponse200 | GetAppAPIKeyIndexResponse401 | GetAppAPIKeyIndexResponse403 | GetAppAPIKeyIndexResponse500]:
    r""" Returns a list of App API Key metadata from the application.

     Metadata does not contain the App API Key secret. A user with the \"Manage App
    API Keys\" permission can manage the metadata for all users. A user with the
    \"Browse App API Keys\" permission can view the metadata for all users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAppAPIKeyIndexResponse200 | GetAppAPIKeyIndexResponse401 | GetAppAPIKeyIndexResponse403 | GetAppAPIKeyIndexResponse500]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,

) -> GetAppAPIKeyIndexResponse200 | GetAppAPIKeyIndexResponse401 | GetAppAPIKeyIndexResponse403 | GetAppAPIKeyIndexResponse500 | None:
    r""" Returns a list of App API Key metadata from the application.

     Metadata does not contain the App API Key secret. A user with the \"Manage App
    API Keys\" permission can manage the metadata for all users. A user with the
    \"Browse App API Keys\" permission can view the metadata for all users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAppAPIKeyIndexResponse200 | GetAppAPIKeyIndexResponse401 | GetAppAPIKeyIndexResponse403 | GetAppAPIKeyIndexResponse500
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetAppAPIKeyIndexResponse200 | GetAppAPIKeyIndexResponse401 | GetAppAPIKeyIndexResponse403 | GetAppAPIKeyIndexResponse500]:
    r""" Returns a list of App API Key metadata from the application.

     Metadata does not contain the App API Key secret. A user with the \"Manage App
    API Keys\" permission can manage the metadata for all users. A user with the
    \"Browse App API Keys\" permission can view the metadata for all users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAppAPIKeyIndexResponse200 | GetAppAPIKeyIndexResponse401 | GetAppAPIKeyIndexResponse403 | GetAppAPIKeyIndexResponse500]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,

) -> GetAppAPIKeyIndexResponse200 | GetAppAPIKeyIndexResponse401 | GetAppAPIKeyIndexResponse403 | GetAppAPIKeyIndexResponse500 | None:
    r""" Returns a list of App API Key metadata from the application.

     Metadata does not contain the App API Key secret. A user with the \"Manage App
    API Keys\" permission can manage the metadata for all users. A user with the
    \"Browse App API Keys\" permission can view the metadata for all users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAppAPIKeyIndexResponse200 | GetAppAPIKeyIndexResponse401 | GetAppAPIKeyIndexResponse403 | GetAppAPIKeyIndexResponse500
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
