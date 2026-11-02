from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_cache_updatable import AccountCacheUpdatable
from ...models.patch_account_cache_response_200 import PatchAccountCacheResponse200
from ...models.patch_account_cache_response_400 import PatchAccountCacheResponse400
from ...models.patch_account_cache_response_401 import PatchAccountCacheResponse401
from ...models.patch_account_cache_response_403 import PatchAccountCacheResponse403
from ...models.patch_account_cache_response_404 import PatchAccountCacheResponse404
from ...models.patch_account_cache_response_422 import PatchAccountCacheResponse422
from ...models.patch_account_cache_response_500 import PatchAccountCacheResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: AccountCacheUpdatable,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/account-cache/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchAccountCacheResponse200 | PatchAccountCacheResponse400 | PatchAccountCacheResponse401 | PatchAccountCacheResponse403 | PatchAccountCacheResponse404 | PatchAccountCacheResponse422 | PatchAccountCacheResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchAccountCacheResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchAccountCacheResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchAccountCacheResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchAccountCacheResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PatchAccountCacheResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PatchAccountCacheResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchAccountCacheResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchAccountCacheResponse200 | PatchAccountCacheResponse400 | PatchAccountCacheResponse401 | PatchAccountCacheResponse403 | PatchAccountCacheResponse404 | PatchAccountCacheResponse422 | PatchAccountCacheResponse500]:
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
    body: AccountCacheUpdatable,

) -> Response[PatchAccountCacheResponse200 | PatchAccountCacheResponse400 | PatchAccountCacheResponse401 | PatchAccountCacheResponse403 | PatchAccountCacheResponse404 | PatchAccountCacheResponse422 | PatchAccountCacheResponse500]:
    """ Updates an existing cached account in the application.

    Args:
        id (int):
        body (AccountCacheUpdatable): AccountCacheUpdatable defines a cached account update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchAccountCacheResponse200 | PatchAccountCacheResponse400 | PatchAccountCacheResponse401 | PatchAccountCacheResponse403 | PatchAccountCacheResponse404 | PatchAccountCacheResponse422 | PatchAccountCacheResponse500]
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
    body: AccountCacheUpdatable,

) -> PatchAccountCacheResponse200 | PatchAccountCacheResponse400 | PatchAccountCacheResponse401 | PatchAccountCacheResponse403 | PatchAccountCacheResponse404 | PatchAccountCacheResponse422 | PatchAccountCacheResponse500 | None:
    """ Updates an existing cached account in the application.

    Args:
        id (int):
        body (AccountCacheUpdatable): AccountCacheUpdatable defines a cached account update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchAccountCacheResponse200 | PatchAccountCacheResponse400 | PatchAccountCacheResponse401 | PatchAccountCacheResponse403 | PatchAccountCacheResponse404 | PatchAccountCacheResponse422 | PatchAccountCacheResponse500
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
    body: AccountCacheUpdatable,

) -> Response[PatchAccountCacheResponse200 | PatchAccountCacheResponse400 | PatchAccountCacheResponse401 | PatchAccountCacheResponse403 | PatchAccountCacheResponse404 | PatchAccountCacheResponse422 | PatchAccountCacheResponse500]:
    """ Updates an existing cached account in the application.

    Args:
        id (int):
        body (AccountCacheUpdatable): AccountCacheUpdatable defines a cached account update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchAccountCacheResponse200 | PatchAccountCacheResponse400 | PatchAccountCacheResponse401 | PatchAccountCacheResponse403 | PatchAccountCacheResponse404 | PatchAccountCacheResponse422 | PatchAccountCacheResponse500]
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
    body: AccountCacheUpdatable,

) -> PatchAccountCacheResponse200 | PatchAccountCacheResponse400 | PatchAccountCacheResponse401 | PatchAccountCacheResponse403 | PatchAccountCacheResponse404 | PatchAccountCacheResponse422 | PatchAccountCacheResponse500 | None:
    """ Updates an existing cached account in the application.

    Args:
        id (int):
        body (AccountCacheUpdatable): AccountCacheUpdatable defines a cached account update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchAccountCacheResponse200 | PatchAccountCacheResponse400 | PatchAccountCacheResponse401 | PatchAccountCacheResponse403 | PatchAccountCacheResponse404 | PatchAccountCacheResponse422 | PatchAccountCacheResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
