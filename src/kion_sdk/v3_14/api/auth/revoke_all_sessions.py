from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.revoke_all_sessions_response_200 import RevokeAllSessionsResponse200
from ...models.revoke_all_sessions_response_400 import RevokeAllSessionsResponse400
from ...models.revoke_all_sessions_response_403 import RevokeAllSessionsResponse403
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/session/revoke-all",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RevokeAllSessionsResponse200 | RevokeAllSessionsResponse400 | RevokeAllSessionsResponse403 | None:
    if response.status_code == 200:
        response_200 = RevokeAllSessionsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = RevokeAllSessionsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 403:
        response_403 = RevokeAllSessionsResponse403.from_dict(response.json())



        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RevokeAllSessionsResponse200 | RevokeAllSessionsResponse400 | RevokeAllSessionsResponse403]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[RevokeAllSessionsResponse200 | RevokeAllSessionsResponse400 | RevokeAllSessionsResponse403]:
    """ Revokes all existing web sessions. This will log every user out of the system and invalidate all
    existing authentication tokens.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RevokeAllSessionsResponse200 | RevokeAllSessionsResponse400 | RevokeAllSessionsResponse403]
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

) -> RevokeAllSessionsResponse200 | RevokeAllSessionsResponse400 | RevokeAllSessionsResponse403 | None:
    """ Revokes all existing web sessions. This will log every user out of the system and invalidate all
    existing authentication tokens.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RevokeAllSessionsResponse200 | RevokeAllSessionsResponse400 | RevokeAllSessionsResponse403
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[RevokeAllSessionsResponse200 | RevokeAllSessionsResponse400 | RevokeAllSessionsResponse403]:
    """ Revokes all existing web sessions. This will log every user out of the system and invalidate all
    existing authentication tokens.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RevokeAllSessionsResponse200 | RevokeAllSessionsResponse400 | RevokeAllSessionsResponse403]
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

) -> RevokeAllSessionsResponse200 | RevokeAllSessionsResponse400 | RevokeAllSessionsResponse403 | None:
    """ Revokes all existing web sessions. This will log every user out of the system and invalidate all
    existing authentication tokens.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RevokeAllSessionsResponse200 | RevokeAllSessionsResponse400 | RevokeAllSessionsResponse403
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
