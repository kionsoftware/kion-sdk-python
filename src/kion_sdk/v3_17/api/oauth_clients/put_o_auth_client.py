from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.o_auth_client_update_request import OAuthClientUpdateRequest
from ...models.put_o_auth_client_response_200 import PutOAuthClientResponse200
from ...models.put_o_auth_client_response_400 import PutOAuthClientResponse400
from ...models.put_o_auth_client_response_401 import PutOAuthClientResponse401
from ...models.put_o_auth_client_response_403 import PutOAuthClientResponse403
from ...models.put_o_auth_client_response_404 import PutOAuthClientResponse404
from ...models.put_o_auth_client_response_422 import PutOAuthClientResponse422
from ...models.put_o_auth_client_response_500 import PutOAuthClientResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: OAuthClientUpdateRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v3/oauth2/clients/{id}".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PutOAuthClientResponse200 | PutOAuthClientResponse400 | PutOAuthClientResponse401 | PutOAuthClientResponse403 | PutOAuthClientResponse404 | PutOAuthClientResponse422 | PutOAuthClientResponse500 | None:
    if response.status_code == 200:
        response_200 = PutOAuthClientResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PutOAuthClientResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PutOAuthClientResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PutOAuthClientResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PutOAuthClientResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PutOAuthClientResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PutOAuthClientResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PutOAuthClientResponse200 | PutOAuthClientResponse400 | PutOAuthClientResponse401 | PutOAuthClientResponse403 | PutOAuthClientResponse404 | PutOAuthClientResponse422 | PutOAuthClientResponse500]:
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
    body: OAuthClientUpdateRequest | Unset = UNSET,

) -> Response[PutOAuthClientResponse200 | PutOAuthClientResponse400 | PutOAuthClientResponse401 | PutOAuthClientResponse403 | PutOAuthClientResponse404 | PutOAuthClientResponse422 | PutOAuthClientResponse500]:
    r""" Updates an existing OAuth client.

     Manually updating a dynamically registered client through this endpoint
    permanently converts it to a manually managed client. It will no longer be
    considered managed by Dynamic Client Registration, and its registration
    access token will be revoked.

    A user with the \"Manage Applications\" permission can update any client. A user
    with the \"Manage Own Applications\" permission can update only their own clients.

    Args:
        id (str):
        body (OAuthClientUpdateRequest | Unset): OAuthClientUpdateRequest defines the body for
            updating an OAuth client.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutOAuthClientResponse200 | PutOAuthClientResponse400 | PutOAuthClientResponse401 | PutOAuthClientResponse403 | PutOAuthClientResponse404 | PutOAuthClientResponse422 | PutOAuthClientResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: OAuthClientUpdateRequest | Unset = UNSET,

) -> PutOAuthClientResponse200 | PutOAuthClientResponse400 | PutOAuthClientResponse401 | PutOAuthClientResponse403 | PutOAuthClientResponse404 | PutOAuthClientResponse422 | PutOAuthClientResponse500 | None:
    r""" Updates an existing OAuth client.

     Manually updating a dynamically registered client through this endpoint
    permanently converts it to a manually managed client. It will no longer be
    considered managed by Dynamic Client Registration, and its registration
    access token will be revoked.

    A user with the \"Manage Applications\" permission can update any client. A user
    with the \"Manage Own Applications\" permission can update only their own clients.

    Args:
        id (str):
        body (OAuthClientUpdateRequest | Unset): OAuthClientUpdateRequest defines the body for
            updating an OAuth client.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutOAuthClientResponse200 | PutOAuthClientResponse400 | PutOAuthClientResponse401 | PutOAuthClientResponse403 | PutOAuthClientResponse404 | PutOAuthClientResponse422 | PutOAuthClientResponse500
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: OAuthClientUpdateRequest | Unset = UNSET,

) -> Response[PutOAuthClientResponse200 | PutOAuthClientResponse400 | PutOAuthClientResponse401 | PutOAuthClientResponse403 | PutOAuthClientResponse404 | PutOAuthClientResponse422 | PutOAuthClientResponse500]:
    r""" Updates an existing OAuth client.

     Manually updating a dynamically registered client through this endpoint
    permanently converts it to a manually managed client. It will no longer be
    considered managed by Dynamic Client Registration, and its registration
    access token will be revoked.

    A user with the \"Manage Applications\" permission can update any client. A user
    with the \"Manage Own Applications\" permission can update only their own clients.

    Args:
        id (str):
        body (OAuthClientUpdateRequest | Unset): OAuthClientUpdateRequest defines the body for
            updating an OAuth client.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutOAuthClientResponse200 | PutOAuthClientResponse400 | PutOAuthClientResponse401 | PutOAuthClientResponse403 | PutOAuthClientResponse404 | PutOAuthClientResponse422 | PutOAuthClientResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: OAuthClientUpdateRequest | Unset = UNSET,

) -> PutOAuthClientResponse200 | PutOAuthClientResponse400 | PutOAuthClientResponse401 | PutOAuthClientResponse403 | PutOAuthClientResponse404 | PutOAuthClientResponse422 | PutOAuthClientResponse500 | None:
    r""" Updates an existing OAuth client.

     Manually updating a dynamically registered client through this endpoint
    permanently converts it to a manually managed client. It will no longer be
    considered managed by Dynamic Client Registration, and its registration
    access token will be revoked.

    A user with the \"Manage Applications\" permission can update any client. A user
    with the \"Manage Own Applications\" permission can update only their own clients.

    Args:
        id (str):
        body (OAuthClientUpdateRequest | Unset): OAuthClientUpdateRequest defines the body for
            updating an OAuth client.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutOAuthClientResponse200 | PutOAuthClientResponse400 | PutOAuthClientResponse401 | PutOAuthClientResponse403 | PutOAuthClientResponse404 | PutOAuthClientResponse422 | PutOAuthClientResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
