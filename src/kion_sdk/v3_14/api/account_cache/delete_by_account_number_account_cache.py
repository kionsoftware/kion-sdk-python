from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_by_account_number_account_cache_response_200 import DeleteByAccountNumberAccountCacheResponse200
from ...models.delete_by_account_number_account_cache_response_400 import DeleteByAccountNumberAccountCacheResponse400
from ...models.delete_by_account_number_account_cache_response_401 import DeleteByAccountNumberAccountCacheResponse401
from ...models.delete_by_account_number_account_cache_response_403 import DeleteByAccountNumberAccountCacheResponse403
from ...models.delete_by_account_number_account_cache_response_404 import DeleteByAccountNumberAccountCacheResponse404
from ...models.delete_by_account_number_account_cache_response_500 import DeleteByAccountNumberAccountCacheResponse500
from typing import cast



def _get_kwargs(
    account_number: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/account-cache/by-number/{account_number}".format(account_number=quote(str(account_number), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteByAccountNumberAccountCacheResponse200 | DeleteByAccountNumberAccountCacheResponse400 | DeleteByAccountNumberAccountCacheResponse401 | DeleteByAccountNumberAccountCacheResponse403 | DeleteByAccountNumberAccountCacheResponse404 | DeleteByAccountNumberAccountCacheResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteByAccountNumberAccountCacheResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DeleteByAccountNumberAccountCacheResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteByAccountNumberAccountCacheResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteByAccountNumberAccountCacheResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteByAccountNumberAccountCacheResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = DeleteByAccountNumberAccountCacheResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteByAccountNumberAccountCacheResponse200 | DeleteByAccountNumberAccountCacheResponse400 | DeleteByAccountNumberAccountCacheResponse401 | DeleteByAccountNumberAccountCacheResponse403 | DeleteByAccountNumberAccountCacheResponse404 | DeleteByAccountNumberAccountCacheResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_number: str,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteByAccountNumberAccountCacheResponse200 | DeleteByAccountNumberAccountCacheResponse400 | DeleteByAccountNumberAccountCacheResponse401 | DeleteByAccountNumberAccountCacheResponse403 | DeleteByAccountNumberAccountCacheResponse404 | DeleteByAccountNumberAccountCacheResponse500]:
    """ Deletes the cached account with passed in account number.

    Args:
        account_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteByAccountNumberAccountCacheResponse200 | DeleteByAccountNumberAccountCacheResponse400 | DeleteByAccountNumberAccountCacheResponse401 | DeleteByAccountNumberAccountCacheResponse403 | DeleteByAccountNumberAccountCacheResponse404 | DeleteByAccountNumberAccountCacheResponse500]
     """


    kwargs = _get_kwargs(
        account_number=account_number,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    account_number: str,
    *,
    client: AuthenticatedClient,

) -> DeleteByAccountNumberAccountCacheResponse200 | DeleteByAccountNumberAccountCacheResponse400 | DeleteByAccountNumberAccountCacheResponse401 | DeleteByAccountNumberAccountCacheResponse403 | DeleteByAccountNumberAccountCacheResponse404 | DeleteByAccountNumberAccountCacheResponse500 | None:
    """ Deletes the cached account with passed in account number.

    Args:
        account_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteByAccountNumberAccountCacheResponse200 | DeleteByAccountNumberAccountCacheResponse400 | DeleteByAccountNumberAccountCacheResponse401 | DeleteByAccountNumberAccountCacheResponse403 | DeleteByAccountNumberAccountCacheResponse404 | DeleteByAccountNumberAccountCacheResponse500
     """


    return sync_detailed(
        account_number=account_number,
client=client,

    ).parsed

async def asyncio_detailed(
    account_number: str,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteByAccountNumberAccountCacheResponse200 | DeleteByAccountNumberAccountCacheResponse400 | DeleteByAccountNumberAccountCacheResponse401 | DeleteByAccountNumberAccountCacheResponse403 | DeleteByAccountNumberAccountCacheResponse404 | DeleteByAccountNumberAccountCacheResponse500]:
    """ Deletes the cached account with passed in account number.

    Args:
        account_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteByAccountNumberAccountCacheResponse200 | DeleteByAccountNumberAccountCacheResponse400 | DeleteByAccountNumberAccountCacheResponse401 | DeleteByAccountNumberAccountCacheResponse403 | DeleteByAccountNumberAccountCacheResponse404 | DeleteByAccountNumberAccountCacheResponse500]
     """


    kwargs = _get_kwargs(
        account_number=account_number,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    account_number: str,
    *,
    client: AuthenticatedClient,

) -> DeleteByAccountNumberAccountCacheResponse200 | DeleteByAccountNumberAccountCacheResponse400 | DeleteByAccountNumberAccountCacheResponse401 | DeleteByAccountNumberAccountCacheResponse403 | DeleteByAccountNumberAccountCacheResponse404 | DeleteByAccountNumberAccountCacheResponse500 | None:
    """ Deletes the cached account with passed in account number.

    Args:
        account_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteByAccountNumberAccountCacheResponse200 | DeleteByAccountNumberAccountCacheResponse400 | DeleteByAccountNumberAccountCacheResponse401 | DeleteByAccountNumberAccountCacheResponse403 | DeleteByAccountNumberAccountCacheResponse404 | DeleteByAccountNumberAccountCacheResponse500
     """


    return (await asyncio_detailed(
        account_number=account_number,
client=client,

    )).parsed
