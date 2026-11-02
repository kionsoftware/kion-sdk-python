from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.revert_account_by_account_number_response_200 import RevertAccountByAccountNumberResponse200
from ...models.revert_account_by_account_number_response_400 import RevertAccountByAccountNumberResponse400
from ...models.revert_account_by_account_number_response_401 import RevertAccountByAccountNumberResponse401
from ...models.revert_account_by_account_number_response_403 import RevertAccountByAccountNumberResponse403
from ...models.revert_account_by_account_number_response_404 import RevertAccountByAccountNumberResponse404
from ...models.revert_account_by_account_number_response_500 import RevertAccountByAccountNumberResponse500
from typing import cast



def _get_kwargs(
    account_number: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/account/revert/by-account-number/{account_number}".format(account_number=quote(str(account_number), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RevertAccountByAccountNumberResponse200 | RevertAccountByAccountNumberResponse400 | RevertAccountByAccountNumberResponse401 | RevertAccountByAccountNumberResponse403 | RevertAccountByAccountNumberResponse404 | RevertAccountByAccountNumberResponse500 | None:
    if response.status_code == 200:
        response_200 = RevertAccountByAccountNumberResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = RevertAccountByAccountNumberResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = RevertAccountByAccountNumberResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = RevertAccountByAccountNumberResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = RevertAccountByAccountNumberResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = RevertAccountByAccountNumberResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RevertAccountByAccountNumberResponse200 | RevertAccountByAccountNumberResponse400 | RevertAccountByAccountNumberResponse401 | RevertAccountByAccountNumberResponse403 | RevertAccountByAccountNumberResponse404 | RevertAccountByAccountNumberResponse500]:
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

) -> Response[RevertAccountByAccountNumberResponse200 | RevertAccountByAccountNumberResponse400 | RevertAccountByAccountNumberResponse401 | RevertAccountByAccountNumberResponse403 | RevertAccountByAccountNumberResponse404 | RevertAccountByAccountNumberResponse500]:
    """ Reverts the account with passed in account number by moving the account into the account cache.

    Args:
        account_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RevertAccountByAccountNumberResponse200 | RevertAccountByAccountNumberResponse400 | RevertAccountByAccountNumberResponse401 | RevertAccountByAccountNumberResponse403 | RevertAccountByAccountNumberResponse404 | RevertAccountByAccountNumberResponse500]
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

) -> RevertAccountByAccountNumberResponse200 | RevertAccountByAccountNumberResponse400 | RevertAccountByAccountNumberResponse401 | RevertAccountByAccountNumberResponse403 | RevertAccountByAccountNumberResponse404 | RevertAccountByAccountNumberResponse500 | None:
    """ Reverts the account with passed in account number by moving the account into the account cache.

    Args:
        account_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RevertAccountByAccountNumberResponse200 | RevertAccountByAccountNumberResponse400 | RevertAccountByAccountNumberResponse401 | RevertAccountByAccountNumberResponse403 | RevertAccountByAccountNumberResponse404 | RevertAccountByAccountNumberResponse500
     """


    return sync_detailed(
        account_number=account_number,
client=client,

    ).parsed

async def asyncio_detailed(
    account_number: str,
    *,
    client: AuthenticatedClient,

) -> Response[RevertAccountByAccountNumberResponse200 | RevertAccountByAccountNumberResponse400 | RevertAccountByAccountNumberResponse401 | RevertAccountByAccountNumberResponse403 | RevertAccountByAccountNumberResponse404 | RevertAccountByAccountNumberResponse500]:
    """ Reverts the account with passed in account number by moving the account into the account cache.

    Args:
        account_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RevertAccountByAccountNumberResponse200 | RevertAccountByAccountNumberResponse400 | RevertAccountByAccountNumberResponse401 | RevertAccountByAccountNumberResponse403 | RevertAccountByAccountNumberResponse404 | RevertAccountByAccountNumberResponse500]
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

) -> RevertAccountByAccountNumberResponse200 | RevertAccountByAccountNumberResponse400 | RevertAccountByAccountNumberResponse401 | RevertAccountByAccountNumberResponse403 | RevertAccountByAccountNumberResponse404 | RevertAccountByAccountNumberResponse500 | None:
    """ Reverts the account with passed in account number by moving the account into the account cache.

    Args:
        account_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RevertAccountByAccountNumberResponse200 | RevertAccountByAccountNumberResponse400 | RevertAccountByAccountNumberResponse401 | RevertAccountByAccountNumberResponse403 | RevertAccountByAccountNumberResponse404 | RevertAccountByAccountNumberResponse500
     """


    return (await asyncio_detailed(
        account_number=account_number,
client=client,

    )).parsed
