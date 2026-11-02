from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.o_auth_client_create_request import OAuthClientCreateRequest
from ...models.post_o_auth_client_response_201 import PostOAuthClientResponse201
from ...models.post_o_auth_client_response_400 import PostOAuthClientResponse400
from ...models.post_o_auth_client_response_401 import PostOAuthClientResponse401
from ...models.post_o_auth_client_response_403 import PostOAuthClientResponse403
from ...models.post_o_auth_client_response_422 import PostOAuthClientResponse422
from ...models.post_o_auth_client_response_500 import PostOAuthClientResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: OAuthClientCreateRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/oauth2/clients",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostOAuthClientResponse201 | PostOAuthClientResponse400 | PostOAuthClientResponse401 | PostOAuthClientResponse403 | PostOAuthClientResponse422 | PostOAuthClientResponse500 | None:
    if response.status_code == 201:
        response_201 = PostOAuthClientResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostOAuthClientResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostOAuthClientResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostOAuthClientResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostOAuthClientResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostOAuthClientResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostOAuthClientResponse201 | PostOAuthClientResponse400 | PostOAuthClientResponse401 | PostOAuthClientResponse403 | PostOAuthClientResponse422 | PostOAuthClientResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: OAuthClientCreateRequest | Unset = UNSET,

) -> Response[PostOAuthClientResponse201 | PostOAuthClientResponse400 | PostOAuthClientResponse401 | PostOAuthClientResponse403 | PostOAuthClientResponse422 | PostOAuthClientResponse500]:
    r""" Creates a new OAuth client.

     A user with the \"Manage Applications\" or \"Manage Own Applications\" permission
    can create a new client.

    Args:
        body (OAuthClientCreateRequest | Unset): OAuthClientCreateRequest defines the body for
            creating an OAuth client.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostOAuthClientResponse201 | PostOAuthClientResponse400 | PostOAuthClientResponse401 | PostOAuthClientResponse403 | PostOAuthClientResponse422 | PostOAuthClientResponse500]
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
    body: OAuthClientCreateRequest | Unset = UNSET,

) -> PostOAuthClientResponse201 | PostOAuthClientResponse400 | PostOAuthClientResponse401 | PostOAuthClientResponse403 | PostOAuthClientResponse422 | PostOAuthClientResponse500 | None:
    r""" Creates a new OAuth client.

     A user with the \"Manage Applications\" or \"Manage Own Applications\" permission
    can create a new client.

    Args:
        body (OAuthClientCreateRequest | Unset): OAuthClientCreateRequest defines the body for
            creating an OAuth client.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostOAuthClientResponse201 | PostOAuthClientResponse400 | PostOAuthClientResponse401 | PostOAuthClientResponse403 | PostOAuthClientResponse422 | PostOAuthClientResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: OAuthClientCreateRequest | Unset = UNSET,

) -> Response[PostOAuthClientResponse201 | PostOAuthClientResponse400 | PostOAuthClientResponse401 | PostOAuthClientResponse403 | PostOAuthClientResponse422 | PostOAuthClientResponse500]:
    r""" Creates a new OAuth client.

     A user with the \"Manage Applications\" or \"Manage Own Applications\" permission
    can create a new client.

    Args:
        body (OAuthClientCreateRequest | Unset): OAuthClientCreateRequest defines the body for
            creating an OAuth client.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostOAuthClientResponse201 | PostOAuthClientResponse400 | PostOAuthClientResponse401 | PostOAuthClientResponse403 | PostOAuthClientResponse422 | PostOAuthClientResponse500]
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
    body: OAuthClientCreateRequest | Unset = UNSET,

) -> PostOAuthClientResponse201 | PostOAuthClientResponse400 | PostOAuthClientResponse401 | PostOAuthClientResponse403 | PostOAuthClientResponse422 | PostOAuthClientResponse500 | None:
    r""" Creates a new OAuth client.

     A user with the \"Manage Applications\" or \"Manage Own Applications\" permission
    can create a new client.

    Args:
        body (OAuthClientCreateRequest | Unset): OAuthClientCreateRequest defines the body for
            creating an OAuth client.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostOAuthClientResponse201 | PostOAuthClientResponse400 | PostOAuthClientResponse401 | PostOAuthClientResponse403 | PostOAuthClientResponse422 | PostOAuthClientResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
