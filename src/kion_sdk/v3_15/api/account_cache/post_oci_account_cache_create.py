from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.oci_account_cache_create import OCIAccountCacheCreate
from ...models.post_oci_account_cache_create_response_201 import PostOciAccountCacheCreateResponse201
from ...models.post_oci_account_cache_create_response_400 import PostOciAccountCacheCreateResponse400
from ...models.post_oci_account_cache_create_response_401 import PostOciAccountCacheCreateResponse401
from ...models.post_oci_account_cache_create_response_403 import PostOciAccountCacheCreateResponse403
from ...models.post_oci_account_cache_create_response_422 import PostOciAccountCacheCreateResponse422
from ...models.post_oci_account_cache_create_response_500 import PostOciAccountCacheCreateResponse500
from typing import cast



def _get_kwargs(
    *,
    body: OCIAccountCacheCreate,
    account_type: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["account-type"] = account_type


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/account-cache/__qs__/account-type/oci",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostOciAccountCacheCreateResponse201 | PostOciAccountCacheCreateResponse400 | PostOciAccountCacheCreateResponse401 | PostOciAccountCacheCreateResponse403 | PostOciAccountCacheCreateResponse422 | PostOciAccountCacheCreateResponse500 | None:
    if response.status_code == 201:
        response_201 = PostOciAccountCacheCreateResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostOciAccountCacheCreateResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostOciAccountCacheCreateResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostOciAccountCacheCreateResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostOciAccountCacheCreateResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostOciAccountCacheCreateResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostOciAccountCacheCreateResponse201 | PostOciAccountCacheCreateResponse400 | PostOciAccountCacheCreateResponse401 | PostOciAccountCacheCreateResponse403 | PostOciAccountCacheCreateResponse422 | PostOciAccountCacheCreateResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: OCIAccountCacheCreate,
    account_type: str,

) -> Response[PostOciAccountCacheCreateResponse201 | PostOciAccountCacheCreateResponse400 | PostOciAccountCacheCreateResponse401 | PostOciAccountCacheCreateResponse403 | PostOciAccountCacheCreateResponse422 | PostOciAccountCacheCreateResponse500]:
    """ Imports an existing Oracle Cloud Infrastructure Account to the account cache in the application.

    Args:
        account_type (str):
        body (OCIAccountCacheCreate): OCIAccountCacheCreate defines a payload for a cached OCI
            account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostOciAccountCacheCreateResponse201 | PostOciAccountCacheCreateResponse400 | PostOciAccountCacheCreateResponse401 | PostOciAccountCacheCreateResponse403 | PostOciAccountCacheCreateResponse422 | PostOciAccountCacheCreateResponse500]
     """


    kwargs = _get_kwargs(
        body=body,
account_type=account_type,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: OCIAccountCacheCreate,
    account_type: str,

) -> PostOciAccountCacheCreateResponse201 | PostOciAccountCacheCreateResponse400 | PostOciAccountCacheCreateResponse401 | PostOciAccountCacheCreateResponse403 | PostOciAccountCacheCreateResponse422 | PostOciAccountCacheCreateResponse500 | None:
    """ Imports an existing Oracle Cloud Infrastructure Account to the account cache in the application.

    Args:
        account_type (str):
        body (OCIAccountCacheCreate): OCIAccountCacheCreate defines a payload for a cached OCI
            account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostOciAccountCacheCreateResponse201 | PostOciAccountCacheCreateResponse400 | PostOciAccountCacheCreateResponse401 | PostOciAccountCacheCreateResponse403 | PostOciAccountCacheCreateResponse422 | PostOciAccountCacheCreateResponse500
     """


    return sync_detailed(
        client=client,
body=body,
account_type=account_type,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: OCIAccountCacheCreate,
    account_type: str,

) -> Response[PostOciAccountCacheCreateResponse201 | PostOciAccountCacheCreateResponse400 | PostOciAccountCacheCreateResponse401 | PostOciAccountCacheCreateResponse403 | PostOciAccountCacheCreateResponse422 | PostOciAccountCacheCreateResponse500]:
    """ Imports an existing Oracle Cloud Infrastructure Account to the account cache in the application.

    Args:
        account_type (str):
        body (OCIAccountCacheCreate): OCIAccountCacheCreate defines a payload for a cached OCI
            account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostOciAccountCacheCreateResponse201 | PostOciAccountCacheCreateResponse400 | PostOciAccountCacheCreateResponse401 | PostOciAccountCacheCreateResponse403 | PostOciAccountCacheCreateResponse422 | PostOciAccountCacheCreateResponse500]
     """


    kwargs = _get_kwargs(
        body=body,
account_type=account_type,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: OCIAccountCacheCreate,
    account_type: str,

) -> PostOciAccountCacheCreateResponse201 | PostOciAccountCacheCreateResponse400 | PostOciAccountCacheCreateResponse401 | PostOciAccountCacheCreateResponse403 | PostOciAccountCacheCreateResponse422 | PostOciAccountCacheCreateResponse500 | None:
    """ Imports an existing Oracle Cloud Infrastructure Account to the account cache in the application.

    Args:
        account_type (str):
        body (OCIAccountCacheCreate): OCIAccountCacheCreate defines a payload for a cached OCI
            account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostOciAccountCacheCreateResponse201 | PostOciAccountCacheCreateResponse400 | PostOciAccountCacheCreateResponse401 | PostOciAccountCacheCreateResponse403 | PostOciAccountCacheCreateResponse422 | PostOciAccountCacheCreateResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,
account_type=account_type,

    )).parsed
