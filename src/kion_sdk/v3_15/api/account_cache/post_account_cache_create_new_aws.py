from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.aws_account_cache_new_aws_account import AWSAccountCacheNewAWSAccount
from ...models.post_account_cache_create_new_aws_response_201 import PostAccountCacheCreateNewAWSResponse201
from ...models.post_account_cache_create_new_aws_response_400 import PostAccountCacheCreateNewAWSResponse400
from ...models.post_account_cache_create_new_aws_response_401 import PostAccountCacheCreateNewAWSResponse401
from ...models.post_account_cache_create_new_aws_response_403 import PostAccountCacheCreateNewAWSResponse403
from ...models.post_account_cache_create_new_aws_response_422 import PostAccountCacheCreateNewAWSResponse422
from ...models.post_account_cache_create_new_aws_response_500 import PostAccountCacheCreateNewAWSResponse500
from typing import cast



def _get_kwargs(
    *,
    body: AWSAccountCacheNewAWSAccount,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/account-cache/create/__qs__/account-type/aws",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostAccountCacheCreateNewAWSResponse201 | PostAccountCacheCreateNewAWSResponse400 | PostAccountCacheCreateNewAWSResponse401 | PostAccountCacheCreateNewAWSResponse403 | PostAccountCacheCreateNewAWSResponse422 | PostAccountCacheCreateNewAWSResponse500 | None:
    if response.status_code == 201:
        response_201 = PostAccountCacheCreateNewAWSResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostAccountCacheCreateNewAWSResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostAccountCacheCreateNewAWSResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostAccountCacheCreateNewAWSResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostAccountCacheCreateNewAWSResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostAccountCacheCreateNewAWSResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostAccountCacheCreateNewAWSResponse201 | PostAccountCacheCreateNewAWSResponse400 | PostAccountCacheCreateNewAWSResponse401 | PostAccountCacheCreateNewAWSResponse403 | PostAccountCacheCreateNewAWSResponse422 | PostAccountCacheCreateNewAWSResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AWSAccountCacheNewAWSAccount,

) -> Response[PostAccountCacheCreateNewAWSResponse201 | PostAccountCacheCreateNewAWSResponse400 | PostAccountCacheCreateNewAWSResponse401 | PostAccountCacheCreateNewAWSResponse403 | PostAccountCacheCreateNewAWSResponse422 | PostAccountCacheCreateNewAWSResponse500]:
    """ Creates a new AWS Account via the Organizations API and adds it to the account cache in the
    application.

     The cached ID will be returned immediately.  The AWS account may take a few minutes to provision.
    You can poll
    GET /v3/account-cache/{id} looking for account_number to determine when the AWS Account is fully
    provisioned.

    Args:
        body (AWSAccountCacheNewAWSAccount): AWSAccountCacheNewAWSAccount defines a payload for
            creating a new AWS Account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAccountCacheCreateNewAWSResponse201 | PostAccountCacheCreateNewAWSResponse400 | PostAccountCacheCreateNewAWSResponse401 | PostAccountCacheCreateNewAWSResponse403 | PostAccountCacheCreateNewAWSResponse422 | PostAccountCacheCreateNewAWSResponse500]
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
    body: AWSAccountCacheNewAWSAccount,

) -> PostAccountCacheCreateNewAWSResponse201 | PostAccountCacheCreateNewAWSResponse400 | PostAccountCacheCreateNewAWSResponse401 | PostAccountCacheCreateNewAWSResponse403 | PostAccountCacheCreateNewAWSResponse422 | PostAccountCacheCreateNewAWSResponse500 | None:
    """ Creates a new AWS Account via the Organizations API and adds it to the account cache in the
    application.

     The cached ID will be returned immediately.  The AWS account may take a few minutes to provision.
    You can poll
    GET /v3/account-cache/{id} looking for account_number to determine when the AWS Account is fully
    provisioned.

    Args:
        body (AWSAccountCacheNewAWSAccount): AWSAccountCacheNewAWSAccount defines a payload for
            creating a new AWS Account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAccountCacheCreateNewAWSResponse201 | PostAccountCacheCreateNewAWSResponse400 | PostAccountCacheCreateNewAWSResponse401 | PostAccountCacheCreateNewAWSResponse403 | PostAccountCacheCreateNewAWSResponse422 | PostAccountCacheCreateNewAWSResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AWSAccountCacheNewAWSAccount,

) -> Response[PostAccountCacheCreateNewAWSResponse201 | PostAccountCacheCreateNewAWSResponse400 | PostAccountCacheCreateNewAWSResponse401 | PostAccountCacheCreateNewAWSResponse403 | PostAccountCacheCreateNewAWSResponse422 | PostAccountCacheCreateNewAWSResponse500]:
    """ Creates a new AWS Account via the Organizations API and adds it to the account cache in the
    application.

     The cached ID will be returned immediately.  The AWS account may take a few minutes to provision.
    You can poll
    GET /v3/account-cache/{id} looking for account_number to determine when the AWS Account is fully
    provisioned.

    Args:
        body (AWSAccountCacheNewAWSAccount): AWSAccountCacheNewAWSAccount defines a payload for
            creating a new AWS Account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAccountCacheCreateNewAWSResponse201 | PostAccountCacheCreateNewAWSResponse400 | PostAccountCacheCreateNewAWSResponse401 | PostAccountCacheCreateNewAWSResponse403 | PostAccountCacheCreateNewAWSResponse422 | PostAccountCacheCreateNewAWSResponse500]
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
    body: AWSAccountCacheNewAWSAccount,

) -> PostAccountCacheCreateNewAWSResponse201 | PostAccountCacheCreateNewAWSResponse400 | PostAccountCacheCreateNewAWSResponse401 | PostAccountCacheCreateNewAWSResponse403 | PostAccountCacheCreateNewAWSResponse422 | PostAccountCacheCreateNewAWSResponse500 | None:
    """ Creates a new AWS Account via the Organizations API and adds it to the account cache in the
    application.

     The cached ID will be returned immediately.  The AWS account may take a few minutes to provision.
    You can poll
    GET /v3/account-cache/{id} looking for account_number to determine when the AWS Account is fully
    provisioned.

    Args:
        body (AWSAccountCacheNewAWSAccount): AWSAccountCacheNewAWSAccount defines a payload for
            creating a new AWS Account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAccountCacheCreateNewAWSResponse201 | PostAccountCacheCreateNewAWSResponse400 | PostAccountCacheCreateNewAWSResponse401 | PostAccountCacheCreateNewAWSResponse403 | PostAccountCacheCreateNewAWSResponse422 | PostAccountCacheCreateNewAWSResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
