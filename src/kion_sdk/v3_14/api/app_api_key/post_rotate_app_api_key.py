from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_rotate_app_api_key_response_201 import PostRotateAppAPIKeyResponse201
from ...models.post_rotate_app_api_key_response_400 import PostRotateAppAPIKeyResponse400
from ...models.post_rotate_app_api_key_response_401 import PostRotateAppAPIKeyResponse401
from ...models.post_rotate_app_api_key_response_403 import PostRotateAppAPIKeyResponse403
from ...models.post_rotate_app_api_key_response_422 import PostRotateAppAPIKeyResponse422
from ...models.post_rotate_app_api_key_response_500 import PostRotateAppAPIKeyResponse500
from ...models.rotate_key import RotateKey
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: RotateKey | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/app-api-key/rotate",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostRotateAppAPIKeyResponse201 | PostRotateAppAPIKeyResponse400 | PostRotateAppAPIKeyResponse401 | PostRotateAppAPIKeyResponse403 | PostRotateAppAPIKeyResponse422 | PostRotateAppAPIKeyResponse500 | None:
    if response.status_code == 201:
        response_201 = PostRotateAppAPIKeyResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostRotateAppAPIKeyResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostRotateAppAPIKeyResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostRotateAppAPIKeyResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostRotateAppAPIKeyResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostRotateAppAPIKeyResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostRotateAppAPIKeyResponse201 | PostRotateAppAPIKeyResponse400 | PostRotateAppAPIKeyResponse401 | PostRotateAppAPIKeyResponse403 | PostRotateAppAPIKeyResponse422 | PostRotateAppAPIKeyResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RotateKey | Unset = UNSET,

) -> Response[PostRotateAppAPIKeyResponse201 | PostRotateAppAPIKeyResponse400 | PostRotateAppAPIKeyResponse401 | PostRotateAppAPIKeyResponse403 | PostRotateAppAPIKeyResponse422 | PostRotateAppAPIKeyResponse500]:
    """ Rotates the passed in App API Key.

    Args:
        body (RotateKey | Unset): RotateKey defines an App API Key rotation request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostRotateAppAPIKeyResponse201 | PostRotateAppAPIKeyResponse400 | PostRotateAppAPIKeyResponse401 | PostRotateAppAPIKeyResponse403 | PostRotateAppAPIKeyResponse422 | PostRotateAppAPIKeyResponse500]
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
    body: RotateKey | Unset = UNSET,

) -> PostRotateAppAPIKeyResponse201 | PostRotateAppAPIKeyResponse400 | PostRotateAppAPIKeyResponse401 | PostRotateAppAPIKeyResponse403 | PostRotateAppAPIKeyResponse422 | PostRotateAppAPIKeyResponse500 | None:
    """ Rotates the passed in App API Key.

    Args:
        body (RotateKey | Unset): RotateKey defines an App API Key rotation request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostRotateAppAPIKeyResponse201 | PostRotateAppAPIKeyResponse400 | PostRotateAppAPIKeyResponse401 | PostRotateAppAPIKeyResponse403 | PostRotateAppAPIKeyResponse422 | PostRotateAppAPIKeyResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RotateKey | Unset = UNSET,

) -> Response[PostRotateAppAPIKeyResponse201 | PostRotateAppAPIKeyResponse400 | PostRotateAppAPIKeyResponse401 | PostRotateAppAPIKeyResponse403 | PostRotateAppAPIKeyResponse422 | PostRotateAppAPIKeyResponse500]:
    """ Rotates the passed in App API Key.

    Args:
        body (RotateKey | Unset): RotateKey defines an App API Key rotation request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostRotateAppAPIKeyResponse201 | PostRotateAppAPIKeyResponse400 | PostRotateAppAPIKeyResponse401 | PostRotateAppAPIKeyResponse403 | PostRotateAppAPIKeyResponse422 | PostRotateAppAPIKeyResponse500]
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
    body: RotateKey | Unset = UNSET,

) -> PostRotateAppAPIKeyResponse201 | PostRotateAppAPIKeyResponse400 | PostRotateAppAPIKeyResponse401 | PostRotateAppAPIKeyResponse403 | PostRotateAppAPIKeyResponse422 | PostRotateAppAPIKeyResponse500 | None:
    """ Rotates the passed in App API Key.

    Args:
        body (RotateKey | Unset): RotateKey defines an App API Key rotation request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostRotateAppAPIKeyResponse201 | PostRotateAppAPIKeyResponse400 | PostRotateAppAPIKeyResponse401 | PostRotateAppAPIKeyResponse403 | PostRotateAppAPIKeyResponse422 | PostRotateAppAPIKeyResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
