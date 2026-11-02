from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.duplicate_dashboard_response_201 import DuplicateDashboardResponse201
from ...models.duplicate_dashboard_response_400 import DuplicateDashboardResponse400
from ...models.duplicate_dashboard_response_401 import DuplicateDashboardResponse401
from ...models.duplicate_dashboard_response_500 import DuplicateDashboardResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/beta/dashboard/{id}/duplicate".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DuplicateDashboardResponse201 | DuplicateDashboardResponse400 | DuplicateDashboardResponse401 | DuplicateDashboardResponse500 | None:
    if response.status_code == 201:
        response_201 = DuplicateDashboardResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = DuplicateDashboardResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DuplicateDashboardResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 500:
        response_500 = DuplicateDashboardResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DuplicateDashboardResponse201 | DuplicateDashboardResponse400 | DuplicateDashboardResponse401 | DuplicateDashboardResponse500]:
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

) -> Response[DuplicateDashboardResponse201 | DuplicateDashboardResponse400 | DuplicateDashboardResponse401 | DuplicateDashboardResponse500]:
    """ Creates a copy of an existing dashboard in the system.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DuplicateDashboardResponse201 | DuplicateDashboardResponse400 | DuplicateDashboardResponse401 | DuplicateDashboardResponse500]
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

) -> DuplicateDashboardResponse201 | DuplicateDashboardResponse400 | DuplicateDashboardResponse401 | DuplicateDashboardResponse500 | None:
    """ Creates a copy of an existing dashboard in the system.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DuplicateDashboardResponse201 | DuplicateDashboardResponse400 | DuplicateDashboardResponse401 | DuplicateDashboardResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[DuplicateDashboardResponse201 | DuplicateDashboardResponse400 | DuplicateDashboardResponse401 | DuplicateDashboardResponse500]:
    """ Creates a copy of an existing dashboard in the system.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DuplicateDashboardResponse201 | DuplicateDashboardResponse400 | DuplicateDashboardResponse401 | DuplicateDashboardResponse500]
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

) -> DuplicateDashboardResponse201 | DuplicateDashboardResponse400 | DuplicateDashboardResponse401 | DuplicateDashboardResponse500 | None:
    """ Creates a copy of an existing dashboard in the system.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DuplicateDashboardResponse201 | DuplicateDashboardResponse400 | DuplicateDashboardResponse401 | DuplicateDashboardResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
