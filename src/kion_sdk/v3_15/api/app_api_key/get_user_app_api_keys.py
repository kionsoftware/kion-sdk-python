from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_user_app_api_keys_response_200 import GetUserAppAPIKeysResponse200
from ...models.get_user_app_api_keys_response_401 import GetUserAppAPIKeysResponse401
from ...models.get_user_app_api_keys_response_403 import GetUserAppAPIKeysResponse403
from ...models.get_user_app_api_keys_response_404 import GetUserAppAPIKeysResponse404
from ...models.get_user_app_api_keys_response_500 import GetUserAppAPIKeysResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/app-api-key/user/{id}".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetUserAppAPIKeysResponse200 | GetUserAppAPIKeysResponse401 | GetUserAppAPIKeysResponse403 | GetUserAppAPIKeysResponse404 | GetUserAppAPIKeysResponse500 | None:
    if response.status_code == 200:
        response_200 = GetUserAppAPIKeysResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetUserAppAPIKeysResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetUserAppAPIKeysResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetUserAppAPIKeysResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetUserAppAPIKeysResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetUserAppAPIKeysResponse200 | GetUserAppAPIKeysResponse401 | GetUserAppAPIKeysResponse403 | GetUserAppAPIKeysResponse404 | GetUserAppAPIKeysResponse500]:
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

) -> Response[GetUserAppAPIKeysResponse200 | GetUserAppAPIKeysResponse401 | GetUserAppAPIKeysResponse403 | GetUserAppAPIKeysResponse404 | GetUserAppAPIKeysResponse500]:
    r""" Finds a list of a user's active (non-expired) App API Key metadata in the application.

     Metadata does not contain the App API Key secret. A user with the \"Manage App
    API Keys\" permission can manage the metadata for all users. A user with the
    \"Browse App API Keys\" permission can view the metadata for all users.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUserAppAPIKeysResponse200 | GetUserAppAPIKeysResponse401 | GetUserAppAPIKeysResponse403 | GetUserAppAPIKeysResponse404 | GetUserAppAPIKeysResponse500]
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

) -> GetUserAppAPIKeysResponse200 | GetUserAppAPIKeysResponse401 | GetUserAppAPIKeysResponse403 | GetUserAppAPIKeysResponse404 | GetUserAppAPIKeysResponse500 | None:
    r""" Finds a list of a user's active (non-expired) App API Key metadata in the application.

     Metadata does not contain the App API Key secret. A user with the \"Manage App
    API Keys\" permission can manage the metadata for all users. A user with the
    \"Browse App API Keys\" permission can view the metadata for all users.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUserAppAPIKeysResponse200 | GetUserAppAPIKeysResponse401 | GetUserAppAPIKeysResponse403 | GetUserAppAPIKeysResponse404 | GetUserAppAPIKeysResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetUserAppAPIKeysResponse200 | GetUserAppAPIKeysResponse401 | GetUserAppAPIKeysResponse403 | GetUserAppAPIKeysResponse404 | GetUserAppAPIKeysResponse500]:
    r""" Finds a list of a user's active (non-expired) App API Key metadata in the application.

     Metadata does not contain the App API Key secret. A user with the \"Manage App
    API Keys\" permission can manage the metadata for all users. A user with the
    \"Browse App API Keys\" permission can view the metadata for all users.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUserAppAPIKeysResponse200 | GetUserAppAPIKeysResponse401 | GetUserAppAPIKeysResponse403 | GetUserAppAPIKeysResponse404 | GetUserAppAPIKeysResponse500]
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

) -> GetUserAppAPIKeysResponse200 | GetUserAppAPIKeysResponse401 | GetUserAppAPIKeysResponse403 | GetUserAppAPIKeysResponse404 | GetUserAppAPIKeysResponse500 | None:
    r""" Finds a list of a user's active (non-expired) App API Key metadata in the application.

     Metadata does not contain the App API Key secret. A user with the \"Manage App
    API Keys\" permission can manage the metadata for all users. A user with the
    \"Browse App API Keys\" permission can view the metadata for all users.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUserAppAPIKeysResponse200 | GetUserAppAPIKeysResponse401 | GetUserAppAPIKeysResponse403 | GetUserAppAPIKeysResponse404 | GetUserAppAPIKeysResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
