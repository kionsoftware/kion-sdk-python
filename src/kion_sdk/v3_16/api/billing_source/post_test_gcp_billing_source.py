from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.gcp_billing_source_create import GCPBillingSourceCreate
from ...models.post_test_gcp_billing_source_response_200 import PostTestGCPBillingSourceResponse200
from ...models.post_test_gcp_billing_source_response_400 import PostTestGCPBillingSourceResponse400
from ...models.post_test_gcp_billing_source_response_401 import PostTestGCPBillingSourceResponse401
from ...models.post_test_gcp_billing_source_response_422 import PostTestGCPBillingSourceResponse422
from ...models.post_test_gcp_billing_source_response_500 import PostTestGCPBillingSourceResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: GCPBillingSourceCreate,
    unique: bool | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["unique"] = unique


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/billing-source/test-gcp",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostTestGCPBillingSourceResponse200 | PostTestGCPBillingSourceResponse400 | PostTestGCPBillingSourceResponse401 | PostTestGCPBillingSourceResponse422 | PostTestGCPBillingSourceResponse500 | None:
    if response.status_code == 200:
        response_200 = PostTestGCPBillingSourceResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PostTestGCPBillingSourceResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostTestGCPBillingSourceResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 422:
        response_422 = PostTestGCPBillingSourceResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostTestGCPBillingSourceResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostTestGCPBillingSourceResponse200 | PostTestGCPBillingSourceResponse400 | PostTestGCPBillingSourceResponse401 | PostTestGCPBillingSourceResponse422 | PostTestGCPBillingSourceResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: GCPBillingSourceCreate,
    unique: bool | Unset = UNSET,

) -> Response[PostTestGCPBillingSourceResponse200 | PostTestGCPBillingSourceResponse400 | PostTestGCPBillingSourceResponse401 | PostTestGCPBillingSourceResponse422 | PostTestGCPBillingSourceResponse500]:
    """ Tests a gcp billing source.

    Args:
        unique (bool | Unset):
        body (GCPBillingSourceCreate): GCPBillingSourceCreate defines a billing source used for
            testing and creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostTestGCPBillingSourceResponse200 | PostTestGCPBillingSourceResponse400 | PostTestGCPBillingSourceResponse401 | PostTestGCPBillingSourceResponse422 | PostTestGCPBillingSourceResponse500]
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
    body: GCPBillingSourceCreate,
    unique: bool | Unset = UNSET,

) -> PostTestGCPBillingSourceResponse200 | PostTestGCPBillingSourceResponse400 | PostTestGCPBillingSourceResponse401 | PostTestGCPBillingSourceResponse422 | PostTestGCPBillingSourceResponse500 | None:
    """ Tests a gcp billing source.

    Args:
        unique (bool | Unset):
        body (GCPBillingSourceCreate): GCPBillingSourceCreate defines a billing source used for
            testing and creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostTestGCPBillingSourceResponse200 | PostTestGCPBillingSourceResponse400 | PostTestGCPBillingSourceResponse401 | PostTestGCPBillingSourceResponse422 | PostTestGCPBillingSourceResponse500
     """


    return sync_detailed(
        client=client,
body=body,
unique=unique,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: GCPBillingSourceCreate,
    unique: bool | Unset = UNSET,

) -> Response[PostTestGCPBillingSourceResponse200 | PostTestGCPBillingSourceResponse400 | PostTestGCPBillingSourceResponse401 | PostTestGCPBillingSourceResponse422 | PostTestGCPBillingSourceResponse500]:
    """ Tests a gcp billing source.

    Args:
        unique (bool | Unset):
        body (GCPBillingSourceCreate): GCPBillingSourceCreate defines a billing source used for
            testing and creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostTestGCPBillingSourceResponse200 | PostTestGCPBillingSourceResponse400 | PostTestGCPBillingSourceResponse401 | PostTestGCPBillingSourceResponse422 | PostTestGCPBillingSourceResponse500]
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
    body: GCPBillingSourceCreate,
    unique: bool | Unset = UNSET,

) -> PostTestGCPBillingSourceResponse200 | PostTestGCPBillingSourceResponse400 | PostTestGCPBillingSourceResponse401 | PostTestGCPBillingSourceResponse422 | PostTestGCPBillingSourceResponse500 | None:
    """ Tests a gcp billing source.

    Args:
        unique (bool | Unset):
        body (GCPBillingSourceCreate): GCPBillingSourceCreate defines a billing source used for
            testing and creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostTestGCPBillingSourceResponse200 | PostTestGCPBillingSourceResponse400 | PostTestGCPBillingSourceResponse401 | PostTestGCPBillingSourceResponse422 | PostTestGCPBillingSourceResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,
unique=unique,

    )).parsed
