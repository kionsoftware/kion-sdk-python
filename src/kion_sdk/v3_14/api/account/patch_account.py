from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_updatable import AccountUpdatable
from ...models.patch_account_response_200 import PatchAccountResponse200
from ...models.patch_account_response_400 import PatchAccountResponse400
from ...models.patch_account_response_401 import PatchAccountResponse401
from ...models.patch_account_response_403 import PatchAccountResponse403
from ...models.patch_account_response_404 import PatchAccountResponse404
from ...models.patch_account_response_422 import PatchAccountResponse422
from ...models.patch_account_response_500 import PatchAccountResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: AccountUpdatable,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/account/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchAccountResponse200 | PatchAccountResponse400 | PatchAccountResponse401 | PatchAccountResponse403 | PatchAccountResponse404 | PatchAccountResponse422 | PatchAccountResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchAccountResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchAccountResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchAccountResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchAccountResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PatchAccountResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PatchAccountResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchAccountResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchAccountResponse200 | PatchAccountResponse400 | PatchAccountResponse401 | PatchAccountResponse403 | PatchAccountResponse404 | PatchAccountResponse422 | PatchAccountResponse500]:
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
    body: AccountUpdatable,

) -> Response[PatchAccountResponse200 | PatchAccountResponse400 | PatchAccountResponse401 | PatchAccountResponse403 | PatchAccountResponse404 | PatchAccountResponse422 | PatchAccountResponse500]:
    """ Updates an existing account in the application.

    Args:
        id (int):
        body (AccountUpdatable): AccountUpdatable defines an account update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchAccountResponse200 | PatchAccountResponse400 | PatchAccountResponse401 | PatchAccountResponse403 | PatchAccountResponse404 | PatchAccountResponse422 | PatchAccountResponse500]
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
    body: AccountUpdatable,

) -> PatchAccountResponse200 | PatchAccountResponse400 | PatchAccountResponse401 | PatchAccountResponse403 | PatchAccountResponse404 | PatchAccountResponse422 | PatchAccountResponse500 | None:
    """ Updates an existing account in the application.

    Args:
        id (int):
        body (AccountUpdatable): AccountUpdatable defines an account update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchAccountResponse200 | PatchAccountResponse400 | PatchAccountResponse401 | PatchAccountResponse403 | PatchAccountResponse404 | PatchAccountResponse422 | PatchAccountResponse500
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
    body: AccountUpdatable,

) -> Response[PatchAccountResponse200 | PatchAccountResponse400 | PatchAccountResponse401 | PatchAccountResponse403 | PatchAccountResponse404 | PatchAccountResponse422 | PatchAccountResponse500]:
    """ Updates an existing account in the application.

    Args:
        id (int):
        body (AccountUpdatable): AccountUpdatable defines an account update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchAccountResponse200 | PatchAccountResponse400 | PatchAccountResponse401 | PatchAccountResponse403 | PatchAccountResponse404 | PatchAccountResponse422 | PatchAccountResponse500]
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
    body: AccountUpdatable,

) -> PatchAccountResponse200 | PatchAccountResponse400 | PatchAccountResponse401 | PatchAccountResponse403 | PatchAccountResponse404 | PatchAccountResponse422 | PatchAccountResponse500 | None:
    """ Updates an existing account in the application.

    Args:
        id (int):
        body (AccountUpdatable): AccountUpdatable defines an account update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchAccountResponse200 | PatchAccountResponse400 | PatchAccountResponse401 | PatchAccountResponse403 | PatchAccountResponse404 | PatchAccountResponse422 | PatchAccountResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
