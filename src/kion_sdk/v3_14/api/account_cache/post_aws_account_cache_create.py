from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.aws_account_cache_create import AWSAccountCacheCreate
from ...models.post_aws_account_cache_create_response_201 import PostAwsAccountCacheCreateResponse201
from ...models.post_aws_account_cache_create_response_400 import PostAwsAccountCacheCreateResponse400
from ...models.post_aws_account_cache_create_response_401 import PostAwsAccountCacheCreateResponse401
from ...models.post_aws_account_cache_create_response_403 import PostAwsAccountCacheCreateResponse403
from ...models.post_aws_account_cache_create_response_422 import PostAwsAccountCacheCreateResponse422
from ...models.post_aws_account_cache_create_response_500 import PostAwsAccountCacheCreateResponse500
from typing import cast



def _get_kwargs(
    *,
    body: AWSAccountCacheCreate,
    account_type: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["account-type"] = account_type


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/account-cache/__qs__/account-type/aws",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostAwsAccountCacheCreateResponse201 | PostAwsAccountCacheCreateResponse400 | PostAwsAccountCacheCreateResponse401 | PostAwsAccountCacheCreateResponse403 | PostAwsAccountCacheCreateResponse422 | PostAwsAccountCacheCreateResponse500 | None:
    if response.status_code == 201:
        response_201 = PostAwsAccountCacheCreateResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostAwsAccountCacheCreateResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostAwsAccountCacheCreateResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostAwsAccountCacheCreateResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostAwsAccountCacheCreateResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostAwsAccountCacheCreateResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostAwsAccountCacheCreateResponse201 | PostAwsAccountCacheCreateResponse400 | PostAwsAccountCacheCreateResponse401 | PostAwsAccountCacheCreateResponse403 | PostAwsAccountCacheCreateResponse422 | PostAwsAccountCacheCreateResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AWSAccountCacheCreate,
    account_type: str,

) -> Response[PostAwsAccountCacheCreateResponse201 | PostAwsAccountCacheCreateResponse400 | PostAwsAccountCacheCreateResponse401 | PostAwsAccountCacheCreateResponse403 | PostAwsAccountCacheCreateResponse422 | PostAwsAccountCacheCreateResponse500]:
    """ Imports an existing AWS Account to the account cache the in application.

    Args:
        account_type (str):
        body (AWSAccountCacheCreate): AWSAccountCacheCreate defines the object to create a cached
            account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAwsAccountCacheCreateResponse201 | PostAwsAccountCacheCreateResponse400 | PostAwsAccountCacheCreateResponse401 | PostAwsAccountCacheCreateResponse403 | PostAwsAccountCacheCreateResponse422 | PostAwsAccountCacheCreateResponse500]
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
    body: AWSAccountCacheCreate,
    account_type: str,

) -> PostAwsAccountCacheCreateResponse201 | PostAwsAccountCacheCreateResponse400 | PostAwsAccountCacheCreateResponse401 | PostAwsAccountCacheCreateResponse403 | PostAwsAccountCacheCreateResponse422 | PostAwsAccountCacheCreateResponse500 | None:
    """ Imports an existing AWS Account to the account cache the in application.

    Args:
        account_type (str):
        body (AWSAccountCacheCreate): AWSAccountCacheCreate defines the object to create a cached
            account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAwsAccountCacheCreateResponse201 | PostAwsAccountCacheCreateResponse400 | PostAwsAccountCacheCreateResponse401 | PostAwsAccountCacheCreateResponse403 | PostAwsAccountCacheCreateResponse422 | PostAwsAccountCacheCreateResponse500
     """


    return sync_detailed(
        client=client,
body=body,
account_type=account_type,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AWSAccountCacheCreate,
    account_type: str,

) -> Response[PostAwsAccountCacheCreateResponse201 | PostAwsAccountCacheCreateResponse400 | PostAwsAccountCacheCreateResponse401 | PostAwsAccountCacheCreateResponse403 | PostAwsAccountCacheCreateResponse422 | PostAwsAccountCacheCreateResponse500]:
    """ Imports an existing AWS Account to the account cache the in application.

    Args:
        account_type (str):
        body (AWSAccountCacheCreate): AWSAccountCacheCreate defines the object to create a cached
            account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAwsAccountCacheCreateResponse201 | PostAwsAccountCacheCreateResponse400 | PostAwsAccountCacheCreateResponse401 | PostAwsAccountCacheCreateResponse403 | PostAwsAccountCacheCreateResponse422 | PostAwsAccountCacheCreateResponse500]
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
    body: AWSAccountCacheCreate,
    account_type: str,

) -> PostAwsAccountCacheCreateResponse201 | PostAwsAccountCacheCreateResponse400 | PostAwsAccountCacheCreateResponse401 | PostAwsAccountCacheCreateResponse403 | PostAwsAccountCacheCreateResponse422 | PostAwsAccountCacheCreateResponse500 | None:
    """ Imports an existing AWS Account to the account cache the in application.

    Args:
        account_type (str):
        body (AWSAccountCacheCreate): AWSAccountCacheCreate defines the object to create a cached
            account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAwsAccountCacheCreateResponse201 | PostAwsAccountCacheCreateResponse400 | PostAwsAccountCacheCreateResponse401 | PostAwsAccountCacheCreateResponse403 | PostAwsAccountCacheCreateResponse422 | PostAwsAccountCacheCreateResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,
account_type=account_type,

    )).parsed
