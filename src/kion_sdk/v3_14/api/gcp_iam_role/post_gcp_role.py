from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.gcp_role_create import GCPRoleCreate
from ...models.post_gcp_role_response_201 import PostGCPRoleResponse201
from ...models.post_gcp_role_response_400 import PostGCPRoleResponse400
from ...models.post_gcp_role_response_401 import PostGCPRoleResponse401
from ...models.post_gcp_role_response_403 import PostGCPRoleResponse403
from ...models.post_gcp_role_response_409 import PostGCPRoleResponse409
from ...models.post_gcp_role_response_422 import PostGCPRoleResponse422
from ...models.post_gcp_role_response_500 import PostGCPRoleResponse500
from typing import cast



def _get_kwargs(
    *,
    body: GCPRoleCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/gcp-iam-role",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostGCPRoleResponse201 | PostGCPRoleResponse400 | PostGCPRoleResponse401 | PostGCPRoleResponse403 | PostGCPRoleResponse409 | PostGCPRoleResponse422 | PostGCPRoleResponse500 | None:
    if response.status_code == 201:
        response_201 = PostGCPRoleResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostGCPRoleResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostGCPRoleResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostGCPRoleResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 409:
        response_409 = PostGCPRoleResponse409.from_dict(response.json())



        return response_409

    if response.status_code == 422:
        response_422 = PostGCPRoleResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostGCPRoleResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostGCPRoleResponse201 | PostGCPRoleResponse400 | PostGCPRoleResponse401 | PostGCPRoleResponse403 | PostGCPRoleResponse409 | PostGCPRoleResponse422 | PostGCPRoleResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: GCPRoleCreate,

) -> Response[PostGCPRoleResponse201 | PostGCPRoleResponse400 | PostGCPRoleResponse401 | PostGCPRoleResponse403 | PostGCPRoleResponse409 | PostGCPRoleResponse422 | PostGCPRoleResponse500]:
    """ Creates a GCP IAM Role in the application.

    Args:
        body (GCPRoleCreate): GCPRoleCreate defines an GCP Role creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostGCPRoleResponse201 | PostGCPRoleResponse400 | PostGCPRoleResponse401 | PostGCPRoleResponse403 | PostGCPRoleResponse409 | PostGCPRoleResponse422 | PostGCPRoleResponse500]
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
    body: GCPRoleCreate,

) -> PostGCPRoleResponse201 | PostGCPRoleResponse400 | PostGCPRoleResponse401 | PostGCPRoleResponse403 | PostGCPRoleResponse409 | PostGCPRoleResponse422 | PostGCPRoleResponse500 | None:
    """ Creates a GCP IAM Role in the application.

    Args:
        body (GCPRoleCreate): GCPRoleCreate defines an GCP Role creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostGCPRoleResponse201 | PostGCPRoleResponse400 | PostGCPRoleResponse401 | PostGCPRoleResponse403 | PostGCPRoleResponse409 | PostGCPRoleResponse422 | PostGCPRoleResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: GCPRoleCreate,

) -> Response[PostGCPRoleResponse201 | PostGCPRoleResponse400 | PostGCPRoleResponse401 | PostGCPRoleResponse403 | PostGCPRoleResponse409 | PostGCPRoleResponse422 | PostGCPRoleResponse500]:
    """ Creates a GCP IAM Role in the application.

    Args:
        body (GCPRoleCreate): GCPRoleCreate defines an GCP Role creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostGCPRoleResponse201 | PostGCPRoleResponse400 | PostGCPRoleResponse401 | PostGCPRoleResponse403 | PostGCPRoleResponse409 | PostGCPRoleResponse422 | PostGCPRoleResponse500]
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
    body: GCPRoleCreate,

) -> PostGCPRoleResponse201 | PostGCPRoleResponse400 | PostGCPRoleResponse401 | PostGCPRoleResponse403 | PostGCPRoleResponse409 | PostGCPRoleResponse422 | PostGCPRoleResponse500 | None:
    """ Creates a GCP IAM Role in the application.

    Args:
        body (GCPRoleCreate): GCPRoleCreate defines an GCP Role creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostGCPRoleResponse201 | PostGCPRoleResponse400 | PostGCPRoleResponse401 | PostGCPRoleResponse403 | PostGCPRoleResponse409 | PostGCPRoleResponse422 | PostGCPRoleResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
