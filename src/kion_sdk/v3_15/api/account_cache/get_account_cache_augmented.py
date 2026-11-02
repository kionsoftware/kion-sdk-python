from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_account_cache_augmented_response_200 import GetAccountCacheAugmentedResponse200
from ...models.get_account_cache_augmented_response_400 import GetAccountCacheAugmentedResponse400
from ...models.get_account_cache_augmented_response_401 import GetAccountCacheAugmentedResponse401
from ...models.get_account_cache_augmented_response_403 import GetAccountCacheAugmentedResponse403
from ...models.get_account_cache_augmented_response_404 import GetAccountCacheAugmentedResponse404
from ...models.get_account_cache_augmented_response_500 import GetAccountCacheAugmentedResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    query: str | Unset = UNSET,
    account_type_id: int | Unset = UNSET,
    payer_id: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["query"] = query

    params["account_type_id"] = account_type_id

    params["payer_id"] = payer_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/account-cache/search",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetAccountCacheAugmentedResponse200 | GetAccountCacheAugmentedResponse400 | GetAccountCacheAugmentedResponse401 | GetAccountCacheAugmentedResponse403 | GetAccountCacheAugmentedResponse404 | GetAccountCacheAugmentedResponse500 | None:
    if response.status_code == 200:
        response_200 = GetAccountCacheAugmentedResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetAccountCacheAugmentedResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetAccountCacheAugmentedResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetAccountCacheAugmentedResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetAccountCacheAugmentedResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetAccountCacheAugmentedResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetAccountCacheAugmentedResponse200 | GetAccountCacheAugmentedResponse400 | GetAccountCacheAugmentedResponse401 | GetAccountCacheAugmentedResponse403 | GetAccountCacheAugmentedResponse404 | GetAccountCacheAugmentedResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    query: str | Unset = UNSET,
    account_type_id: int | Unset = UNSET,
    payer_id: int | Unset = UNSET,

) -> Response[GetAccountCacheAugmentedResponse200 | GetAccountCacheAugmentedResponse400 | GetAccountCacheAugmentedResponse401 | GetAccountCacheAugmentedResponse403 | GetAccountCacheAugmentedResponse404 | GetAccountCacheAugmentedResponse500]:
    """ Get account cache objects based on a filters passed through params.

    Args:
        query (str | Unset):
        account_type_id (int | Unset):
        payer_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountCacheAugmentedResponse200 | GetAccountCacheAugmentedResponse400 | GetAccountCacheAugmentedResponse401 | GetAccountCacheAugmentedResponse403 | GetAccountCacheAugmentedResponse404 | GetAccountCacheAugmentedResponse500]
     """


    kwargs = _get_kwargs(
        query=query,
account_type_id=account_type_id,
payer_id=payer_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    query: str | Unset = UNSET,
    account_type_id: int | Unset = UNSET,
    payer_id: int | Unset = UNSET,

) -> GetAccountCacheAugmentedResponse200 | GetAccountCacheAugmentedResponse400 | GetAccountCacheAugmentedResponse401 | GetAccountCacheAugmentedResponse403 | GetAccountCacheAugmentedResponse404 | GetAccountCacheAugmentedResponse500 | None:
    """ Get account cache objects based on a filters passed through params.

    Args:
        query (str | Unset):
        account_type_id (int | Unset):
        payer_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountCacheAugmentedResponse200 | GetAccountCacheAugmentedResponse400 | GetAccountCacheAugmentedResponse401 | GetAccountCacheAugmentedResponse403 | GetAccountCacheAugmentedResponse404 | GetAccountCacheAugmentedResponse500
     """


    return sync_detailed(
        client=client,
query=query,
account_type_id=account_type_id,
payer_id=payer_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    query: str | Unset = UNSET,
    account_type_id: int | Unset = UNSET,
    payer_id: int | Unset = UNSET,

) -> Response[GetAccountCacheAugmentedResponse200 | GetAccountCacheAugmentedResponse400 | GetAccountCacheAugmentedResponse401 | GetAccountCacheAugmentedResponse403 | GetAccountCacheAugmentedResponse404 | GetAccountCacheAugmentedResponse500]:
    """ Get account cache objects based on a filters passed through params.

    Args:
        query (str | Unset):
        account_type_id (int | Unset):
        payer_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountCacheAugmentedResponse200 | GetAccountCacheAugmentedResponse400 | GetAccountCacheAugmentedResponse401 | GetAccountCacheAugmentedResponse403 | GetAccountCacheAugmentedResponse404 | GetAccountCacheAugmentedResponse500]
     """


    kwargs = _get_kwargs(
        query=query,
account_type_id=account_type_id,
payer_id=payer_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    query: str | Unset = UNSET,
    account_type_id: int | Unset = UNSET,
    payer_id: int | Unset = UNSET,

) -> GetAccountCacheAugmentedResponse200 | GetAccountCacheAugmentedResponse400 | GetAccountCacheAugmentedResponse401 | GetAccountCacheAugmentedResponse403 | GetAccountCacheAugmentedResponse404 | GetAccountCacheAugmentedResponse500 | None:
    """ Get account cache objects based on a filters passed through params.

    Args:
        query (str | Unset):
        account_type_id (int | Unset):
        payer_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountCacheAugmentedResponse200 | GetAccountCacheAugmentedResponse400 | GetAccountCacheAugmentedResponse401 | GetAccountCacheAugmentedResponse403 | GetAccountCacheAugmentedResponse404 | GetAccountCacheAugmentedResponse500
     """


    return (await asyncio_detailed(
        client=client,
query=query,
account_type_id=account_type_id,
payer_id=payer_id,

    )).parsed
