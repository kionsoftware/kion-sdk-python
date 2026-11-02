from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_master_key_settings_response_200 import GetMasterKeySettingsResponse200
from ...models.get_master_key_settings_response_400 import GetMasterKeySettingsResponse400
from ...models.get_master_key_settings_response_403 import GetMasterKeySettingsResponse403
from ...models.get_master_key_settings_response_422 import GetMasterKeySettingsResponse422
from ...models.get_master_key_settings_response_500 import GetMasterKeySettingsResponse500
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/master-key/settings",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetMasterKeySettingsResponse200 | GetMasterKeySettingsResponse400 | GetMasterKeySettingsResponse403 | GetMasterKeySettingsResponse422 | GetMasterKeySettingsResponse500 | None:
    if response.status_code == 200:
        response_200 = GetMasterKeySettingsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetMasterKeySettingsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 403:
        response_403 = GetMasterKeySettingsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = GetMasterKeySettingsResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = GetMasterKeySettingsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetMasterKeySettingsResponse200 | GetMasterKeySettingsResponse400 | GetMasterKeySettingsResponse403 | GetMasterKeySettingsResponse422 | GetMasterKeySettingsResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetMasterKeySettingsResponse200 | GetMasterKeySettingsResponse400 | GetMasterKeySettingsResponse403 | GetMasterKeySettingsResponse422 | GetMasterKeySettingsResponse500]:
    """ Gets the storage mode settings for the master key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMasterKeySettingsResponse200 | GetMasterKeySettingsResponse400 | GetMasterKeySettingsResponse403 | GetMasterKeySettingsResponse422 | GetMasterKeySettingsResponse500]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,

) -> GetMasterKeySettingsResponse200 | GetMasterKeySettingsResponse400 | GetMasterKeySettingsResponse403 | GetMasterKeySettingsResponse422 | GetMasterKeySettingsResponse500 | None:
    """ Gets the storage mode settings for the master key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMasterKeySettingsResponse200 | GetMasterKeySettingsResponse400 | GetMasterKeySettingsResponse403 | GetMasterKeySettingsResponse422 | GetMasterKeySettingsResponse500
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetMasterKeySettingsResponse200 | GetMasterKeySettingsResponse400 | GetMasterKeySettingsResponse403 | GetMasterKeySettingsResponse422 | GetMasterKeySettingsResponse500]:
    """ Gets the storage mode settings for the master key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMasterKeySettingsResponse200 | GetMasterKeySettingsResponse400 | GetMasterKeySettingsResponse403 | GetMasterKeySettingsResponse422 | GetMasterKeySettingsResponse500]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,

) -> GetMasterKeySettingsResponse200 | GetMasterKeySettingsResponse400 | GetMasterKeySettingsResponse403 | GetMasterKeySettingsResponse422 | GetMasterKeySettingsResponse500 | None:
    """ Gets the storage mode settings for the master key.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMasterKeySettingsResponse200 | GetMasterKeySettingsResponse400 | GetMasterKeySettingsResponse403 | GetMasterKeySettingsResponse422 | GetMasterKeySettingsResponse500
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
