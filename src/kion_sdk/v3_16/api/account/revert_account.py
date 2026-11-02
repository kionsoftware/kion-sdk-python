from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.revert_account_response_200 import RevertAccountResponse200
from ...models.revert_account_response_401 import RevertAccountResponse401
from ...models.revert_account_response_403 import RevertAccountResponse403
from ...models.revert_account_response_404 import RevertAccountResponse404
from ...models.revert_account_response_500 import RevertAccountResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/account/revert/{id}".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RevertAccountResponse200 | RevertAccountResponse401 | RevertAccountResponse403 | RevertAccountResponse404 | RevertAccountResponse500 | None:
    if response.status_code == 200:
        response_200 = RevertAccountResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = RevertAccountResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = RevertAccountResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = RevertAccountResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = RevertAccountResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RevertAccountResponse200 | RevertAccountResponse401 | RevertAccountResponse403 | RevertAccountResponse404 | RevertAccountResponse500]:
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

) -> Response[RevertAccountResponse200 | RevertAccountResponse401 | RevertAccountResponse403 | RevertAccountResponse404 | RevertAccountResponse500]:
    """ Reverts the account with passed in ID by moving the account into the account cache.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RevertAccountResponse200 | RevertAccountResponse401 | RevertAccountResponse403 | RevertAccountResponse404 | RevertAccountResponse500]
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

) -> RevertAccountResponse200 | RevertAccountResponse401 | RevertAccountResponse403 | RevertAccountResponse404 | RevertAccountResponse500 | None:
    """ Reverts the account with passed in ID by moving the account into the account cache.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RevertAccountResponse200 | RevertAccountResponse401 | RevertAccountResponse403 | RevertAccountResponse404 | RevertAccountResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[RevertAccountResponse200 | RevertAccountResponse401 | RevertAccountResponse403 | RevertAccountResponse404 | RevertAccountResponse500]:
    """ Reverts the account with passed in ID by moving the account into the account cache.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RevertAccountResponse200 | RevertAccountResponse401 | RevertAccountResponse403 | RevertAccountResponse404 | RevertAccountResponse500]
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

) -> RevertAccountResponse200 | RevertAccountResponse401 | RevertAccountResponse403 | RevertAccountResponse404 | RevertAccountResponse500 | None:
    """ Reverts the account with passed in ID by moving the account into the account cache.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RevertAccountResponse200 | RevertAccountResponse401 | RevertAccountResponse403 | RevertAccountResponse404 | RevertAccountResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
