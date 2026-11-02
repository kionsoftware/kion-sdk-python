from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_dashboard_response_201 import PostDashboardResponse201
from ...models.post_dashboard_response_401 import PostDashboardResponse401
from ...models.post_dashboard_response_422 import PostDashboardResponse422
from ...models.post_dashboard_response_500 import PostDashboardResponse500
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/beta/dashboard",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostDashboardResponse201 | PostDashboardResponse401 | PostDashboardResponse422 | PostDashboardResponse500 | None:
    if response.status_code == 201:
        response_201 = PostDashboardResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 401:
        response_401 = PostDashboardResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 422:
        response_422 = PostDashboardResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostDashboardResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostDashboardResponse201 | PostDashboardResponse401 | PostDashboardResponse422 | PostDashboardResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[PostDashboardResponse201 | PostDashboardResponse401 | PostDashboardResponse422 | PostDashboardResponse500]:
    """ Creates a new dashboard in the system.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostDashboardResponse201 | PostDashboardResponse401 | PostDashboardResponse422 | PostDashboardResponse500]
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

) -> PostDashboardResponse201 | PostDashboardResponse401 | PostDashboardResponse422 | PostDashboardResponse500 | None:
    """ Creates a new dashboard in the system.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostDashboardResponse201 | PostDashboardResponse401 | PostDashboardResponse422 | PostDashboardResponse500
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[PostDashboardResponse201 | PostDashboardResponse401 | PostDashboardResponse422 | PostDashboardResponse500]:
    """ Creates a new dashboard in the system.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostDashboardResponse201 | PostDashboardResponse401 | PostDashboardResponse422 | PostDashboardResponse500]
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

) -> PostDashboardResponse201 | PostDashboardResponse401 | PostDashboardResponse422 | PostDashboardResponse500 | None:
    """ Creates a new dashboard in the system.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostDashboardResponse201 | PostDashboardResponse401 | PostDashboardResponse422 | PostDashboardResponse500
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
