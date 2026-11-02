from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_o_auth_grants_response_200 import GetOAuthGrantsResponse200
from ...models.get_o_auth_grants_response_401 import GetOAuthGrantsResponse401
from ...models.get_o_auth_grants_response_500 import GetOAuthGrantsResponse500
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/oauth2/grants",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetOAuthGrantsResponse200 | GetOAuthGrantsResponse401 | GetOAuthGrantsResponse500 | None:
    if response.status_code == 200:
        response_200 = GetOAuthGrantsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetOAuthGrantsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 500:
        response_500 = GetOAuthGrantsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetOAuthGrantsResponse200 | GetOAuthGrantsResponse401 | GetOAuthGrantsResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetOAuthGrantsResponse200 | GetOAuthGrantsResponse401 | GetOAuthGrantsResponse500]:
    """ Returns a list of OAuth grants for the authenticated user.

     Any authenticated user can view their own grants. A grant represents an
    authorized client that has been given access to act on behalf of the user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOAuthGrantsResponse200 | GetOAuthGrantsResponse401 | GetOAuthGrantsResponse500]
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

) -> GetOAuthGrantsResponse200 | GetOAuthGrantsResponse401 | GetOAuthGrantsResponse500 | None:
    """ Returns a list of OAuth grants for the authenticated user.

     Any authenticated user can view their own grants. A grant represents an
    authorized client that has been given access to act on behalf of the user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOAuthGrantsResponse200 | GetOAuthGrantsResponse401 | GetOAuthGrantsResponse500
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetOAuthGrantsResponse200 | GetOAuthGrantsResponse401 | GetOAuthGrantsResponse500]:
    """ Returns a list of OAuth grants for the authenticated user.

     Any authenticated user can view their own grants. A grant represents an
    authorized client that has been given access to act on behalf of the user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOAuthGrantsResponse200 | GetOAuthGrantsResponse401 | GetOAuthGrantsResponse500]
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

) -> GetOAuthGrantsResponse200 | GetOAuthGrantsResponse401 | GetOAuthGrantsResponse500 | None:
    """ Returns a list of OAuth grants for the authenticated user.

     Any authenticated user can view their own grants. A grant represents an
    authorized client that has been given access to act on behalf of the user.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOAuthGrantsResponse200 | GetOAuthGrantsResponse401 | GetOAuthGrantsResponse500
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
