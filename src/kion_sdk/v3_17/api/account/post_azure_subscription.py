from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.azure_subscription_create import AzureSubscriptionCreate
from ...models.post_azure_subscription_response_201 import PostAzureSubscriptionResponse201
from ...models.post_azure_subscription_response_400 import PostAzureSubscriptionResponse400
from ...models.post_azure_subscription_response_401 import PostAzureSubscriptionResponse401
from ...models.post_azure_subscription_response_403 import PostAzureSubscriptionResponse403
from ...models.post_azure_subscription_response_422 import PostAzureSubscriptionResponse422
from ...models.post_azure_subscription_response_500 import PostAzureSubscriptionResponse500
from typing import cast



def _get_kwargs(
    *,
    body: AzureSubscriptionCreate,
    account_type: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["account-type"] = account_type


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/account/__qs__/account-type/azure",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostAzureSubscriptionResponse201 | PostAzureSubscriptionResponse400 | PostAzureSubscriptionResponse401 | PostAzureSubscriptionResponse403 | PostAzureSubscriptionResponse422 | PostAzureSubscriptionResponse500 | None:
    if response.status_code == 201:
        response_201 = PostAzureSubscriptionResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostAzureSubscriptionResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostAzureSubscriptionResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostAzureSubscriptionResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostAzureSubscriptionResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostAzureSubscriptionResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostAzureSubscriptionResponse201 | PostAzureSubscriptionResponse400 | PostAzureSubscriptionResponse401 | PostAzureSubscriptionResponse403 | PostAzureSubscriptionResponse422 | PostAzureSubscriptionResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AzureSubscriptionCreate,
    account_type: str,

) -> Response[PostAzureSubscriptionResponse201 | PostAzureSubscriptionResponse400 | PostAzureSubscriptionResponse401 | PostAzureSubscriptionResponse403 | PostAzureSubscriptionResponse422 | PostAzureSubscriptionResponse500]:
    """ Attaches an existing Azure Subscription to a project in the application.

    Args:
        account_type (str):
        body (AzureSubscriptionCreate): AzureSubscriptionCreate defines a payload for an Azure
            account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAzureSubscriptionResponse201 | PostAzureSubscriptionResponse400 | PostAzureSubscriptionResponse401 | PostAzureSubscriptionResponse403 | PostAzureSubscriptionResponse422 | PostAzureSubscriptionResponse500]
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
    body: AzureSubscriptionCreate,
    account_type: str,

) -> PostAzureSubscriptionResponse201 | PostAzureSubscriptionResponse400 | PostAzureSubscriptionResponse401 | PostAzureSubscriptionResponse403 | PostAzureSubscriptionResponse422 | PostAzureSubscriptionResponse500 | None:
    """ Attaches an existing Azure Subscription to a project in the application.

    Args:
        account_type (str):
        body (AzureSubscriptionCreate): AzureSubscriptionCreate defines a payload for an Azure
            account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAzureSubscriptionResponse201 | PostAzureSubscriptionResponse400 | PostAzureSubscriptionResponse401 | PostAzureSubscriptionResponse403 | PostAzureSubscriptionResponse422 | PostAzureSubscriptionResponse500
     """


    return sync_detailed(
        client=client,
body=body,
account_type=account_type,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AzureSubscriptionCreate,
    account_type: str,

) -> Response[PostAzureSubscriptionResponse201 | PostAzureSubscriptionResponse400 | PostAzureSubscriptionResponse401 | PostAzureSubscriptionResponse403 | PostAzureSubscriptionResponse422 | PostAzureSubscriptionResponse500]:
    """ Attaches an existing Azure Subscription to a project in the application.

    Args:
        account_type (str):
        body (AzureSubscriptionCreate): AzureSubscriptionCreate defines a payload for an Azure
            account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAzureSubscriptionResponse201 | PostAzureSubscriptionResponse400 | PostAzureSubscriptionResponse401 | PostAzureSubscriptionResponse403 | PostAzureSubscriptionResponse422 | PostAzureSubscriptionResponse500]
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
    body: AzureSubscriptionCreate,
    account_type: str,

) -> PostAzureSubscriptionResponse201 | PostAzureSubscriptionResponse400 | PostAzureSubscriptionResponse401 | PostAzureSubscriptionResponse403 | PostAzureSubscriptionResponse422 | PostAzureSubscriptionResponse500 | None:
    """ Attaches an existing Azure Subscription to a project in the application.

    Args:
        account_type (str):
        body (AzureSubscriptionCreate): AzureSubscriptionCreate defines a payload for an Azure
            account.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAzureSubscriptionResponse201 | PostAzureSubscriptionResponse400 | PostAzureSubscriptionResponse401 | PostAzureSubscriptionResponse403 | PostAzureSubscriptionResponse422 | PostAzureSubscriptionResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,
account_type=account_type,

    )).parsed
