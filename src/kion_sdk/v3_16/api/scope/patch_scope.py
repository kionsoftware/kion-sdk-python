from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.patch_scope_response_200 import PatchScopeResponse200
from ...models.patch_scope_response_400 import PatchScopeResponse400
from ...models.patch_scope_response_401 import PatchScopeResponse401
from ...models.patch_scope_response_403 import PatchScopeResponse403
from ...models.patch_scope_response_404 import PatchScopeResponse404
from ...models.patch_scope_response_422 import PatchScopeResponse422
from ...models.patch_scope_response_500 import PatchScopeResponse500
from ...models.scope_update import ScopeUpdate
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: ScopeUpdate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/beta/scope/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchScopeResponse200 | PatchScopeResponse400 | PatchScopeResponse401 | PatchScopeResponse403 | PatchScopeResponse404 | PatchScopeResponse422 | PatchScopeResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchScopeResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchScopeResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchScopeResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchScopeResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PatchScopeResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PatchScopeResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchScopeResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchScopeResponse200 | PatchScopeResponse400 | PatchScopeResponse401 | PatchScopeResponse403 | PatchScopeResponse404 | PatchScopeResponse422 | PatchScopeResponse500]:
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
    body: ScopeUpdate,

) -> Response[PatchScopeResponse200 | PatchScopeResponse400 | PatchScopeResponse401 | PatchScopeResponse403 | PatchScopeResponse404 | PatchScopeResponse422 | PatchScopeResponse500]:
    """ Updates an existing scope in the system.

    Args:
        id (int):
        body (ScopeUpdate): ScopeUpdate defines a Scope update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchScopeResponse200 | PatchScopeResponse400 | PatchScopeResponse401 | PatchScopeResponse403 | PatchScopeResponse404 | PatchScopeResponse422 | PatchScopeResponse500]
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
    body: ScopeUpdate,

) -> PatchScopeResponse200 | PatchScopeResponse400 | PatchScopeResponse401 | PatchScopeResponse403 | PatchScopeResponse404 | PatchScopeResponse422 | PatchScopeResponse500 | None:
    """ Updates an existing scope in the system.

    Args:
        id (int):
        body (ScopeUpdate): ScopeUpdate defines a Scope update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchScopeResponse200 | PatchScopeResponse400 | PatchScopeResponse401 | PatchScopeResponse403 | PatchScopeResponse404 | PatchScopeResponse422 | PatchScopeResponse500
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
    body: ScopeUpdate,

) -> Response[PatchScopeResponse200 | PatchScopeResponse400 | PatchScopeResponse401 | PatchScopeResponse403 | PatchScopeResponse404 | PatchScopeResponse422 | PatchScopeResponse500]:
    """ Updates an existing scope in the system.

    Args:
        id (int):
        body (ScopeUpdate): ScopeUpdate defines a Scope update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchScopeResponse200 | PatchScopeResponse400 | PatchScopeResponse401 | PatchScopeResponse403 | PatchScopeResponse404 | PatchScopeResponse422 | PatchScopeResponse500]
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
    body: ScopeUpdate,

) -> PatchScopeResponse200 | PatchScopeResponse400 | PatchScopeResponse401 | PatchScopeResponse403 | PatchScopeResponse404 | PatchScopeResponse422 | PatchScopeResponse500 | None:
    """ Updates an existing scope in the system.

    Args:
        id (int):
        body (ScopeUpdate): ScopeUpdate defines a Scope update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchScopeResponse200 | PatchScopeResponse400 | PatchScopeResponse401 | PatchScopeResponse403 | PatchScopeResponse404 | PatchScopeResponse422 | PatchScopeResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
