from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.patch_u_group_response_200 import PatchUGroupResponse200
from ...models.patch_u_group_response_400 import PatchUGroupResponse400
from ...models.patch_u_group_response_401 import PatchUGroupResponse401
from ...models.patch_u_group_response_403 import PatchUGroupResponse403
from ...models.patch_u_group_response_404 import PatchUGroupResponse404
from ...models.patch_u_group_response_422 import PatchUGroupResponse422
from ...models.patch_u_group_response_500 import PatchUGroupResponse500
from ...models.u_group_updatable import UGroupUpdatable
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: UGroupUpdatable | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/user-group/{id}".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchUGroupResponse200 | PatchUGroupResponse400 | PatchUGroupResponse401 | PatchUGroupResponse403 | PatchUGroupResponse404 | PatchUGroupResponse422 | PatchUGroupResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchUGroupResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchUGroupResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchUGroupResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchUGroupResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PatchUGroupResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PatchUGroupResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchUGroupResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchUGroupResponse200 | PatchUGroupResponse400 | PatchUGroupResponse401 | PatchUGroupResponse403 | PatchUGroupResponse404 | PatchUGroupResponse422 | PatchUGroupResponse500]:
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
    body: UGroupUpdatable | Unset = UNSET,

) -> Response[PatchUGroupResponse200 | PatchUGroupResponse400 | PatchUGroupResponse401 | PatchUGroupResponse403 | PatchUGroupResponse404 | PatchUGroupResponse422 | PatchUGroupResponse500]:
    """ Updates a user group by ID in the application.

    Args:
        id (int):
        body (UGroupUpdatable | Unset): UGroupUpdatable defines a user group update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchUGroupResponse200 | PatchUGroupResponse400 | PatchUGroupResponse401 | PatchUGroupResponse403 | PatchUGroupResponse404 | PatchUGroupResponse422 | PatchUGroupResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: UGroupUpdatable | Unset = UNSET,

) -> PatchUGroupResponse200 | PatchUGroupResponse400 | PatchUGroupResponse401 | PatchUGroupResponse403 | PatchUGroupResponse404 | PatchUGroupResponse422 | PatchUGroupResponse500 | None:
    """ Updates a user group by ID in the application.

    Args:
        id (int):
        body (UGroupUpdatable | Unset): UGroupUpdatable defines a user group update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchUGroupResponse200 | PatchUGroupResponse400 | PatchUGroupResponse401 | PatchUGroupResponse403 | PatchUGroupResponse404 | PatchUGroupResponse422 | PatchUGroupResponse500
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: UGroupUpdatable | Unset = UNSET,

) -> Response[PatchUGroupResponse200 | PatchUGroupResponse400 | PatchUGroupResponse401 | PatchUGroupResponse403 | PatchUGroupResponse404 | PatchUGroupResponse422 | PatchUGroupResponse500]:
    """ Updates a user group by ID in the application.

    Args:
        id (int):
        body (UGroupUpdatable | Unset): UGroupUpdatable defines a user group update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchUGroupResponse200 | PatchUGroupResponse400 | PatchUGroupResponse401 | PatchUGroupResponse403 | PatchUGroupResponse404 | PatchUGroupResponse422 | PatchUGroupResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: UGroupUpdatable | Unset = UNSET,

) -> PatchUGroupResponse200 | PatchUGroupResponse400 | PatchUGroupResponse401 | PatchUGroupResponse403 | PatchUGroupResponse404 | PatchUGroupResponse422 | PatchUGroupResponse500 | None:
    """ Updates a user group by ID in the application.

    Args:
        id (int):
        body (UGroupUpdatable | Unset): UGroupUpdatable defines a user group update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchUGroupResponse200 | PatchUGroupResponse400 | PatchUGroupResponse401 | PatchUGroupResponse403 | PatchUGroupResponse404 | PatchUGroupResponse422 | PatchUGroupResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
