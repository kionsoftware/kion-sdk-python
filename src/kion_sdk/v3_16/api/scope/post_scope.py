from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_scope_response_201 import PostScopeResponse201
from ...models.post_scope_response_400 import PostScopeResponse400
from ...models.post_scope_response_401 import PostScopeResponse401
from ...models.post_scope_response_403 import PostScopeResponse403
from ...models.post_scope_response_404 import PostScopeResponse404
from ...models.post_scope_response_422 import PostScopeResponse422
from ...models.post_scope_response_500 import PostScopeResponse500
from ...models.scope_create import ScopeCreate
from typing import cast



def _get_kwargs(
    *,
    body: ScopeCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/beta/scope",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostScopeResponse201 | PostScopeResponse400 | PostScopeResponse401 | PostScopeResponse403 | PostScopeResponse404 | PostScopeResponse422 | PostScopeResponse500 | None:
    if response.status_code == 201:
        response_201 = PostScopeResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostScopeResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostScopeResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostScopeResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PostScopeResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PostScopeResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostScopeResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostScopeResponse201 | PostScopeResponse400 | PostScopeResponse401 | PostScopeResponse403 | PostScopeResponse404 | PostScopeResponse422 | PostScopeResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ScopeCreate,

) -> Response[PostScopeResponse201 | PostScopeResponse400 | PostScopeResponse401 | PostScopeResponse403 | PostScopeResponse404 | PostScopeResponse422 | PostScopeResponse500]:
    """ Creates a new scope in the system.

    Args:
        body (ScopeCreate): AppRoleCreate defines a Scope creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostScopeResponse201 | PostScopeResponse400 | PostScopeResponse401 | PostScopeResponse403 | PostScopeResponse404 | PostScopeResponse422 | PostScopeResponse500]
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
    body: ScopeCreate,

) -> PostScopeResponse201 | PostScopeResponse400 | PostScopeResponse401 | PostScopeResponse403 | PostScopeResponse404 | PostScopeResponse422 | PostScopeResponse500 | None:
    """ Creates a new scope in the system.

    Args:
        body (ScopeCreate): AppRoleCreate defines a Scope creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostScopeResponse201 | PostScopeResponse400 | PostScopeResponse401 | PostScopeResponse403 | PostScopeResponse404 | PostScopeResponse422 | PostScopeResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ScopeCreate,

) -> Response[PostScopeResponse201 | PostScopeResponse400 | PostScopeResponse401 | PostScopeResponse403 | PostScopeResponse404 | PostScopeResponse422 | PostScopeResponse500]:
    """ Creates a new scope in the system.

    Args:
        body (ScopeCreate): AppRoleCreate defines a Scope creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostScopeResponse201 | PostScopeResponse400 | PostScopeResponse401 | PostScopeResponse403 | PostScopeResponse404 | PostScopeResponse422 | PostScopeResponse500]
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
    body: ScopeCreate,

) -> PostScopeResponse201 | PostScopeResponse400 | PostScopeResponse401 | PostScopeResponse403 | PostScopeResponse404 | PostScopeResponse422 | PostScopeResponse500 | None:
    """ Creates a new scope in the system.

    Args:
        body (ScopeCreate): AppRoleCreate defines a Scope creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostScopeResponse201 | PostScopeResponse400 | PostScopeResponse401 | PostScopeResponse403 | PostScopeResponse404 | PostScopeResponse422 | PostScopeResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
