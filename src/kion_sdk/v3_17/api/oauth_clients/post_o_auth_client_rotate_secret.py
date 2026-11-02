from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_o_auth_client_rotate_secret_response_200 import PostOAuthClientRotateSecretResponse200
from ...models.post_o_auth_client_rotate_secret_response_400 import PostOAuthClientRotateSecretResponse400
from ...models.post_o_auth_client_rotate_secret_response_401 import PostOAuthClientRotateSecretResponse401
from ...models.post_o_auth_client_rotate_secret_response_403 import PostOAuthClientRotateSecretResponse403
from ...models.post_o_auth_client_rotate_secret_response_404 import PostOAuthClientRotateSecretResponse404
from ...models.post_o_auth_client_rotate_secret_response_500 import PostOAuthClientRotateSecretResponse500
from typing import cast



def _get_kwargs(
    id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/oauth2/clients/{id}/rotate-secret".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostOAuthClientRotateSecretResponse200 | PostOAuthClientRotateSecretResponse400 | PostOAuthClientRotateSecretResponse401 | PostOAuthClientRotateSecretResponse403 | PostOAuthClientRotateSecretResponse404 | PostOAuthClientRotateSecretResponse500 | None:
    if response.status_code == 200:
        response_200 = PostOAuthClientRotateSecretResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PostOAuthClientRotateSecretResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostOAuthClientRotateSecretResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostOAuthClientRotateSecretResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PostOAuthClientRotateSecretResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = PostOAuthClientRotateSecretResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostOAuthClientRotateSecretResponse200 | PostOAuthClientRotateSecretResponse400 | PostOAuthClientRotateSecretResponse401 | PostOAuthClientRotateSecretResponse403 | PostOAuthClientRotateSecretResponse404 | PostOAuthClientRotateSecretResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,

) -> Response[PostOAuthClientRotateSecretResponse200 | PostOAuthClientRotateSecretResponse400 | PostOAuthClientRotateSecretResponse401 | PostOAuthClientRotateSecretResponse403 | PostOAuthClientRotateSecretResponse404 | PostOAuthClientRotateSecretResponse500]:
    r""" Rotates the client secret for an OAuth client.

     A user with the \"Manage Applications\" permission can rotate secrets for any client.
    A user with the \"Manage Own Applications\" permission can rotate secrets only for
    their own clients. Cannot rotate secrets for public clients.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostOAuthClientRotateSecretResponse200 | PostOAuthClientRotateSecretResponse400 | PostOAuthClientRotateSecretResponse401 | PostOAuthClientRotateSecretResponse403 | PostOAuthClientRotateSecretResponse404 | PostOAuthClientRotateSecretResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient,

) -> PostOAuthClientRotateSecretResponse200 | PostOAuthClientRotateSecretResponse400 | PostOAuthClientRotateSecretResponse401 | PostOAuthClientRotateSecretResponse403 | PostOAuthClientRotateSecretResponse404 | PostOAuthClientRotateSecretResponse500 | None:
    r""" Rotates the client secret for an OAuth client.

     A user with the \"Manage Applications\" permission can rotate secrets for any client.
    A user with the \"Manage Own Applications\" permission can rotate secrets only for
    their own clients. Cannot rotate secrets for public clients.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostOAuthClientRotateSecretResponse200 | PostOAuthClientRotateSecretResponse400 | PostOAuthClientRotateSecretResponse401 | PostOAuthClientRotateSecretResponse403 | PostOAuthClientRotateSecretResponse404 | PostOAuthClientRotateSecretResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,

) -> Response[PostOAuthClientRotateSecretResponse200 | PostOAuthClientRotateSecretResponse400 | PostOAuthClientRotateSecretResponse401 | PostOAuthClientRotateSecretResponse403 | PostOAuthClientRotateSecretResponse404 | PostOAuthClientRotateSecretResponse500]:
    r""" Rotates the client secret for an OAuth client.

     A user with the \"Manage Applications\" permission can rotate secrets for any client.
    A user with the \"Manage Own Applications\" permission can rotate secrets only for
    their own clients. Cannot rotate secrets for public clients.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostOAuthClientRotateSecretResponse200 | PostOAuthClientRotateSecretResponse400 | PostOAuthClientRotateSecretResponse401 | PostOAuthClientRotateSecretResponse403 | PostOAuthClientRotateSecretResponse404 | PostOAuthClientRotateSecretResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,

) -> PostOAuthClientRotateSecretResponse200 | PostOAuthClientRotateSecretResponse400 | PostOAuthClientRotateSecretResponse401 | PostOAuthClientRotateSecretResponse403 | PostOAuthClientRotateSecretResponse404 | PostOAuthClientRotateSecretResponse500 | None:
    r""" Rotates the client secret for an OAuth client.

     A user with the \"Manage Applications\" permission can rotate secrets for any client.
    A user with the \"Manage Own Applications\" permission can rotate secrets only for
    their own clients. Cannot rotate secrets for public clients.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostOAuthClientRotateSecretResponse200 | PostOAuthClientRotateSecretResponse400 | PostOAuthClientRotateSecretResponse401 | PostOAuthClientRotateSecretResponse403 | PostOAuthClientRotateSecretResponse404 | PostOAuthClientRotateSecretResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
