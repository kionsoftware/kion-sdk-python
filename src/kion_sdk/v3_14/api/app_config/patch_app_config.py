from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.app_config import AppConfig
from ...models.patch_app_config_response_201 import PatchAppConfigResponse201
from ...models.patch_app_config_response_400 import PatchAppConfigResponse400
from ...models.patch_app_config_response_401 import PatchAppConfigResponse401
from ...models.patch_app_config_response_403 import PatchAppConfigResponse403
from ...models.patch_app_config_response_500 import PatchAppConfigResponse500
from typing import cast



def _get_kwargs(
    *,
    body: AppConfig,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/app-config",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchAppConfigResponse201 | PatchAppConfigResponse400 | PatchAppConfigResponse401 | PatchAppConfigResponse403 | PatchAppConfigResponse500 | None:
    if response.status_code == 201:
        response_201 = PatchAppConfigResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PatchAppConfigResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchAppConfigResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchAppConfigResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = PatchAppConfigResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchAppConfigResponse201 | PatchAppConfigResponse400 | PatchAppConfigResponse401 | PatchAppConfigResponse403 | PatchAppConfigResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AppConfig,

) -> Response[PatchAppConfigResponse201 | PatchAppConfigResponse400 | PatchAppConfigResponse401 | PatchAppConfigResponse403 | PatchAppConfigResponse500]:
    """ Updates passed in Kion settings.

    Args:
        body (AppConfig): AppConfig defines an AppConfig.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchAppConfigResponse201 | PatchAppConfigResponse400 | PatchAppConfigResponse401 | PatchAppConfigResponse403 | PatchAppConfigResponse500]
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
    body: AppConfig,

) -> PatchAppConfigResponse201 | PatchAppConfigResponse400 | PatchAppConfigResponse401 | PatchAppConfigResponse403 | PatchAppConfigResponse500 | None:
    """ Updates passed in Kion settings.

    Args:
        body (AppConfig): AppConfig defines an AppConfig.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchAppConfigResponse201 | PatchAppConfigResponse400 | PatchAppConfigResponse401 | PatchAppConfigResponse403 | PatchAppConfigResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AppConfig,

) -> Response[PatchAppConfigResponse201 | PatchAppConfigResponse400 | PatchAppConfigResponse401 | PatchAppConfigResponse403 | PatchAppConfigResponse500]:
    """ Updates passed in Kion settings.

    Args:
        body (AppConfig): AppConfig defines an AppConfig.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchAppConfigResponse201 | PatchAppConfigResponse400 | PatchAppConfigResponse401 | PatchAppConfigResponse403 | PatchAppConfigResponse500]
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
    body: AppConfig,

) -> PatchAppConfigResponse201 | PatchAppConfigResponse400 | PatchAppConfigResponse401 | PatchAppConfigResponse403 | PatchAppConfigResponse500 | None:
    """ Updates passed in Kion settings.

    Args:
        body (AppConfig): AppConfig defines an AppConfig.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchAppConfigResponse201 | PatchAppConfigResponse400 | PatchAppConfigResponse401 | PatchAppConfigResponse403 | PatchAppConfigResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
