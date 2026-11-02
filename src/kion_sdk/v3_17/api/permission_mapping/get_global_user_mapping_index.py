from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_global_user_mapping_index_response_200 import GetGlobalUserMappingIndexResponse200
from ...models.get_global_user_mapping_index_response_401 import GetGlobalUserMappingIndexResponse401
from ...models.get_global_user_mapping_index_response_403 import GetGlobalUserMappingIndexResponse403
from ...models.get_global_user_mapping_index_response_500 import GetGlobalUserMappingIndexResponse500
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/global/permission-mapping",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetGlobalUserMappingIndexResponse200 | GetGlobalUserMappingIndexResponse401 | GetGlobalUserMappingIndexResponse403 | GetGlobalUserMappingIndexResponse500 | None:
    if response.status_code == 200:
        response_200 = GetGlobalUserMappingIndexResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetGlobalUserMappingIndexResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetGlobalUserMappingIndexResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetGlobalUserMappingIndexResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetGlobalUserMappingIndexResponse200 | GetGlobalUserMappingIndexResponse401 | GetGlobalUserMappingIndexResponse403 | GetGlobalUserMappingIndexResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetGlobalUserMappingIndexResponse200 | GetGlobalUserMappingIndexResponse401 | GetGlobalUserMappingIndexResponse403 | GetGlobalUserMappingIndexResponse500]:
    """ Returns a list of user permission mappings for the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGlobalUserMappingIndexResponse200 | GetGlobalUserMappingIndexResponse401 | GetGlobalUserMappingIndexResponse403 | GetGlobalUserMappingIndexResponse500]
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

) -> GetGlobalUserMappingIndexResponse200 | GetGlobalUserMappingIndexResponse401 | GetGlobalUserMappingIndexResponse403 | GetGlobalUserMappingIndexResponse500 | None:
    """ Returns a list of user permission mappings for the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGlobalUserMappingIndexResponse200 | GetGlobalUserMappingIndexResponse401 | GetGlobalUserMappingIndexResponse403 | GetGlobalUserMappingIndexResponse500
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetGlobalUserMappingIndexResponse200 | GetGlobalUserMappingIndexResponse401 | GetGlobalUserMappingIndexResponse403 | GetGlobalUserMappingIndexResponse500]:
    """ Returns a list of user permission mappings for the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGlobalUserMappingIndexResponse200 | GetGlobalUserMappingIndexResponse401 | GetGlobalUserMappingIndexResponse403 | GetGlobalUserMappingIndexResponse500]
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

) -> GetGlobalUserMappingIndexResponse200 | GetGlobalUserMappingIndexResponse401 | GetGlobalUserMappingIndexResponse403 | GetGlobalUserMappingIndexResponse500 | None:
    """ Returns a list of user permission mappings for the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGlobalUserMappingIndexResponse200 | GetGlobalUserMappingIndexResponse401 | GetGlobalUserMappingIndexResponse403 | GetGlobalUserMappingIndexResponse500
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
