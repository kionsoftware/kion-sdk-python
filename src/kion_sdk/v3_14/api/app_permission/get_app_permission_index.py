from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_app_permission_index_response_200 import GetAppPermissionIndexResponse200
from ...models.get_app_permission_index_response_400 import GetAppPermissionIndexResponse400
from ...models.get_app_permission_index_response_401 import GetAppPermissionIndexResponse401
from ...models.get_app_permission_index_response_500 import GetAppPermissionIndexResponse500
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/app-permission",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetAppPermissionIndexResponse200 | GetAppPermissionIndexResponse400 | GetAppPermissionIndexResponse401 | GetAppPermissionIndexResponse500 | None:
    if response.status_code == 200:
        response_200 = GetAppPermissionIndexResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetAppPermissionIndexResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetAppPermissionIndexResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 500:
        response_500 = GetAppPermissionIndexResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetAppPermissionIndexResponse200 | GetAppPermissionIndexResponse400 | GetAppPermissionIndexResponse401 | GetAppPermissionIndexResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetAppPermissionIndexResponse200 | GetAppPermissionIndexResponse400 | GetAppPermissionIndexResponse401 | GetAppPermissionIndexResponse500]:
    r""" Returns a list of app permissions.

     query parameters -
    1. \"type\" - Specify the type of permissions to return.
    Valid types are `ou`, `project`, `global`, or `funding_source`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAppPermissionIndexResponse200 | GetAppPermissionIndexResponse400 | GetAppPermissionIndexResponse401 | GetAppPermissionIndexResponse500]
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

) -> GetAppPermissionIndexResponse200 | GetAppPermissionIndexResponse400 | GetAppPermissionIndexResponse401 | GetAppPermissionIndexResponse500 | None:
    r""" Returns a list of app permissions.

     query parameters -
    1. \"type\" - Specify the type of permissions to return.
    Valid types are `ou`, `project`, `global`, or `funding_source`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAppPermissionIndexResponse200 | GetAppPermissionIndexResponse400 | GetAppPermissionIndexResponse401 | GetAppPermissionIndexResponse500
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetAppPermissionIndexResponse200 | GetAppPermissionIndexResponse400 | GetAppPermissionIndexResponse401 | GetAppPermissionIndexResponse500]:
    r""" Returns a list of app permissions.

     query parameters -
    1. \"type\" - Specify the type of permissions to return.
    Valid types are `ou`, `project`, `global`, or `funding_source`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAppPermissionIndexResponse200 | GetAppPermissionIndexResponse400 | GetAppPermissionIndexResponse401 | GetAppPermissionIndexResponse500]
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

) -> GetAppPermissionIndexResponse200 | GetAppPermissionIndexResponse400 | GetAppPermissionIndexResponse401 | GetAppPermissionIndexResponse500 | None:
    r""" Returns a list of app permissions.

     query parameters -
    1. \"type\" - Specify the type of permissions to return.
    Valid types are `ou`, `project`, `global`, or `funding_source`

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAppPermissionIndexResponse200 | GetAppPermissionIndexResponse400 | GetAppPermissionIndexResponse401 | GetAppPermissionIndexResponse500
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
