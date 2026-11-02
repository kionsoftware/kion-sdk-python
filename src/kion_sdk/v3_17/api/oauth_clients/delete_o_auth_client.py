from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_o_auth_client_response_200 import DeleteOAuthClientResponse200
from ...models.delete_o_auth_client_response_401 import DeleteOAuthClientResponse401
from ...models.delete_o_auth_client_response_403 import DeleteOAuthClientResponse403
from ...models.delete_o_auth_client_response_404 import DeleteOAuthClientResponse404
from ...models.delete_o_auth_client_response_500 import DeleteOAuthClientResponse500
from typing import cast



def _get_kwargs(
    id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/oauth2/clients/{id}".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteOAuthClientResponse200 | DeleteOAuthClientResponse401 | DeleteOAuthClientResponse403 | DeleteOAuthClientResponse404 | DeleteOAuthClientResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteOAuthClientResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DeleteOAuthClientResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteOAuthClientResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteOAuthClientResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = DeleteOAuthClientResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteOAuthClientResponse200 | DeleteOAuthClientResponse401 | DeleteOAuthClientResponse403 | DeleteOAuthClientResponse404 | DeleteOAuthClientResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteOAuthClientResponse200 | DeleteOAuthClientResponse401 | DeleteOAuthClientResponse403 | DeleteOAuthClientResponse404 | DeleteOAuthClientResponse500]:
    r""" Deletes an OAuth client.

     A user with the \"Manage Applications\" permission can delete any client. A user
    with the \"Manage Own Applications\" permission can delete only their own clients.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteOAuthClientResponse200 | DeleteOAuthClientResponse401 | DeleteOAuthClientResponse403 | DeleteOAuthClientResponse404 | DeleteOAuthClientResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient,

) -> DeleteOAuthClientResponse200 | DeleteOAuthClientResponse401 | DeleteOAuthClientResponse403 | DeleteOAuthClientResponse404 | DeleteOAuthClientResponse500 | None:
    r""" Deletes an OAuth client.

     A user with the \"Manage Applications\" permission can delete any client. A user
    with the \"Manage Own Applications\" permission can delete only their own clients.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteOAuthClientResponse200 | DeleteOAuthClientResponse401 | DeleteOAuthClientResponse403 | DeleteOAuthClientResponse404 | DeleteOAuthClientResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteOAuthClientResponse200 | DeleteOAuthClientResponse401 | DeleteOAuthClientResponse403 | DeleteOAuthClientResponse404 | DeleteOAuthClientResponse500]:
    r""" Deletes an OAuth client.

     A user with the \"Manage Applications\" permission can delete any client. A user
    with the \"Manage Own Applications\" permission can delete only their own clients.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteOAuthClientResponse200 | DeleteOAuthClientResponse401 | DeleteOAuthClientResponse403 | DeleteOAuthClientResponse404 | DeleteOAuthClientResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,

) -> DeleteOAuthClientResponse200 | DeleteOAuthClientResponse401 | DeleteOAuthClientResponse403 | DeleteOAuthClientResponse404 | DeleteOAuthClientResponse500 | None:
    r""" Deletes an OAuth client.

     A user with the \"Manage Applications\" permission can delete any client. A user
    with the \"Manage Own Applications\" permission can delete only their own clients.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteOAuthClientResponse200 | DeleteOAuthClientResponse401 | DeleteOAuthClientResponse403 | DeleteOAuthClientResponse404 | DeleteOAuthClientResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
