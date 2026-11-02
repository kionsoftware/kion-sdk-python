from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.auth_timeout_config import AuthTimeoutConfig
from ...models.put_auth_timeout_config_response_200 import PutAuthTimeoutConfigResponse200
from ...models.put_auth_timeout_config_response_401 import PutAuthTimeoutConfigResponse401
from ...models.put_auth_timeout_config_response_403 import PutAuthTimeoutConfigResponse403
from ...models.put_auth_timeout_config_response_500 import PutAuthTimeoutConfigResponse500
from typing import cast



def _get_kwargs(
    *,
    body: AuthTimeoutConfig,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v3/app-config/auth-timeout",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PutAuthTimeoutConfigResponse200 | PutAuthTimeoutConfigResponse401 | PutAuthTimeoutConfigResponse403 | PutAuthTimeoutConfigResponse500 | None:
    if response.status_code == 200:
        response_200 = PutAuthTimeoutConfigResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = PutAuthTimeoutConfigResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PutAuthTimeoutConfigResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = PutAuthTimeoutConfigResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PutAuthTimeoutConfigResponse200 | PutAuthTimeoutConfigResponse401 | PutAuthTimeoutConfigResponse403 | PutAuthTimeoutConfigResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AuthTimeoutConfig,

) -> Response[PutAuthTimeoutConfigResponse200 | PutAuthTimeoutConfigResponse401 | PutAuthTimeoutConfigResponse403 | PutAuthTimeoutConfigResponse500]:
    """ Sets the auth timeout config settings

    Args:
        body (AuthTimeoutConfig): AuthTimeoutConfig represents the system settings for auth
            timeouts

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutAuthTimeoutConfigResponse200 | PutAuthTimeoutConfigResponse401 | PutAuthTimeoutConfigResponse403 | PutAuthTimeoutConfigResponse500]
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
    body: AuthTimeoutConfig,

) -> PutAuthTimeoutConfigResponse200 | PutAuthTimeoutConfigResponse401 | PutAuthTimeoutConfigResponse403 | PutAuthTimeoutConfigResponse500 | None:
    """ Sets the auth timeout config settings

    Args:
        body (AuthTimeoutConfig): AuthTimeoutConfig represents the system settings for auth
            timeouts

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutAuthTimeoutConfigResponse200 | PutAuthTimeoutConfigResponse401 | PutAuthTimeoutConfigResponse403 | PutAuthTimeoutConfigResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AuthTimeoutConfig,

) -> Response[PutAuthTimeoutConfigResponse200 | PutAuthTimeoutConfigResponse401 | PutAuthTimeoutConfigResponse403 | PutAuthTimeoutConfigResponse500]:
    """ Sets the auth timeout config settings

    Args:
        body (AuthTimeoutConfig): AuthTimeoutConfig represents the system settings for auth
            timeouts

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutAuthTimeoutConfigResponse200 | PutAuthTimeoutConfigResponse401 | PutAuthTimeoutConfigResponse403 | PutAuthTimeoutConfigResponse500]
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
    body: AuthTimeoutConfig,

) -> PutAuthTimeoutConfigResponse200 | PutAuthTimeoutConfigResponse401 | PutAuthTimeoutConfigResponse403 | PutAuthTimeoutConfigResponse500 | None:
    """ Sets the auth timeout config settings

    Args:
        body (AuthTimeoutConfig): AuthTimeoutConfig represents the system settings for auth
            timeouts

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutAuthTimeoutConfigResponse200 | PutAuthTimeoutConfigResponse401 | PutAuthTimeoutConfigResponse403 | PutAuthTimeoutConfigResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
