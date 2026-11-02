from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.custom_account_cache_create import CustomAccountCacheCreate
from ...models.post_custom_account_cache_create_response_201 import PostCustomAccountCacheCreateResponse201
from ...models.post_custom_account_cache_create_response_400 import PostCustomAccountCacheCreateResponse400
from ...models.post_custom_account_cache_create_response_401 import PostCustomAccountCacheCreateResponse401
from ...models.post_custom_account_cache_create_response_403 import PostCustomAccountCacheCreateResponse403
from ...models.post_custom_account_cache_create_response_422 import PostCustomAccountCacheCreateResponse422
from ...models.post_custom_account_cache_create_response_500 import PostCustomAccountCacheCreateResponse500
from typing import cast



def _get_kwargs(
    *,
    body: CustomAccountCacheCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/account-cache/__qs__/account-type/custom",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostCustomAccountCacheCreateResponse201 | PostCustomAccountCacheCreateResponse400 | PostCustomAccountCacheCreateResponse401 | PostCustomAccountCacheCreateResponse403 | PostCustomAccountCacheCreateResponse422 | PostCustomAccountCacheCreateResponse500 | None:
    if response.status_code == 201:
        response_201 = PostCustomAccountCacheCreateResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostCustomAccountCacheCreateResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostCustomAccountCacheCreateResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostCustomAccountCacheCreateResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostCustomAccountCacheCreateResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostCustomAccountCacheCreateResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostCustomAccountCacheCreateResponse201 | PostCustomAccountCacheCreateResponse400 | PostCustomAccountCacheCreateResponse401 | PostCustomAccountCacheCreateResponse403 | PostCustomAccountCacheCreateResponse422 | PostCustomAccountCacheCreateResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CustomAccountCacheCreate,

) -> Response[PostCustomAccountCacheCreateResponse201 | PostCustomAccountCacheCreateResponse400 | PostCustomAccountCacheCreateResponse401 | PostCustomAccountCacheCreateResponse403 | PostCustomAccountCacheCreateResponse422 | PostCustomAccountCacheCreateResponse500]:
    """ Imports an existing Custom Account to the account cache in the application.

    Args:
        body (CustomAccountCacheCreate): CustomAccountCacheCreate defines a payload for a cached
            Custom account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostCustomAccountCacheCreateResponse201 | PostCustomAccountCacheCreateResponse400 | PostCustomAccountCacheCreateResponse401 | PostCustomAccountCacheCreateResponse403 | PostCustomAccountCacheCreateResponse422 | PostCustomAccountCacheCreateResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: CustomAccountCacheCreate,

) -> PostCustomAccountCacheCreateResponse201 | PostCustomAccountCacheCreateResponse400 | PostCustomAccountCacheCreateResponse401 | PostCustomAccountCacheCreateResponse403 | PostCustomAccountCacheCreateResponse422 | PostCustomAccountCacheCreateResponse500 | None:
    """ Imports an existing Custom Account to the account cache in the application.

    Args:
        body (CustomAccountCacheCreate): CustomAccountCacheCreate defines a payload for a cached
            Custom account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostCustomAccountCacheCreateResponse201 | PostCustomAccountCacheCreateResponse400 | PostCustomAccountCacheCreateResponse401 | PostCustomAccountCacheCreateResponse403 | PostCustomAccountCacheCreateResponse422 | PostCustomAccountCacheCreateResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CustomAccountCacheCreate,

) -> Response[PostCustomAccountCacheCreateResponse201 | PostCustomAccountCacheCreateResponse400 | PostCustomAccountCacheCreateResponse401 | PostCustomAccountCacheCreateResponse403 | PostCustomAccountCacheCreateResponse422 | PostCustomAccountCacheCreateResponse500]:
    """ Imports an existing Custom Account to the account cache in the application.

    Args:
        body (CustomAccountCacheCreate): CustomAccountCacheCreate defines a payload for a cached
            Custom account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostCustomAccountCacheCreateResponse201 | PostCustomAccountCacheCreateResponse400 | PostCustomAccountCacheCreateResponse401 | PostCustomAccountCacheCreateResponse403 | PostCustomAccountCacheCreateResponse422 | PostCustomAccountCacheCreateResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CustomAccountCacheCreate,

) -> PostCustomAccountCacheCreateResponse201 | PostCustomAccountCacheCreateResponse400 | PostCustomAccountCacheCreateResponse401 | PostCustomAccountCacheCreateResponse403 | PostCustomAccountCacheCreateResponse422 | PostCustomAccountCacheCreateResponse500 | None:
    """ Imports an existing Custom Account to the account cache in the application.

    Args:
        body (CustomAccountCacheCreate): CustomAccountCacheCreate defines a payload for a cached
            Custom account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostCustomAccountCacheCreateResponse201 | PostCustomAccountCacheCreateResponse400 | PostCustomAccountCacheCreateResponse401 | PostCustomAccountCacheCreateResponse403 | PostCustomAccountCacheCreateResponse422 | PostCustomAccountCacheCreateResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
