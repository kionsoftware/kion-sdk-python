from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_link_all_payer_accounts_response_200 import PostLinkAllPayerAccountsResponse200
from ...models.post_link_all_payer_accounts_response_400 import PostLinkAllPayerAccountsResponse400
from ...models.post_link_all_payer_accounts_response_401 import PostLinkAllPayerAccountsResponse401
from ...models.post_link_all_payer_accounts_response_403 import PostLinkAllPayerAccountsResponse403
from ...models.post_link_all_payer_accounts_response_422 import PostLinkAllPayerAccountsResponse422
from ...models.post_link_all_payer_accounts_response_500 import PostLinkAllPayerAccountsResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/payer/{id}/link-all-accounts".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostLinkAllPayerAccountsResponse200 | PostLinkAllPayerAccountsResponse400 | PostLinkAllPayerAccountsResponse401 | PostLinkAllPayerAccountsResponse403 | PostLinkAllPayerAccountsResponse422 | PostLinkAllPayerAccountsResponse500 | None:
    if response.status_code == 200:
        response_200 = PostLinkAllPayerAccountsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PostLinkAllPayerAccountsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostLinkAllPayerAccountsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostLinkAllPayerAccountsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostLinkAllPayerAccountsResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostLinkAllPayerAccountsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostLinkAllPayerAccountsResponse200 | PostLinkAllPayerAccountsResponse400 | PostLinkAllPayerAccountsResponse401 | PostLinkAllPayerAccountsResponse403 | PostLinkAllPayerAccountsResponse422 | PostLinkAllPayerAccountsResponse500]:
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

) -> Response[PostLinkAllPayerAccountsResponse200 | PostLinkAllPayerAccountsResponse400 | PostLinkAllPayerAccountsResponse401 | PostLinkAllPayerAccountsResponse403 | PostLinkAllPayerAccountsResponse422 | PostLinkAllPayerAccountsResponse500]:
    """ Links all accounts from the organization to Kion.

     The added accounts will be available in the cache.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostLinkAllPayerAccountsResponse200 | PostLinkAllPayerAccountsResponse400 | PostLinkAllPayerAccountsResponse401 | PostLinkAllPayerAccountsResponse403 | PostLinkAllPayerAccountsResponse422 | PostLinkAllPayerAccountsResponse500]
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

) -> PostLinkAllPayerAccountsResponse200 | PostLinkAllPayerAccountsResponse400 | PostLinkAllPayerAccountsResponse401 | PostLinkAllPayerAccountsResponse403 | PostLinkAllPayerAccountsResponse422 | PostLinkAllPayerAccountsResponse500 | None:
    """ Links all accounts from the organization to Kion.

     The added accounts will be available in the cache.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostLinkAllPayerAccountsResponse200 | PostLinkAllPayerAccountsResponse400 | PostLinkAllPayerAccountsResponse401 | PostLinkAllPayerAccountsResponse403 | PostLinkAllPayerAccountsResponse422 | PostLinkAllPayerAccountsResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[PostLinkAllPayerAccountsResponse200 | PostLinkAllPayerAccountsResponse400 | PostLinkAllPayerAccountsResponse401 | PostLinkAllPayerAccountsResponse403 | PostLinkAllPayerAccountsResponse422 | PostLinkAllPayerAccountsResponse500]:
    """ Links all accounts from the organization to Kion.

     The added accounts will be available in the cache.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostLinkAllPayerAccountsResponse200 | PostLinkAllPayerAccountsResponse400 | PostLinkAllPayerAccountsResponse401 | PostLinkAllPayerAccountsResponse403 | PostLinkAllPayerAccountsResponse422 | PostLinkAllPayerAccountsResponse500]
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

) -> PostLinkAllPayerAccountsResponse200 | PostLinkAllPayerAccountsResponse400 | PostLinkAllPayerAccountsResponse401 | PostLinkAllPayerAccountsResponse403 | PostLinkAllPayerAccountsResponse422 | PostLinkAllPayerAccountsResponse500 | None:
    """ Links all accounts from the organization to Kion.

     The added accounts will be available in the cache.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostLinkAllPayerAccountsResponse200 | PostLinkAllPayerAccountsResponse400 | PostLinkAllPayerAccountsResponse401 | PostLinkAllPayerAccountsResponse403 | PostLinkAllPayerAccountsResponse422 | PostLinkAllPayerAccountsResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
