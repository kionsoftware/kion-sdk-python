from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.azure_account_linkage_create import AzureAccountLinkageCreate
from ...models.post_account_linkage_response_201 import PostAccountLinkageResponse201
from ...models.post_account_linkage_response_400 import PostAccountLinkageResponse400
from ...models.post_account_linkage_response_401 import PostAccountLinkageResponse401
from ...models.post_account_linkage_response_422 import PostAccountLinkageResponse422
from ...models.post_account_linkage_response_500 import PostAccountLinkageResponse500
from typing import cast



def _get_kwargs(
    *,
    body: AzureAccountLinkageCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/account-linkages",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostAccountLinkageResponse201 | PostAccountLinkageResponse400 | PostAccountLinkageResponse401 | PostAccountLinkageResponse422 | PostAccountLinkageResponse500 | None:
    if response.status_code == 201:
        response_201 = PostAccountLinkageResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostAccountLinkageResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostAccountLinkageResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 422:
        response_422 = PostAccountLinkageResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostAccountLinkageResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostAccountLinkageResponse201 | PostAccountLinkageResponse400 | PostAccountLinkageResponse401 | PostAccountLinkageResponse422 | PostAccountLinkageResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AzureAccountLinkageCreate,

) -> Response[PostAccountLinkageResponse201 | PostAccountLinkageResponse400 | PostAccountLinkageResponse401 | PostAccountLinkageResponse422 | PostAccountLinkageResponse500]:
    """ Creates an Azure Account Linkage for the specified user.

    Args:
        body (AzureAccountLinkageCreate): AzureAccountLinkageCreate is the request body for
            creating an Azure Account Linkage.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAccountLinkageResponse201 | PostAccountLinkageResponse400 | PostAccountLinkageResponse401 | PostAccountLinkageResponse422 | PostAccountLinkageResponse500]
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
    body: AzureAccountLinkageCreate,

) -> PostAccountLinkageResponse201 | PostAccountLinkageResponse400 | PostAccountLinkageResponse401 | PostAccountLinkageResponse422 | PostAccountLinkageResponse500 | None:
    """ Creates an Azure Account Linkage for the specified user.

    Args:
        body (AzureAccountLinkageCreate): AzureAccountLinkageCreate is the request body for
            creating an Azure Account Linkage.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAccountLinkageResponse201 | PostAccountLinkageResponse400 | PostAccountLinkageResponse401 | PostAccountLinkageResponse422 | PostAccountLinkageResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AzureAccountLinkageCreate,

) -> Response[PostAccountLinkageResponse201 | PostAccountLinkageResponse400 | PostAccountLinkageResponse401 | PostAccountLinkageResponse422 | PostAccountLinkageResponse500]:
    """ Creates an Azure Account Linkage for the specified user.

    Args:
        body (AzureAccountLinkageCreate): AzureAccountLinkageCreate is the request body for
            creating an Azure Account Linkage.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAccountLinkageResponse201 | PostAccountLinkageResponse400 | PostAccountLinkageResponse401 | PostAccountLinkageResponse422 | PostAccountLinkageResponse500]
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
    body: AzureAccountLinkageCreate,

) -> PostAccountLinkageResponse201 | PostAccountLinkageResponse400 | PostAccountLinkageResponse401 | PostAccountLinkageResponse422 | PostAccountLinkageResponse500 | None:
    """ Creates an Azure Account Linkage for the specified user.

    Args:
        body (AzureAccountLinkageCreate): AzureAccountLinkageCreate is the request body for
            creating an Azure Account Linkage.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAccountLinkageResponse201 | PostAccountLinkageResponse400 | PostAccountLinkageResponse401 | PostAccountLinkageResponse422 | PostAccountLinkageResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
