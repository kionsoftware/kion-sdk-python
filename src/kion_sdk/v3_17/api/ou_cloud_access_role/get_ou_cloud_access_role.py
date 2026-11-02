from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_ou_cloud_access_role_response_200 import GetOUCloudAccessRoleResponse200
from ...models.get_ou_cloud_access_role_response_401 import GetOUCloudAccessRoleResponse401
from ...models.get_ou_cloud_access_role_response_403 import GetOUCloudAccessRoleResponse403
from ...models.get_ou_cloud_access_role_response_404 import GetOUCloudAccessRoleResponse404
from ...models.get_ou_cloud_access_role_response_500 import GetOUCloudAccessRoleResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/ou-cloud-access-role/{id}".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetOUCloudAccessRoleResponse200 | GetOUCloudAccessRoleResponse401 | GetOUCloudAccessRoleResponse403 | GetOUCloudAccessRoleResponse404 | GetOUCloudAccessRoleResponse500 | None:
    if response.status_code == 200:
        response_200 = GetOUCloudAccessRoleResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetOUCloudAccessRoleResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetOUCloudAccessRoleResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetOUCloudAccessRoleResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetOUCloudAccessRoleResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetOUCloudAccessRoleResponse200 | GetOUCloudAccessRoleResponse401 | GetOUCloudAccessRoleResponse403 | GetOUCloudAccessRoleResponse404 | GetOUCloudAccessRoleResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetOUCloudAccessRoleResponse200 | GetOUCloudAccessRoleResponse401 | GetOUCloudAccessRoleResponse403 | GetOUCloudAccessRoleResponse404 | GetOUCloudAccessRoleResponse500]:
    """ Finds a ou cloud access role by ID in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOUCloudAccessRoleResponse200 | GetOUCloudAccessRoleResponse401 | GetOUCloudAccessRoleResponse403 | GetOUCloudAccessRoleResponse404 | GetOUCloudAccessRoleResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,

) -> GetOUCloudAccessRoleResponse200 | GetOUCloudAccessRoleResponse401 | GetOUCloudAccessRoleResponse403 | GetOUCloudAccessRoleResponse404 | GetOUCloudAccessRoleResponse500 | None:
    """ Finds a ou cloud access role by ID in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOUCloudAccessRoleResponse200 | GetOUCloudAccessRoleResponse401 | GetOUCloudAccessRoleResponse403 | GetOUCloudAccessRoleResponse404 | GetOUCloudAccessRoleResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetOUCloudAccessRoleResponse200 | GetOUCloudAccessRoleResponse401 | GetOUCloudAccessRoleResponse403 | GetOUCloudAccessRoleResponse404 | GetOUCloudAccessRoleResponse500]:
    """ Finds a ou cloud access role by ID in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOUCloudAccessRoleResponse200 | GetOUCloudAccessRoleResponse401 | GetOUCloudAccessRoleResponse403 | GetOUCloudAccessRoleResponse404 | GetOUCloudAccessRoleResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,

) -> GetOUCloudAccessRoleResponse200 | GetOUCloudAccessRoleResponse401 | GetOUCloudAccessRoleResponse403 | GetOUCloudAccessRoleResponse404 | GetOUCloudAccessRoleResponse500 | None:
    """ Finds a ou cloud access role by ID in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOUCloudAccessRoleResponse200 | GetOUCloudAccessRoleResponse401 | GetOUCloudAccessRoleResponse403 | GetOUCloudAccessRoleResponse404 | GetOUCloudAccessRoleResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
