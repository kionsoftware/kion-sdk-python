from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.custom_billing_source_test_request import CustomBillingSourceTestRequest
from ...models.post_test_custom_billing_source_response_200 import PostTestCustomBillingSourceResponse200
from ...models.post_test_custom_billing_source_response_400 import PostTestCustomBillingSourceResponse400
from ...models.post_test_custom_billing_source_response_401 import PostTestCustomBillingSourceResponse401
from ...models.post_test_custom_billing_source_response_422 import PostTestCustomBillingSourceResponse422
from ...models.post_test_custom_billing_source_response_500 import PostTestCustomBillingSourceResponse500
from typing import cast



def _get_kwargs(
    *,
    body: CustomBillingSourceTestRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/billing-source/test-custom",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostTestCustomBillingSourceResponse200 | PostTestCustomBillingSourceResponse400 | PostTestCustomBillingSourceResponse401 | PostTestCustomBillingSourceResponse422 | PostTestCustomBillingSourceResponse500 | None:
    if response.status_code == 200:
        response_200 = PostTestCustomBillingSourceResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PostTestCustomBillingSourceResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostTestCustomBillingSourceResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 422:
        response_422 = PostTestCustomBillingSourceResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostTestCustomBillingSourceResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostTestCustomBillingSourceResponse200 | PostTestCustomBillingSourceResponse400 | PostTestCustomBillingSourceResponse401 | PostTestCustomBillingSourceResponse422 | PostTestCustomBillingSourceResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CustomBillingSourceTestRequest,

) -> Response[PostTestCustomBillingSourceResponse200 | PostTestCustomBillingSourceResponse400 | PostTestCustomBillingSourceResponse401 | PostTestCustomBillingSourceResponse422 | PostTestCustomBillingSourceResponse500]:
    """ Tests a custom billing source.

    Args:
        body (CustomBillingSourceTestRequest): CustomBillingSourceTestRequest defines a request to
            test a custom billing source.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostTestCustomBillingSourceResponse200 | PostTestCustomBillingSourceResponse400 | PostTestCustomBillingSourceResponse401 | PostTestCustomBillingSourceResponse422 | PostTestCustomBillingSourceResponse500]
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
    body: CustomBillingSourceTestRequest,

) -> PostTestCustomBillingSourceResponse200 | PostTestCustomBillingSourceResponse400 | PostTestCustomBillingSourceResponse401 | PostTestCustomBillingSourceResponse422 | PostTestCustomBillingSourceResponse500 | None:
    """ Tests a custom billing source.

    Args:
        body (CustomBillingSourceTestRequest): CustomBillingSourceTestRequest defines a request to
            test a custom billing source.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostTestCustomBillingSourceResponse200 | PostTestCustomBillingSourceResponse400 | PostTestCustomBillingSourceResponse401 | PostTestCustomBillingSourceResponse422 | PostTestCustomBillingSourceResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CustomBillingSourceTestRequest,

) -> Response[PostTestCustomBillingSourceResponse200 | PostTestCustomBillingSourceResponse400 | PostTestCustomBillingSourceResponse401 | PostTestCustomBillingSourceResponse422 | PostTestCustomBillingSourceResponse500]:
    """ Tests a custom billing source.

    Args:
        body (CustomBillingSourceTestRequest): CustomBillingSourceTestRequest defines a request to
            test a custom billing source.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostTestCustomBillingSourceResponse200 | PostTestCustomBillingSourceResponse400 | PostTestCustomBillingSourceResponse401 | PostTestCustomBillingSourceResponse422 | PostTestCustomBillingSourceResponse500]
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
    body: CustomBillingSourceTestRequest,

) -> PostTestCustomBillingSourceResponse200 | PostTestCustomBillingSourceResponse400 | PostTestCustomBillingSourceResponse401 | PostTestCustomBillingSourceResponse422 | PostTestCustomBillingSourceResponse500 | None:
    """ Tests a custom billing source.

    Args:
        body (CustomBillingSourceTestRequest): CustomBillingSourceTestRequest defines a request to
            test a custom billing source.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostTestCustomBillingSourceResponse200 | PostTestCustomBillingSourceResponse400 | PostTestCustomBillingSourceResponse401 | PostTestCustomBillingSourceResponse422 | PostTestCustomBillingSourceResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
