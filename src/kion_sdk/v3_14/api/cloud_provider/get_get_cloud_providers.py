from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_get_cloud_providers_response_200 import GetGetCloudProvidersResponse200
from ...models.get_get_cloud_providers_response_401 import GetGetCloudProvidersResponse401
from ...models.get_get_cloud_providers_response_500 import GetGetCloudProvidersResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    only_enabled: bool | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["only_enabled"] = only_enabled


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/cloud-provider",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetGetCloudProvidersResponse200 | GetGetCloudProvidersResponse401 | GetGetCloudProvidersResponse500 | None:
    if response.status_code == 200:
        response_200 = GetGetCloudProvidersResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetGetCloudProvidersResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 500:
        response_500 = GetGetCloudProvidersResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetGetCloudProvidersResponse200 | GetGetCloudProvidersResponse401 | GetGetCloudProvidersResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    only_enabled: bool | Unset = UNSET,

) -> Response[GetGetCloudProvidersResponse200 | GetGetCloudProvidersResponse401 | GetGetCloudProvidersResponse500]:
    """ Returns a list of cloud providers and their enabled status.

    Args:
        only_enabled (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGetCloudProvidersResponse200 | GetGetCloudProvidersResponse401 | GetGetCloudProvidersResponse500]
     """


    kwargs = _get_kwargs(
        only_enabled=only_enabled,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    only_enabled: bool | Unset = UNSET,

) -> GetGetCloudProvidersResponse200 | GetGetCloudProvidersResponse401 | GetGetCloudProvidersResponse500 | None:
    """ Returns a list of cloud providers and their enabled status.

    Args:
        only_enabled (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGetCloudProvidersResponse200 | GetGetCloudProvidersResponse401 | GetGetCloudProvidersResponse500
     """


    return sync_detailed(
        client=client,
only_enabled=only_enabled,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    only_enabled: bool | Unset = UNSET,

) -> Response[GetGetCloudProvidersResponse200 | GetGetCloudProvidersResponse401 | GetGetCloudProvidersResponse500]:
    """ Returns a list of cloud providers and their enabled status.

    Args:
        only_enabled (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGetCloudProvidersResponse200 | GetGetCloudProvidersResponse401 | GetGetCloudProvidersResponse500]
     """


    kwargs = _get_kwargs(
        only_enabled=only_enabled,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    only_enabled: bool | Unset = UNSET,

) -> GetGetCloudProvidersResponse200 | GetGetCloudProvidersResponse401 | GetGetCloudProvidersResponse500 | None:
    """ Returns a list of cloud providers and their enabled status.

    Args:
        only_enabled (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGetCloudProvidersResponse200 | GetGetCloudProvidersResponse401 | GetGetCloudProvidersResponse500
     """


    return (await asyncio_detailed(
        client=client,
only_enabled=only_enabled,

    )).parsed
