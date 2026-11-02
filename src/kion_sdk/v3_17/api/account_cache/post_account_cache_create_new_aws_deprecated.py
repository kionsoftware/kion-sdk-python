from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_account_cache_create_new_aws_deprecated_response_201 import PostAccountCacheCreateNewAWSDeprecatedResponse201
from ...models.post_account_cache_create_new_aws_deprecated_response_400 import PostAccountCacheCreateNewAWSDeprecatedResponse400
from ...models.post_account_cache_create_new_aws_deprecated_response_401 import PostAccountCacheCreateNewAWSDeprecatedResponse401
from ...models.post_account_cache_create_new_aws_deprecated_response_403 import PostAccountCacheCreateNewAWSDeprecatedResponse403
from ...models.post_account_cache_create_new_aws_deprecated_response_422 import PostAccountCacheCreateNewAWSDeprecatedResponse422
from ...models.post_account_cache_create_new_aws_deprecated_response_500 import PostAccountCacheCreateNewAWSDeprecatedResponse500
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/account-cache/aws",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostAccountCacheCreateNewAWSDeprecatedResponse201 | PostAccountCacheCreateNewAWSDeprecatedResponse400 | PostAccountCacheCreateNewAWSDeprecatedResponse401 | PostAccountCacheCreateNewAWSDeprecatedResponse403 | PostAccountCacheCreateNewAWSDeprecatedResponse422 | PostAccountCacheCreateNewAWSDeprecatedResponse500 | None:
    if response.status_code == 201:
        response_201 = PostAccountCacheCreateNewAWSDeprecatedResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostAccountCacheCreateNewAWSDeprecatedResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostAccountCacheCreateNewAWSDeprecatedResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostAccountCacheCreateNewAWSDeprecatedResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostAccountCacheCreateNewAWSDeprecatedResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostAccountCacheCreateNewAWSDeprecatedResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostAccountCacheCreateNewAWSDeprecatedResponse201 | PostAccountCacheCreateNewAWSDeprecatedResponse400 | PostAccountCacheCreateNewAWSDeprecatedResponse401 | PostAccountCacheCreateNewAWSDeprecatedResponse403 | PostAccountCacheCreateNewAWSDeprecatedResponse422 | PostAccountCacheCreateNewAWSDeprecatedResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[PostAccountCacheCreateNewAWSDeprecatedResponse201 | PostAccountCacheCreateNewAWSDeprecatedResponse400 | PostAccountCacheCreateNewAWSDeprecatedResponse401 | PostAccountCacheCreateNewAWSDeprecatedResponse403 | PostAccountCacheCreateNewAWSDeprecatedResponse422 | PostAccountCacheCreateNewAWSDeprecatedResponse500]:
    """ Create a new AWS account via the Organizations API.

     This is deprecated but retained for backwards compatibility.
    Use POST /v3/account-cache/create?account-type=aws instead.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAccountCacheCreateNewAWSDeprecatedResponse201 | PostAccountCacheCreateNewAWSDeprecatedResponse400 | PostAccountCacheCreateNewAWSDeprecatedResponse401 | PostAccountCacheCreateNewAWSDeprecatedResponse403 | PostAccountCacheCreateNewAWSDeprecatedResponse422 | PostAccountCacheCreateNewAWSDeprecatedResponse500]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,

) -> PostAccountCacheCreateNewAWSDeprecatedResponse201 | PostAccountCacheCreateNewAWSDeprecatedResponse400 | PostAccountCacheCreateNewAWSDeprecatedResponse401 | PostAccountCacheCreateNewAWSDeprecatedResponse403 | PostAccountCacheCreateNewAWSDeprecatedResponse422 | PostAccountCacheCreateNewAWSDeprecatedResponse500 | None:
    """ Create a new AWS account via the Organizations API.

     This is deprecated but retained for backwards compatibility.
    Use POST /v3/account-cache/create?account-type=aws instead.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAccountCacheCreateNewAWSDeprecatedResponse201 | PostAccountCacheCreateNewAWSDeprecatedResponse400 | PostAccountCacheCreateNewAWSDeprecatedResponse401 | PostAccountCacheCreateNewAWSDeprecatedResponse403 | PostAccountCacheCreateNewAWSDeprecatedResponse422 | PostAccountCacheCreateNewAWSDeprecatedResponse500
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[PostAccountCacheCreateNewAWSDeprecatedResponse201 | PostAccountCacheCreateNewAWSDeprecatedResponse400 | PostAccountCacheCreateNewAWSDeprecatedResponse401 | PostAccountCacheCreateNewAWSDeprecatedResponse403 | PostAccountCacheCreateNewAWSDeprecatedResponse422 | PostAccountCacheCreateNewAWSDeprecatedResponse500]:
    """ Create a new AWS account via the Organizations API.

     This is deprecated but retained for backwards compatibility.
    Use POST /v3/account-cache/create?account-type=aws instead.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAccountCacheCreateNewAWSDeprecatedResponse201 | PostAccountCacheCreateNewAWSDeprecatedResponse400 | PostAccountCacheCreateNewAWSDeprecatedResponse401 | PostAccountCacheCreateNewAWSDeprecatedResponse403 | PostAccountCacheCreateNewAWSDeprecatedResponse422 | PostAccountCacheCreateNewAWSDeprecatedResponse500]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,

) -> PostAccountCacheCreateNewAWSDeprecatedResponse201 | PostAccountCacheCreateNewAWSDeprecatedResponse400 | PostAccountCacheCreateNewAWSDeprecatedResponse401 | PostAccountCacheCreateNewAWSDeprecatedResponse403 | PostAccountCacheCreateNewAWSDeprecatedResponse422 | PostAccountCacheCreateNewAWSDeprecatedResponse500 | None:
    """ Create a new AWS account via the Organizations API.

     This is deprecated but retained for backwards compatibility.
    Use POST /v3/account-cache/create?account-type=aws instead.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAccountCacheCreateNewAWSDeprecatedResponse201 | PostAccountCacheCreateNewAWSDeprecatedResponse400 | PostAccountCacheCreateNewAWSDeprecatedResponse401 | PostAccountCacheCreateNewAWSDeprecatedResponse403 | PostAccountCacheCreateNewAWSDeprecatedResponse422 | PostAccountCacheCreateNewAWSDeprecatedResponse500
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
