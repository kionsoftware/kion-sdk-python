from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.oci_billing_source_create_with_validation import OCIBillingSourceCreateWithValidation
from ...models.post_oci_billing_source_response_201 import PostOCIBillingSourceResponse201
from ...models.post_oci_billing_source_response_400 import PostOCIBillingSourceResponse400
from ...models.post_oci_billing_source_response_401 import PostOCIBillingSourceResponse401
from ...models.post_oci_billing_source_response_403 import PostOCIBillingSourceResponse403
from ...models.post_oci_billing_source_response_409 import PostOCIBillingSourceResponse409
from ...models.post_oci_billing_source_response_422 import PostOCIBillingSourceResponse422
from ...models.post_oci_billing_source_response_500 import PostOCIBillingSourceResponse500
from typing import cast



def _get_kwargs(
    *,
    body: OCIBillingSourceCreateWithValidation,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/billing-source/oci",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostOCIBillingSourceResponse201 | PostOCIBillingSourceResponse400 | PostOCIBillingSourceResponse401 | PostOCIBillingSourceResponse403 | PostOCIBillingSourceResponse409 | PostOCIBillingSourceResponse422 | PostOCIBillingSourceResponse500 | None:
    if response.status_code == 201:
        response_201 = PostOCIBillingSourceResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostOCIBillingSourceResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostOCIBillingSourceResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostOCIBillingSourceResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 409:
        response_409 = PostOCIBillingSourceResponse409.from_dict(response.json())



        return response_409

    if response.status_code == 422:
        response_422 = PostOCIBillingSourceResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostOCIBillingSourceResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostOCIBillingSourceResponse201 | PostOCIBillingSourceResponse400 | PostOCIBillingSourceResponse401 | PostOCIBillingSourceResponse403 | PostOCIBillingSourceResponse409 | PostOCIBillingSourceResponse422 | PostOCIBillingSourceResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: OCIBillingSourceCreateWithValidation,

) -> Response[PostOCIBillingSourceResponse201 | PostOCIBillingSourceResponse400 | PostOCIBillingSourceResponse401 | PostOCIBillingSourceResponse403 | PostOCIBillingSourceResponse409 | PostOCIBillingSourceResponse422 | PostOCIBillingSourceResponse500]:
    """ Creates a new OCI billing source.

    Args:
        body (OCIBillingSourceCreateWithValidation): OCIBillingSourceCreateWithValidation defines
            a billing source used for testing and creation with validation

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostOCIBillingSourceResponse201 | PostOCIBillingSourceResponse400 | PostOCIBillingSourceResponse401 | PostOCIBillingSourceResponse403 | PostOCIBillingSourceResponse409 | PostOCIBillingSourceResponse422 | PostOCIBillingSourceResponse500]
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
    body: OCIBillingSourceCreateWithValidation,

) -> PostOCIBillingSourceResponse201 | PostOCIBillingSourceResponse400 | PostOCIBillingSourceResponse401 | PostOCIBillingSourceResponse403 | PostOCIBillingSourceResponse409 | PostOCIBillingSourceResponse422 | PostOCIBillingSourceResponse500 | None:
    """ Creates a new OCI billing source.

    Args:
        body (OCIBillingSourceCreateWithValidation): OCIBillingSourceCreateWithValidation defines
            a billing source used for testing and creation with validation

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostOCIBillingSourceResponse201 | PostOCIBillingSourceResponse400 | PostOCIBillingSourceResponse401 | PostOCIBillingSourceResponse403 | PostOCIBillingSourceResponse409 | PostOCIBillingSourceResponse422 | PostOCIBillingSourceResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: OCIBillingSourceCreateWithValidation,

) -> Response[PostOCIBillingSourceResponse201 | PostOCIBillingSourceResponse400 | PostOCIBillingSourceResponse401 | PostOCIBillingSourceResponse403 | PostOCIBillingSourceResponse409 | PostOCIBillingSourceResponse422 | PostOCIBillingSourceResponse500]:
    """ Creates a new OCI billing source.

    Args:
        body (OCIBillingSourceCreateWithValidation): OCIBillingSourceCreateWithValidation defines
            a billing source used for testing and creation with validation

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostOCIBillingSourceResponse201 | PostOCIBillingSourceResponse400 | PostOCIBillingSourceResponse401 | PostOCIBillingSourceResponse403 | PostOCIBillingSourceResponse409 | PostOCIBillingSourceResponse422 | PostOCIBillingSourceResponse500]
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
    body: OCIBillingSourceCreateWithValidation,

) -> PostOCIBillingSourceResponse201 | PostOCIBillingSourceResponse400 | PostOCIBillingSourceResponse401 | PostOCIBillingSourceResponse403 | PostOCIBillingSourceResponse409 | PostOCIBillingSourceResponse422 | PostOCIBillingSourceResponse500 | None:
    """ Creates a new OCI billing source.

    Args:
        body (OCIBillingSourceCreateWithValidation): OCIBillingSourceCreateWithValidation defines
            a billing source used for testing and creation with validation

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostOCIBillingSourceResponse201 | PostOCIBillingSourceResponse400 | PostOCIBillingSourceResponse401 | PostOCIBillingSourceResponse403 | PostOCIBillingSourceResponse409 | PostOCIBillingSourceResponse422 | PostOCIBillingSourceResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
