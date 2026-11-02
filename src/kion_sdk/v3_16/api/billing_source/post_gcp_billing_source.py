from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.gcp_billing_source import GCPBillingSource
from ...models.post_gcp_billing_source_response_201 import PostGCPBillingSourceResponse201
from ...models.post_gcp_billing_source_response_400 import PostGCPBillingSourceResponse400
from ...models.post_gcp_billing_source_response_401 import PostGCPBillingSourceResponse401
from ...models.post_gcp_billing_source_response_403 import PostGCPBillingSourceResponse403
from ...models.post_gcp_billing_source_response_422 import PostGCPBillingSourceResponse422
from ...models.post_gcp_billing_source_response_500 import PostGCPBillingSourceResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: GCPBillingSource,
    unique: bool | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["unique"] = unique


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/billing-source/gcp",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostGCPBillingSourceResponse201 | PostGCPBillingSourceResponse400 | PostGCPBillingSourceResponse401 | PostGCPBillingSourceResponse403 | PostGCPBillingSourceResponse422 | PostGCPBillingSourceResponse500 | None:
    if response.status_code == 201:
        response_201 = PostGCPBillingSourceResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostGCPBillingSourceResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostGCPBillingSourceResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostGCPBillingSourceResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostGCPBillingSourceResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostGCPBillingSourceResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostGCPBillingSourceResponse201 | PostGCPBillingSourceResponse400 | PostGCPBillingSourceResponse401 | PostGCPBillingSourceResponse403 | PostGCPBillingSourceResponse422 | PostGCPBillingSourceResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: GCPBillingSource,
    unique: bool | Unset = UNSET,

) -> Response[PostGCPBillingSourceResponse201 | PostGCPBillingSourceResponse400 | PostGCPBillingSourceResponse401 | PostGCPBillingSourceResponse403 | PostGCPBillingSourceResponse422 | PostGCPBillingSourceResponse500]:
    """ Creates a gcp billing source.

    Args:
        unique (bool | Unset):
        body (GCPBillingSource): GCPBillingSource defines a billing source used for testing and
            creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostGCPBillingSourceResponse201 | PostGCPBillingSourceResponse400 | PostGCPBillingSourceResponse401 | PostGCPBillingSourceResponse403 | PostGCPBillingSourceResponse422 | PostGCPBillingSourceResponse500]
     """


    kwargs = _get_kwargs(
        body=body,
unique=unique,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: GCPBillingSource,
    unique: bool | Unset = UNSET,

) -> PostGCPBillingSourceResponse201 | PostGCPBillingSourceResponse400 | PostGCPBillingSourceResponse401 | PostGCPBillingSourceResponse403 | PostGCPBillingSourceResponse422 | PostGCPBillingSourceResponse500 | None:
    """ Creates a gcp billing source.

    Args:
        unique (bool | Unset):
        body (GCPBillingSource): GCPBillingSource defines a billing source used for testing and
            creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostGCPBillingSourceResponse201 | PostGCPBillingSourceResponse400 | PostGCPBillingSourceResponse401 | PostGCPBillingSourceResponse403 | PostGCPBillingSourceResponse422 | PostGCPBillingSourceResponse500
     """


    return sync_detailed(
        client=client,
body=body,
unique=unique,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: GCPBillingSource,
    unique: bool | Unset = UNSET,

) -> Response[PostGCPBillingSourceResponse201 | PostGCPBillingSourceResponse400 | PostGCPBillingSourceResponse401 | PostGCPBillingSourceResponse403 | PostGCPBillingSourceResponse422 | PostGCPBillingSourceResponse500]:
    """ Creates a gcp billing source.

    Args:
        unique (bool | Unset):
        body (GCPBillingSource): GCPBillingSource defines a billing source used for testing and
            creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostGCPBillingSourceResponse201 | PostGCPBillingSourceResponse400 | PostGCPBillingSourceResponse401 | PostGCPBillingSourceResponse403 | PostGCPBillingSourceResponse422 | PostGCPBillingSourceResponse500]
     """


    kwargs = _get_kwargs(
        body=body,
unique=unique,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: GCPBillingSource,
    unique: bool | Unset = UNSET,

) -> PostGCPBillingSourceResponse201 | PostGCPBillingSourceResponse400 | PostGCPBillingSourceResponse401 | PostGCPBillingSourceResponse403 | PostGCPBillingSourceResponse422 | PostGCPBillingSourceResponse500 | None:
    """ Creates a gcp billing source.

    Args:
        unique (bool | Unset):
        body (GCPBillingSource): GCPBillingSource defines a billing source used for testing and
            creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostGCPBillingSourceResponse201 | PostGCPBillingSourceResponse400 | PostGCPBillingSourceResponse401 | PostGCPBillingSourceResponse403 | PostGCPBillingSourceResponse422 | PostGCPBillingSourceResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,
unique=unique,

    )).parsed
