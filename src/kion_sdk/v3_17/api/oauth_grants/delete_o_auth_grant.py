from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_o_auth_grant_response_200 import DeleteOAuthGrantResponse200
from ...models.delete_o_auth_grant_response_400 import DeleteOAuthGrantResponse400
from ...models.delete_o_auth_grant_response_401 import DeleteOAuthGrantResponse401
from ...models.delete_o_auth_grant_response_500 import DeleteOAuthGrantResponse500
from typing import cast



def _get_kwargs(
    client_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/oauth2/grants/{client_id}".format(client_id=quote(str(client_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteOAuthGrantResponse200 | DeleteOAuthGrantResponse400 | DeleteOAuthGrantResponse401 | DeleteOAuthGrantResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteOAuthGrantResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DeleteOAuthGrantResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteOAuthGrantResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 500:
        response_500 = DeleteOAuthGrantResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteOAuthGrantResponse200 | DeleteOAuthGrantResponse400 | DeleteOAuthGrantResponse401 | DeleteOAuthGrantResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    client_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteOAuthGrantResponse200 | DeleteOAuthGrantResponse400 | DeleteOAuthGrantResponse401 | DeleteOAuthGrantResponse500]:
    """ Revokes all tokens for a specific OAuth client grant.

     Any authenticated user can revoke their own grants. This removes all access
    and refresh tokens for the specified client-user pair.

    Args:
        client_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteOAuthGrantResponse200 | DeleteOAuthGrantResponse400 | DeleteOAuthGrantResponse401 | DeleteOAuthGrantResponse500]
     """


    kwargs = _get_kwargs(
        client_id=client_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    client_id: str,
    *,
    client: AuthenticatedClient,

) -> DeleteOAuthGrantResponse200 | DeleteOAuthGrantResponse400 | DeleteOAuthGrantResponse401 | DeleteOAuthGrantResponse500 | None:
    """ Revokes all tokens for a specific OAuth client grant.

     Any authenticated user can revoke their own grants. This removes all access
    and refresh tokens for the specified client-user pair.

    Args:
        client_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteOAuthGrantResponse200 | DeleteOAuthGrantResponse400 | DeleteOAuthGrantResponse401 | DeleteOAuthGrantResponse500
     """


    return sync_detailed(
        client_id=client_id,
client=client,

    ).parsed

async def asyncio_detailed(
    client_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteOAuthGrantResponse200 | DeleteOAuthGrantResponse400 | DeleteOAuthGrantResponse401 | DeleteOAuthGrantResponse500]:
    """ Revokes all tokens for a specific OAuth client grant.

     Any authenticated user can revoke their own grants. This removes all access
    and refresh tokens for the specified client-user pair.

    Args:
        client_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteOAuthGrantResponse200 | DeleteOAuthGrantResponse400 | DeleteOAuthGrantResponse401 | DeleteOAuthGrantResponse500]
     """


    kwargs = _get_kwargs(
        client_id=client_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    client_id: str,
    *,
    client: AuthenticatedClient,

) -> DeleteOAuthGrantResponse200 | DeleteOAuthGrantResponse400 | DeleteOAuthGrantResponse401 | DeleteOAuthGrantResponse500 | None:
    """ Revokes all tokens for a specific OAuth client grant.

     Any authenticated user can revoke their own grants. This removes all access
    and refresh tokens for the specified client-user pair.

    Args:
        client_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteOAuthGrantResponse200 | DeleteOAuthGrantResponse400 | DeleteOAuthGrantResponse401 | DeleteOAuthGrantResponse500
     """


    return (await asyncio_detailed(
        client_id=client_id,
client=client,

    )).parsed
