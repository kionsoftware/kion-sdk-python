from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.scope_response_200 import ScopeResponse200
from ...models.scope_response_401 import ScopeResponse401
from ...models.scope_response_500 import ScopeResponse500
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/beta/scope/processing",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ScopeResponse200 | ScopeResponse401 | ScopeResponse500 | None:
    if response.status_code == 200:
        response_200 = ScopeResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = ScopeResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 500:
        response_500 = ScopeResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ScopeResponse200 | ScopeResponse401 | ScopeResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[ScopeResponse200 | ScopeResponse401 | ScopeResponse500]:
    """ Returns whether scope processing is in progress.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScopeResponse200 | ScopeResponse401 | ScopeResponse500]
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

) -> ScopeResponse200 | ScopeResponse401 | ScopeResponse500 | None:
    """ Returns whether scope processing is in progress.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScopeResponse200 | ScopeResponse401 | ScopeResponse500
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[ScopeResponse200 | ScopeResponse401 | ScopeResponse500]:
    """ Returns whether scope processing is in progress.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScopeResponse200 | ScopeResponse401 | ScopeResponse500]
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

) -> ScopeResponse200 | ScopeResponse401 | ScopeResponse500 | None:
    """ Returns whether scope processing is in progress.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScopeResponse200 | ScopeResponse401 | ScopeResponse500
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
