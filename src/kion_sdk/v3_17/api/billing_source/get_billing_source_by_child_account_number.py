from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_billing_source_by_child_account_number_response_200 import GetBillingSourceByChildAccountNumberResponse200
from ...models.get_billing_source_by_child_account_number_response_401 import GetBillingSourceByChildAccountNumberResponse401
from ...models.get_billing_source_by_child_account_number_response_403 import GetBillingSourceByChildAccountNumberResponse403
from ...models.get_billing_source_by_child_account_number_response_404 import GetBillingSourceByChildAccountNumberResponse404
from ...models.get_billing_source_by_child_account_number_response_500 import GetBillingSourceByChildAccountNumberResponse500
from typing import cast



def _get_kwargs(
    account_number: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/billing-source/by-child-account-number/{account_number}".format(account_number=quote(str(account_number), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetBillingSourceByChildAccountNumberResponse200 | GetBillingSourceByChildAccountNumberResponse401 | GetBillingSourceByChildAccountNumberResponse403 | GetBillingSourceByChildAccountNumberResponse404 | GetBillingSourceByChildAccountNumberResponse500 | None:
    if response.status_code == 200:
        response_200 = GetBillingSourceByChildAccountNumberResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetBillingSourceByChildAccountNumberResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetBillingSourceByChildAccountNumberResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetBillingSourceByChildAccountNumberResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetBillingSourceByChildAccountNumberResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetBillingSourceByChildAccountNumberResponse200 | GetBillingSourceByChildAccountNumberResponse401 | GetBillingSourceByChildAccountNumberResponse403 | GetBillingSourceByChildAccountNumberResponse404 | GetBillingSourceByChildAccountNumberResponse500]:
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

) -> Response[GetBillingSourceByChildAccountNumberResponse200 | GetBillingSourceByChildAccountNumberResponse401 | GetBillingSourceByChildAccountNumberResponse403 | GetBillingSourceByChildAccountNumberResponse404 | GetBillingSourceByChildAccountNumberResponse500]:
    """ Finds a payer by its child account's account number in the application.

    Args:
        account_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBillingSourceByChildAccountNumberResponse200 | GetBillingSourceByChildAccountNumberResponse401 | GetBillingSourceByChildAccountNumberResponse403 | GetBillingSourceByChildAccountNumberResponse404 | GetBillingSourceByChildAccountNumberResponse500]
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

) -> GetBillingSourceByChildAccountNumberResponse200 | GetBillingSourceByChildAccountNumberResponse401 | GetBillingSourceByChildAccountNumberResponse403 | GetBillingSourceByChildAccountNumberResponse404 | GetBillingSourceByChildAccountNumberResponse500 | None:
    """ Finds a payer by its child account's account number in the application.

    Args:
        account_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBillingSourceByChildAccountNumberResponse200 | GetBillingSourceByChildAccountNumberResponse401 | GetBillingSourceByChildAccountNumberResponse403 | GetBillingSourceByChildAccountNumberResponse404 | GetBillingSourceByChildAccountNumberResponse500
     """


    return sync_detailed(
        account_number=account_number,
client=client,

    ).parsed

async def asyncio_detailed(
    account_number: str,
    *,
    client: AuthenticatedClient,

) -> Response[GetBillingSourceByChildAccountNumberResponse200 | GetBillingSourceByChildAccountNumberResponse401 | GetBillingSourceByChildAccountNumberResponse403 | GetBillingSourceByChildAccountNumberResponse404 | GetBillingSourceByChildAccountNumberResponse500]:
    """ Finds a payer by its child account's account number in the application.

    Args:
        account_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBillingSourceByChildAccountNumberResponse200 | GetBillingSourceByChildAccountNumberResponse401 | GetBillingSourceByChildAccountNumberResponse403 | GetBillingSourceByChildAccountNumberResponse404 | GetBillingSourceByChildAccountNumberResponse500]
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

) -> GetBillingSourceByChildAccountNumberResponse200 | GetBillingSourceByChildAccountNumberResponse401 | GetBillingSourceByChildAccountNumberResponse403 | GetBillingSourceByChildAccountNumberResponse404 | GetBillingSourceByChildAccountNumberResponse500 | None:
    """ Finds a payer by its child account's account number in the application.

    Args:
        account_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBillingSourceByChildAccountNumberResponse200 | GetBillingSourceByChildAccountNumberResponse401 | GetBillingSourceByChildAccountNumberResponse403 | GetBillingSourceByChildAccountNumberResponse404 | GetBillingSourceByChildAccountNumberResponse500
     """


    return (await asyncio_detailed(
        account_number=account_number,
client=client,

    )).parsed
