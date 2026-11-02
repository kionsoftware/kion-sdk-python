from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.auth_create import AuthCreate
from ...models.post_token_response_200 import PostTokenResponse200
from ...models.post_token_response_400 import PostTokenResponse400
from ...models.post_token_response_422 import PostTokenResponse422
from typing import cast



def _get_kwargs(
    *,
    body: AuthCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/token",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostTokenResponse200 | PostTokenResponse400 | PostTokenResponse422 | None:
    if response.status_code == 200:
        response_200 = PostTokenResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PostTokenResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 422:
        response_422 = PostTokenResponse422.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostTokenResponse200 | PostTokenResponse400 | PostTokenResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AuthCreate,

) -> Response[PostTokenResponse200 | PostTokenResponse400 | PostTokenResponse422]:
    """ Returns a token after successful authentication as a valid user.

     Note: This endpoint does not support TOTP and U2F.

    Args:
        body (AuthCreate): AuthCreate defines a request to create an AuthToken.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostTokenResponse200 | PostTokenResponse400 | PostTokenResponse422]
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
    body: AuthCreate,

) -> PostTokenResponse200 | PostTokenResponse400 | PostTokenResponse422 | None:
    """ Returns a token after successful authentication as a valid user.

     Note: This endpoint does not support TOTP and U2F.

    Args:
        body (AuthCreate): AuthCreate defines a request to create an AuthToken.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostTokenResponse200 | PostTokenResponse400 | PostTokenResponse422
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AuthCreate,

) -> Response[PostTokenResponse200 | PostTokenResponse400 | PostTokenResponse422]:
    """ Returns a token after successful authentication as a valid user.

     Note: This endpoint does not support TOTP and U2F.

    Args:
        body (AuthCreate): AuthCreate defines a request to create an AuthToken.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostTokenResponse200 | PostTokenResponse400 | PostTokenResponse422]
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
    body: AuthCreate,

) -> PostTokenResponse200 | PostTokenResponse400 | PostTokenResponse422 | None:
    """ Returns a token after successful authentication as a valid user.

     Note: This endpoint does not support TOTP and U2F.

    Args:
        body (AuthCreate): AuthCreate defines a request to create an AuthToken.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostTokenResponse200 | PostTokenResponse400 | PostTokenResponse422
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
