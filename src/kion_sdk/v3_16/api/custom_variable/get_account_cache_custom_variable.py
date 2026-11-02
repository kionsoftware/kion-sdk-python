from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_account_cache_custom_variable_response_200 import GetAccountCacheCustomVariableResponse200
from ...models.get_account_cache_custom_variable_response_400 import GetAccountCacheCustomVariableResponse400
from ...models.get_account_cache_custom_variable_response_401 import GetAccountCacheCustomVariableResponse401
from ...models.get_account_cache_custom_variable_response_403 import GetAccountCacheCustomVariableResponse403
from ...models.get_account_cache_custom_variable_response_404 import GetAccountCacheCustomVariableResponse404
from ...models.get_account_cache_custom_variable_response_500 import GetAccountCacheCustomVariableResponse500
from typing import cast



def _get_kwargs(
    account_cache_id: int,
    custom_variable_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/account-cache/{account_cache_id}/custom-variable/{custom_variable_id}".format(account_cache_id=quote(str(account_cache_id), safe=""),custom_variable_id=quote(str(custom_variable_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetAccountCacheCustomVariableResponse200 | GetAccountCacheCustomVariableResponse400 | GetAccountCacheCustomVariableResponse401 | GetAccountCacheCustomVariableResponse403 | GetAccountCacheCustomVariableResponse404 | GetAccountCacheCustomVariableResponse500 | None:
    if response.status_code == 200:
        response_200 = GetAccountCacheCustomVariableResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetAccountCacheCustomVariableResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetAccountCacheCustomVariableResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetAccountCacheCustomVariableResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetAccountCacheCustomVariableResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetAccountCacheCustomVariableResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetAccountCacheCustomVariableResponse200 | GetAccountCacheCustomVariableResponse400 | GetAccountCacheCustomVariableResponse401 | GetAccountCacheCustomVariableResponse403 | GetAccountCacheCustomVariableResponse404 | GetAccountCacheCustomVariableResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_cache_id: int,
    custom_variable_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetAccountCacheCustomVariableResponse200 | GetAccountCacheCustomVariableResponse400 | GetAccountCacheCustomVariableResponse401 | GetAccountCacheCustomVariableResponse403 | GetAccountCacheCustomVariableResponse404 | GetAccountCacheCustomVariableResponse500]:
    """ Returns an account cache custom variable override.

    Args:
        account_cache_id (int):
        custom_variable_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountCacheCustomVariableResponse200 | GetAccountCacheCustomVariableResponse400 | GetAccountCacheCustomVariableResponse401 | GetAccountCacheCustomVariableResponse403 | GetAccountCacheCustomVariableResponse404 | GetAccountCacheCustomVariableResponse500]
     """


    kwargs = _get_kwargs(
        account_cache_id=account_cache_id,
custom_variable_id=custom_variable_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    account_cache_id: int,
    custom_variable_id: int,
    *,
    client: AuthenticatedClient,

) -> GetAccountCacheCustomVariableResponse200 | GetAccountCacheCustomVariableResponse400 | GetAccountCacheCustomVariableResponse401 | GetAccountCacheCustomVariableResponse403 | GetAccountCacheCustomVariableResponse404 | GetAccountCacheCustomVariableResponse500 | None:
    """ Returns an account cache custom variable override.

    Args:
        account_cache_id (int):
        custom_variable_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountCacheCustomVariableResponse200 | GetAccountCacheCustomVariableResponse400 | GetAccountCacheCustomVariableResponse401 | GetAccountCacheCustomVariableResponse403 | GetAccountCacheCustomVariableResponse404 | GetAccountCacheCustomVariableResponse500
     """


    return sync_detailed(
        account_cache_id=account_cache_id,
custom_variable_id=custom_variable_id,
client=client,

    ).parsed

async def asyncio_detailed(
    account_cache_id: int,
    custom_variable_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetAccountCacheCustomVariableResponse200 | GetAccountCacheCustomVariableResponse400 | GetAccountCacheCustomVariableResponse401 | GetAccountCacheCustomVariableResponse403 | GetAccountCacheCustomVariableResponse404 | GetAccountCacheCustomVariableResponse500]:
    """ Returns an account cache custom variable override.

    Args:
        account_cache_id (int):
        custom_variable_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountCacheCustomVariableResponse200 | GetAccountCacheCustomVariableResponse400 | GetAccountCacheCustomVariableResponse401 | GetAccountCacheCustomVariableResponse403 | GetAccountCacheCustomVariableResponse404 | GetAccountCacheCustomVariableResponse500]
     """


    kwargs = _get_kwargs(
        account_cache_id=account_cache_id,
custom_variable_id=custom_variable_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    account_cache_id: int,
    custom_variable_id: int,
    *,
    client: AuthenticatedClient,

) -> GetAccountCacheCustomVariableResponse200 | GetAccountCacheCustomVariableResponse400 | GetAccountCacheCustomVariableResponse401 | GetAccountCacheCustomVariableResponse403 | GetAccountCacheCustomVariableResponse404 | GetAccountCacheCustomVariableResponse500 | None:
    """ Returns an account cache custom variable override.

    Args:
        account_cache_id (int):
        custom_variable_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountCacheCustomVariableResponse200 | GetAccountCacheCustomVariableResponse400 | GetAccountCacheCustomVariableResponse401 | GetAccountCacheCustomVariableResponse403 | GetAccountCacheCustomVariableResponse404 | GetAccountCacheCustomVariableResponse500
     """


    return (await asyncio_detailed(
        account_cache_id=account_cache_id,
custom_variable_id=custom_variable_id,
client=client,

    )).parsed
