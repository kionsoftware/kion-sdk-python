from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_scope_priority_effective_month_response_200 import GetScopePriorityEffectiveMonthResponse200
from ...models.get_scope_priority_effective_month_response_401 import GetScopePriorityEffectiveMonthResponse401
from ...models.get_scope_priority_effective_month_response_500 import GetScopePriorityEffectiveMonthResponse500
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/beta/scope/priority/effective-month",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetScopePriorityEffectiveMonthResponse200 | GetScopePriorityEffectiveMonthResponse401 | GetScopePriorityEffectiveMonthResponse500 | None:
    if response.status_code == 200:
        response_200 = GetScopePriorityEffectiveMonthResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetScopePriorityEffectiveMonthResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 500:
        response_500 = GetScopePriorityEffectiveMonthResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetScopePriorityEffectiveMonthResponse200 | GetScopePriorityEffectiveMonthResponse401 | GetScopePriorityEffectiveMonthResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetScopePriorityEffectiveMonthResponse200 | GetScopePriorityEffectiveMonthResponse401 | GetScopePriorityEffectiveMonthResponse500]:
    """ Returns the most recent month (YYYYMM) a scope prioritization took effect, or 0 if none.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetScopePriorityEffectiveMonthResponse200 | GetScopePriorityEffectiveMonthResponse401 | GetScopePriorityEffectiveMonthResponse500]
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

) -> GetScopePriorityEffectiveMonthResponse200 | GetScopePriorityEffectiveMonthResponse401 | GetScopePriorityEffectiveMonthResponse500 | None:
    """ Returns the most recent month (YYYYMM) a scope prioritization took effect, or 0 if none.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetScopePriorityEffectiveMonthResponse200 | GetScopePriorityEffectiveMonthResponse401 | GetScopePriorityEffectiveMonthResponse500
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetScopePriorityEffectiveMonthResponse200 | GetScopePriorityEffectiveMonthResponse401 | GetScopePriorityEffectiveMonthResponse500]:
    """ Returns the most recent month (YYYYMM) a scope prioritization took effect, or 0 if none.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetScopePriorityEffectiveMonthResponse200 | GetScopePriorityEffectiveMonthResponse401 | GetScopePriorityEffectiveMonthResponse500]
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

) -> GetScopePriorityEffectiveMonthResponse200 | GetScopePriorityEffectiveMonthResponse401 | GetScopePriorityEffectiveMonthResponse500 | None:
    """ Returns the most recent month (YYYYMM) a scope prioritization took effect, or 0 if none.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetScopePriorityEffectiveMonthResponse200 | GetScopePriorityEffectiveMonthResponse401 | GetScopePriorityEffectiveMonthResponse500
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
