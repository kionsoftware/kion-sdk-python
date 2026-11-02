from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_billing_source_by_child_account_name_response_200 import GetBillingSourceByChildAccountNameResponse200
from ...models.get_billing_source_by_child_account_name_response_401 import GetBillingSourceByChildAccountNameResponse401
from ...models.get_billing_source_by_child_account_name_response_403 import GetBillingSourceByChildAccountNameResponse403
from ...models.get_billing_source_by_child_account_name_response_404 import GetBillingSourceByChildAccountNameResponse404
from ...models.get_billing_source_by_child_account_name_response_500 import GetBillingSourceByChildAccountNameResponse500
from typing import cast



def _get_kwargs(
    account_name: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/billing-source/by-child-account-name/{account_name}".format(account_name=quote(str(account_name), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetBillingSourceByChildAccountNameResponse200 | GetBillingSourceByChildAccountNameResponse401 | GetBillingSourceByChildAccountNameResponse403 | GetBillingSourceByChildAccountNameResponse404 | GetBillingSourceByChildAccountNameResponse500 | None:
    if response.status_code == 200:
        response_200 = GetBillingSourceByChildAccountNameResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetBillingSourceByChildAccountNameResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetBillingSourceByChildAccountNameResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetBillingSourceByChildAccountNameResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetBillingSourceByChildAccountNameResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetBillingSourceByChildAccountNameResponse200 | GetBillingSourceByChildAccountNameResponse401 | GetBillingSourceByChildAccountNameResponse403 | GetBillingSourceByChildAccountNameResponse404 | GetBillingSourceByChildAccountNameResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_name: str,
    *,
    client: AuthenticatedClient,

) -> Response[GetBillingSourceByChildAccountNameResponse200 | GetBillingSourceByChildAccountNameResponse401 | GetBillingSourceByChildAccountNameResponse403 | GetBillingSourceByChildAccountNameResponse404 | GetBillingSourceByChildAccountNameResponse500]:
    """ Finds a payer by its child account's account name in the application.

    Args:
        account_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBillingSourceByChildAccountNameResponse200 | GetBillingSourceByChildAccountNameResponse401 | GetBillingSourceByChildAccountNameResponse403 | GetBillingSourceByChildAccountNameResponse404 | GetBillingSourceByChildAccountNameResponse500]
     """


    kwargs = _get_kwargs(
        account_name=account_name,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    account_name: str,
    *,
    client: AuthenticatedClient,

) -> GetBillingSourceByChildAccountNameResponse200 | GetBillingSourceByChildAccountNameResponse401 | GetBillingSourceByChildAccountNameResponse403 | GetBillingSourceByChildAccountNameResponse404 | GetBillingSourceByChildAccountNameResponse500 | None:
    """ Finds a payer by its child account's account name in the application.

    Args:
        account_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBillingSourceByChildAccountNameResponse200 | GetBillingSourceByChildAccountNameResponse401 | GetBillingSourceByChildAccountNameResponse403 | GetBillingSourceByChildAccountNameResponse404 | GetBillingSourceByChildAccountNameResponse500
     """


    return sync_detailed(
        account_name=account_name,
client=client,

    ).parsed

async def asyncio_detailed(
    account_name: str,
    *,
    client: AuthenticatedClient,

) -> Response[GetBillingSourceByChildAccountNameResponse200 | GetBillingSourceByChildAccountNameResponse401 | GetBillingSourceByChildAccountNameResponse403 | GetBillingSourceByChildAccountNameResponse404 | GetBillingSourceByChildAccountNameResponse500]:
    """ Finds a payer by its child account's account name in the application.

    Args:
        account_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBillingSourceByChildAccountNameResponse200 | GetBillingSourceByChildAccountNameResponse401 | GetBillingSourceByChildAccountNameResponse403 | GetBillingSourceByChildAccountNameResponse404 | GetBillingSourceByChildAccountNameResponse500]
     """


    kwargs = _get_kwargs(
        account_name=account_name,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    account_name: str,
    *,
    client: AuthenticatedClient,

) -> GetBillingSourceByChildAccountNameResponse200 | GetBillingSourceByChildAccountNameResponse401 | GetBillingSourceByChildAccountNameResponse403 | GetBillingSourceByChildAccountNameResponse404 | GetBillingSourceByChildAccountNameResponse500 | None:
    """ Finds a payer by its child account's account name in the application.

    Args:
        account_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBillingSourceByChildAccountNameResponse200 | GetBillingSourceByChildAccountNameResponse401 | GetBillingSourceByChildAccountNameResponse403 | GetBillingSourceByChildAccountNameResponse404 | GetBillingSourceByChildAccountNameResponse500
     """


    return (await asyncio_detailed(
        account_name=account_name,
client=client,

    )).parsed
