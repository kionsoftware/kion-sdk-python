from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.permission_scheme_create import PermissionSchemeCreate
from ...models.post_permission_scheme_response_201 import PostPermissionSchemeResponse201
from ...models.post_permission_scheme_response_400 import PostPermissionSchemeResponse400
from ...models.post_permission_scheme_response_401 import PostPermissionSchemeResponse401
from ...models.post_permission_scheme_response_403 import PostPermissionSchemeResponse403
from ...models.post_permission_scheme_response_422 import PostPermissionSchemeResponse422
from ...models.post_permission_scheme_response_500 import PostPermissionSchemeResponse500
from typing import cast



def _get_kwargs(
    *,
    body: PermissionSchemeCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/permission-scheme",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostPermissionSchemeResponse201 | PostPermissionSchemeResponse400 | PostPermissionSchemeResponse401 | PostPermissionSchemeResponse403 | PostPermissionSchemeResponse422 | PostPermissionSchemeResponse500 | None:
    if response.status_code == 201:
        response_201 = PostPermissionSchemeResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostPermissionSchemeResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostPermissionSchemeResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostPermissionSchemeResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostPermissionSchemeResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostPermissionSchemeResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostPermissionSchemeResponse201 | PostPermissionSchemeResponse400 | PostPermissionSchemeResponse401 | PostPermissionSchemeResponse403 | PostPermissionSchemeResponse422 | PostPermissionSchemeResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PermissionSchemeCreate,

) -> Response[PostPermissionSchemeResponse201 | PostPermissionSchemeResponse400 | PostPermissionSchemeResponse401 | PostPermissionSchemeResponse403 | PostPermissionSchemeResponse422 | PostPermissionSchemeResponse500]:
    """ Creates a permission scheme in the application.

    Args:
        body (PermissionSchemeCreate): PermissionSchemeCreate defines a permission scheme
            creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostPermissionSchemeResponse201 | PostPermissionSchemeResponse400 | PostPermissionSchemeResponse401 | PostPermissionSchemeResponse403 | PostPermissionSchemeResponse422 | PostPermissionSchemeResponse500]
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
    body: PermissionSchemeCreate,

) -> PostPermissionSchemeResponse201 | PostPermissionSchemeResponse400 | PostPermissionSchemeResponse401 | PostPermissionSchemeResponse403 | PostPermissionSchemeResponse422 | PostPermissionSchemeResponse500 | None:
    """ Creates a permission scheme in the application.

    Args:
        body (PermissionSchemeCreate): PermissionSchemeCreate defines a permission scheme
            creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostPermissionSchemeResponse201 | PostPermissionSchemeResponse400 | PostPermissionSchemeResponse401 | PostPermissionSchemeResponse403 | PostPermissionSchemeResponse422 | PostPermissionSchemeResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PermissionSchemeCreate,

) -> Response[PostPermissionSchemeResponse201 | PostPermissionSchemeResponse400 | PostPermissionSchemeResponse401 | PostPermissionSchemeResponse403 | PostPermissionSchemeResponse422 | PostPermissionSchemeResponse500]:
    """ Creates a permission scheme in the application.

    Args:
        body (PermissionSchemeCreate): PermissionSchemeCreate defines a permission scheme
            creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostPermissionSchemeResponse201 | PostPermissionSchemeResponse400 | PostPermissionSchemeResponse401 | PostPermissionSchemeResponse403 | PostPermissionSchemeResponse422 | PostPermissionSchemeResponse500]
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
    body: PermissionSchemeCreate,

) -> PostPermissionSchemeResponse201 | PostPermissionSchemeResponse400 | PostPermissionSchemeResponse401 | PostPermissionSchemeResponse403 | PostPermissionSchemeResponse422 | PostPermissionSchemeResponse500 | None:
    """ Creates a permission scheme in the application.

    Args:
        body (PermissionSchemeCreate): PermissionSchemeCreate defines a permission scheme
            creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostPermissionSchemeResponse201 | PostPermissionSchemeResponse400 | PostPermissionSchemeResponse401 | PostPermissionSchemeResponse403 | PostPermissionSchemeResponse422 | PostPermissionSchemeResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
