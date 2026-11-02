from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_ou_cloud_access_role_index_response_200 import GetOUCloudAccessRoleIndexResponse200
from ...models.get_ou_cloud_access_role_index_response_401 import GetOUCloudAccessRoleIndexResponse401
from ...models.get_ou_cloud_access_role_index_response_403 import GetOUCloudAccessRoleIndexResponse403
from ...models.get_ou_cloud_access_role_index_response_422 import GetOUCloudAccessRoleIndexResponse422
from ...models.get_ou_cloud_access_role_index_response_500 import GetOUCloudAccessRoleIndexResponse500
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v4/ou-cloud-access-role",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetOUCloudAccessRoleIndexResponse200 | GetOUCloudAccessRoleIndexResponse401 | GetOUCloudAccessRoleIndexResponse403 | GetOUCloudAccessRoleIndexResponse422 | GetOUCloudAccessRoleIndexResponse500 | None:
    if response.status_code == 200:
        response_200 = GetOUCloudAccessRoleIndexResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetOUCloudAccessRoleIndexResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetOUCloudAccessRoleIndexResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = GetOUCloudAccessRoleIndexResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = GetOUCloudAccessRoleIndexResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetOUCloudAccessRoleIndexResponse200 | GetOUCloudAccessRoleIndexResponse401 | GetOUCloudAccessRoleIndexResponse403 | GetOUCloudAccessRoleIndexResponse422 | GetOUCloudAccessRoleIndexResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetOUCloudAccessRoleIndexResponse200 | GetOUCloudAccessRoleIndexResponse401 | GetOUCloudAccessRoleIndexResponse403 | GetOUCloudAccessRoleIndexResponse422 | GetOUCloudAccessRoleIndexResponse500]:
    """ Gets a list of all ou cloud access roles in the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOUCloudAccessRoleIndexResponse200 | GetOUCloudAccessRoleIndexResponse401 | GetOUCloudAccessRoleIndexResponse403 | GetOUCloudAccessRoleIndexResponse422 | GetOUCloudAccessRoleIndexResponse500]
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

) -> GetOUCloudAccessRoleIndexResponse200 | GetOUCloudAccessRoleIndexResponse401 | GetOUCloudAccessRoleIndexResponse403 | GetOUCloudAccessRoleIndexResponse422 | GetOUCloudAccessRoleIndexResponse500 | None:
    """ Gets a list of all ou cloud access roles in the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOUCloudAccessRoleIndexResponse200 | GetOUCloudAccessRoleIndexResponse401 | GetOUCloudAccessRoleIndexResponse403 | GetOUCloudAccessRoleIndexResponse422 | GetOUCloudAccessRoleIndexResponse500
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetOUCloudAccessRoleIndexResponse200 | GetOUCloudAccessRoleIndexResponse401 | GetOUCloudAccessRoleIndexResponse403 | GetOUCloudAccessRoleIndexResponse422 | GetOUCloudAccessRoleIndexResponse500]:
    """ Gets a list of all ou cloud access roles in the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOUCloudAccessRoleIndexResponse200 | GetOUCloudAccessRoleIndexResponse401 | GetOUCloudAccessRoleIndexResponse403 | GetOUCloudAccessRoleIndexResponse422 | GetOUCloudAccessRoleIndexResponse500]
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

) -> GetOUCloudAccessRoleIndexResponse200 | GetOUCloudAccessRoleIndexResponse401 | GetOUCloudAccessRoleIndexResponse403 | GetOUCloudAccessRoleIndexResponse422 | GetOUCloudAccessRoleIndexResponse500 | None:
    """ Gets a list of all ou cloud access roles in the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOUCloudAccessRoleIndexResponse200 | GetOUCloudAccessRoleIndexResponse401 | GetOUCloudAccessRoleIndexResponse403 | GetOUCloudAccessRoleIndexResponse422 | GetOUCloudAccessRoleIndexResponse500
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
