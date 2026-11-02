from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.aws_billing_source_create import AWSBillingSourceCreate
from ...models.post_test_billing_source_response_200 import PostTestBillingSourceResponse200
from ...models.post_test_billing_source_response_401 import PostTestBillingSourceResponse401
from ...models.post_test_billing_source_response_422 import PostTestBillingSourceResponse422
from ...models.post_test_billing_source_response_500 import PostTestBillingSourceResponse500
from typing import cast



def _get_kwargs(
    *,
    body: AWSBillingSourceCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/billing-source/test",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostTestBillingSourceResponse200 | PostTestBillingSourceResponse401 | PostTestBillingSourceResponse422 | PostTestBillingSourceResponse500 | None:
    if response.status_code == 200:
        response_200 = PostTestBillingSourceResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = PostTestBillingSourceResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 422:
        response_422 = PostTestBillingSourceResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostTestBillingSourceResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostTestBillingSourceResponse200 | PostTestBillingSourceResponse401 | PostTestBillingSourceResponse422 | PostTestBillingSourceResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AWSBillingSourceCreate,

) -> Response[PostTestBillingSourceResponse200 | PostTestBillingSourceResponse401 | PostTestBillingSourceResponse422 | PostTestBillingSourceResponse500]:
    """ Tests a billing source.

    Args:
        body (AWSBillingSourceCreate): AWSBillingSourceCreate defines a billing source used for
            testing and creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostTestBillingSourceResponse200 | PostTestBillingSourceResponse401 | PostTestBillingSourceResponse422 | PostTestBillingSourceResponse500]
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
    body: AWSBillingSourceCreate,

) -> PostTestBillingSourceResponse200 | PostTestBillingSourceResponse401 | PostTestBillingSourceResponse422 | PostTestBillingSourceResponse500 | None:
    """ Tests a billing source.

    Args:
        body (AWSBillingSourceCreate): AWSBillingSourceCreate defines a billing source used for
            testing and creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostTestBillingSourceResponse200 | PostTestBillingSourceResponse401 | PostTestBillingSourceResponse422 | PostTestBillingSourceResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AWSBillingSourceCreate,

) -> Response[PostTestBillingSourceResponse200 | PostTestBillingSourceResponse401 | PostTestBillingSourceResponse422 | PostTestBillingSourceResponse500]:
    """ Tests a billing source.

    Args:
        body (AWSBillingSourceCreate): AWSBillingSourceCreate defines a billing source used for
            testing and creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostTestBillingSourceResponse200 | PostTestBillingSourceResponse401 | PostTestBillingSourceResponse422 | PostTestBillingSourceResponse500]
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
    body: AWSBillingSourceCreate,

) -> PostTestBillingSourceResponse200 | PostTestBillingSourceResponse401 | PostTestBillingSourceResponse422 | PostTestBillingSourceResponse500 | None:
    """ Tests a billing source.

    Args:
        body (AWSBillingSourceCreate): AWSBillingSourceCreate defines a billing source used for
            testing and creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostTestBillingSourceResponse200 | PostTestBillingSourceResponse401 | PostTestBillingSourceResponse422 | PostTestBillingSourceResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
