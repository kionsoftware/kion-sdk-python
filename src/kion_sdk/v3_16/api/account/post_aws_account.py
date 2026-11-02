from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.aws_account_create import AWSAccountCreate
from ...models.post_aws_account_response_201 import PostAwsAccountResponse201
from ...models.post_aws_account_response_400 import PostAwsAccountResponse400
from ...models.post_aws_account_response_401 import PostAwsAccountResponse401
from ...models.post_aws_account_response_403 import PostAwsAccountResponse403
from ...models.post_aws_account_response_422 import PostAwsAccountResponse422
from ...models.post_aws_account_response_500 import PostAwsAccountResponse500
from typing import cast



def _get_kwargs(
    *,
    body: AWSAccountCreate,
    account_type: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["account-type"] = account_type


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/account/__qs__/account-type/aws",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostAwsAccountResponse201 | PostAwsAccountResponse400 | PostAwsAccountResponse401 | PostAwsAccountResponse403 | PostAwsAccountResponse422 | PostAwsAccountResponse500 | None:
    if response.status_code == 201:
        response_201 = PostAwsAccountResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostAwsAccountResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostAwsAccountResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostAwsAccountResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostAwsAccountResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostAwsAccountResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostAwsAccountResponse201 | PostAwsAccountResponse400 | PostAwsAccountResponse401 | PostAwsAccountResponse403 | PostAwsAccountResponse422 | PostAwsAccountResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AWSAccountCreate,
    account_type: str,

) -> Response[PostAwsAccountResponse201 | PostAwsAccountResponse400 | PostAwsAccountResponse401 | PostAwsAccountResponse403 | PostAwsAccountResponse422 | PostAwsAccountResponse500]:
    """ Attaches an existing AWS Account to a project in the application.

    Args:
        account_type (str):
        body (AWSAccountCreate): AWSAccountCreate defines an AWS account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAwsAccountResponse201 | PostAwsAccountResponse400 | PostAwsAccountResponse401 | PostAwsAccountResponse403 | PostAwsAccountResponse422 | PostAwsAccountResponse500]
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
    body: AWSAccountCreate,
    account_type: str,

) -> PostAwsAccountResponse201 | PostAwsAccountResponse400 | PostAwsAccountResponse401 | PostAwsAccountResponse403 | PostAwsAccountResponse422 | PostAwsAccountResponse500 | None:
    """ Attaches an existing AWS Account to a project in the application.

    Args:
        account_type (str):
        body (AWSAccountCreate): AWSAccountCreate defines an AWS account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAwsAccountResponse201 | PostAwsAccountResponse400 | PostAwsAccountResponse401 | PostAwsAccountResponse403 | PostAwsAccountResponse422 | PostAwsAccountResponse500
     """


    return sync_detailed(
        client=client,
body=body,
account_type=account_type,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AWSAccountCreate,
    account_type: str,

) -> Response[PostAwsAccountResponse201 | PostAwsAccountResponse400 | PostAwsAccountResponse401 | PostAwsAccountResponse403 | PostAwsAccountResponse422 | PostAwsAccountResponse500]:
    """ Attaches an existing AWS Account to a project in the application.

    Args:
        account_type (str):
        body (AWSAccountCreate): AWSAccountCreate defines an AWS account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAwsAccountResponse201 | PostAwsAccountResponse400 | PostAwsAccountResponse401 | PostAwsAccountResponse403 | PostAwsAccountResponse422 | PostAwsAccountResponse500]
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
    body: AWSAccountCreate,
    account_type: str,

) -> PostAwsAccountResponse201 | PostAwsAccountResponse400 | PostAwsAccountResponse401 | PostAwsAccountResponse403 | PostAwsAccountResponse422 | PostAwsAccountResponse500 | None:
    """ Attaches an existing AWS Account to a project in the application.

    Args:
        account_type (str):
        body (AWSAccountCreate): AWSAccountCreate defines an AWS account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAwsAccountResponse201 | PostAwsAccountResponse400 | PostAwsAccountResponse401 | PostAwsAccountResponse403 | PostAwsAccountResponse422 | PostAwsAccountResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,
account_type=account_type,

    )).parsed
