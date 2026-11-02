from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.patch_dashboard_response_200 import PatchDashboardResponse200
from ...models.patch_dashboard_response_400 import PatchDashboardResponse400
from ...models.patch_dashboard_response_401 import PatchDashboardResponse401
from ...models.patch_dashboard_response_403 import PatchDashboardResponse403
from ...models.patch_dashboard_response_422 import PatchDashboardResponse422
from ...models.patch_dashboard_response_500 import PatchDashboardResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/beta/dashboard/{id}".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchDashboardResponse200 | PatchDashboardResponse400 | PatchDashboardResponse401 | PatchDashboardResponse403 | PatchDashboardResponse422 | PatchDashboardResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchDashboardResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchDashboardResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchDashboardResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchDashboardResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PatchDashboardResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchDashboardResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchDashboardResponse200 | PatchDashboardResponse400 | PatchDashboardResponse401 | PatchDashboardResponse403 | PatchDashboardResponse422 | PatchDashboardResponse500]:
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

) -> Response[PatchDashboardResponse200 | PatchDashboardResponse400 | PatchDashboardResponse401 | PatchDashboardResponse403 | PatchDashboardResponse422 | PatchDashboardResponse500]:
    """ Updates an existing dashboard in the system.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchDashboardResponse200 | PatchDashboardResponse400 | PatchDashboardResponse401 | PatchDashboardResponse403 | PatchDashboardResponse422 | PatchDashboardResponse500]
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

) -> PatchDashboardResponse200 | PatchDashboardResponse400 | PatchDashboardResponse401 | PatchDashboardResponse403 | PatchDashboardResponse422 | PatchDashboardResponse500 | None:
    """ Updates an existing dashboard in the system.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchDashboardResponse200 | PatchDashboardResponse400 | PatchDashboardResponse401 | PatchDashboardResponse403 | PatchDashboardResponse422 | PatchDashboardResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[PatchDashboardResponse200 | PatchDashboardResponse400 | PatchDashboardResponse401 | PatchDashboardResponse403 | PatchDashboardResponse422 | PatchDashboardResponse500]:
    """ Updates an existing dashboard in the system.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchDashboardResponse200 | PatchDashboardResponse400 | PatchDashboardResponse401 | PatchDashboardResponse403 | PatchDashboardResponse422 | PatchDashboardResponse500]
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

) -> PatchDashboardResponse200 | PatchDashboardResponse400 | PatchDashboardResponse401 | PatchDashboardResponse403 | PatchDashboardResponse422 | PatchDashboardResponse500 | None:
    """ Updates an existing dashboard in the system.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchDashboardResponse200 | PatchDashboardResponse400 | PatchDashboardResponse401 | PatchDashboardResponse403 | PatchDashboardResponse422 | PatchDashboardResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
