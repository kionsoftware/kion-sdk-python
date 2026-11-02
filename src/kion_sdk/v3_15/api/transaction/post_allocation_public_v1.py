from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.allocation_create import AllocationCreate
from ...models.post_allocation_public_v1_response_201 import PostAllocationPublicV1Response201
from ...models.post_allocation_public_v1_response_400 import PostAllocationPublicV1Response400
from ...models.post_allocation_public_v1_response_401 import PostAllocationPublicV1Response401
from ...models.post_allocation_public_v1_response_403 import PostAllocationPublicV1Response403
from ...models.post_allocation_public_v1_response_422 import PostAllocationPublicV1Response422
from ...models.post_allocation_public_v1_response_500 import PostAllocationPublicV1Response500
from typing import cast



def _get_kwargs(
    *,
    body: AllocationCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/transaction/allocate",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostAllocationPublicV1Response201 | PostAllocationPublicV1Response400 | PostAllocationPublicV1Response401 | PostAllocationPublicV1Response403 | PostAllocationPublicV1Response422 | PostAllocationPublicV1Response500 | None:
    if response.status_code == 201:
        response_201 = PostAllocationPublicV1Response201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostAllocationPublicV1Response400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostAllocationPublicV1Response401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostAllocationPublicV1Response403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostAllocationPublicV1Response422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostAllocationPublicV1Response500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostAllocationPublicV1Response201 | PostAllocationPublicV1Response400 | PostAllocationPublicV1Response401 | PostAllocationPublicV1Response403 | PostAllocationPublicV1Response422 | PostAllocationPublicV1Response500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AllocationCreate,

) -> Response[PostAllocationPublicV1Response201 | PostAllocationPublicV1Response400 | PostAllocationPublicV1Response401 | PostAllocationPublicV1Response403 | PostAllocationPublicV1Response422 | PostAllocationPublicV1Response500]:
    """ Creates an allocation of funds from a funding source from one OU in the application to another.

    Args:
        body (AllocationCreate): AllocationCreate defines the creation of an allocation of funds
            from one OU to another.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAllocationPublicV1Response201 | PostAllocationPublicV1Response400 | PostAllocationPublicV1Response401 | PostAllocationPublicV1Response403 | PostAllocationPublicV1Response422 | PostAllocationPublicV1Response500]
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
    body: AllocationCreate,

) -> PostAllocationPublicV1Response201 | PostAllocationPublicV1Response400 | PostAllocationPublicV1Response401 | PostAllocationPublicV1Response403 | PostAllocationPublicV1Response422 | PostAllocationPublicV1Response500 | None:
    """ Creates an allocation of funds from a funding source from one OU in the application to another.

    Args:
        body (AllocationCreate): AllocationCreate defines the creation of an allocation of funds
            from one OU to another.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAllocationPublicV1Response201 | PostAllocationPublicV1Response400 | PostAllocationPublicV1Response401 | PostAllocationPublicV1Response403 | PostAllocationPublicV1Response422 | PostAllocationPublicV1Response500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AllocationCreate,

) -> Response[PostAllocationPublicV1Response201 | PostAllocationPublicV1Response400 | PostAllocationPublicV1Response401 | PostAllocationPublicV1Response403 | PostAllocationPublicV1Response422 | PostAllocationPublicV1Response500]:
    """ Creates an allocation of funds from a funding source from one OU in the application to another.

    Args:
        body (AllocationCreate): AllocationCreate defines the creation of an allocation of funds
            from one OU to another.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAllocationPublicV1Response201 | PostAllocationPublicV1Response400 | PostAllocationPublicV1Response401 | PostAllocationPublicV1Response403 | PostAllocationPublicV1Response422 | PostAllocationPublicV1Response500]
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
    body: AllocationCreate,

) -> PostAllocationPublicV1Response201 | PostAllocationPublicV1Response400 | PostAllocationPublicV1Response401 | PostAllocationPublicV1Response403 | PostAllocationPublicV1Response422 | PostAllocationPublicV1Response500 | None:
    """ Creates an allocation of funds from a funding source from one OU in the application to another.

    Args:
        body (AllocationCreate): AllocationCreate defines the creation of an allocation of funds
            from one OU to another.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAllocationPublicV1Response201 | PostAllocationPublicV1Response400 | PostAllocationPublicV1Response401 | PostAllocationPublicV1Response403 | PostAllocationPublicV1Response422 | PostAllocationPublicV1Response500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
