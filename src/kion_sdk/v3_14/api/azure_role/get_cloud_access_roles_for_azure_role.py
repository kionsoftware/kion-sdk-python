from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_cloud_access_roles_for_azure_role_response_200 import GetCloudAccessRolesForAzureRoleResponse200
from ...models.get_cloud_access_roles_for_azure_role_response_401 import GetCloudAccessRolesForAzureRoleResponse401
from ...models.get_cloud_access_roles_for_azure_role_response_403 import GetCloudAccessRolesForAzureRoleResponse403
from ...models.get_cloud_access_roles_for_azure_role_response_404 import GetCloudAccessRolesForAzureRoleResponse404
from ...models.get_cloud_access_roles_for_azure_role_response_500 import GetCloudAccessRolesForAzureRoleResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/azure-role/{id}/cloud-access-role".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetCloudAccessRolesForAzureRoleResponse200 | GetCloudAccessRolesForAzureRoleResponse401 | GetCloudAccessRolesForAzureRoleResponse403 | GetCloudAccessRolesForAzureRoleResponse404 | GetCloudAccessRolesForAzureRoleResponse500 | None:
    if response.status_code == 200:
        response_200 = GetCloudAccessRolesForAzureRoleResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetCloudAccessRolesForAzureRoleResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetCloudAccessRolesForAzureRoleResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetCloudAccessRolesForAzureRoleResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetCloudAccessRolesForAzureRoleResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetCloudAccessRolesForAzureRoleResponse200 | GetCloudAccessRolesForAzureRoleResponse401 | GetCloudAccessRolesForAzureRoleResponse403 | GetCloudAccessRolesForAzureRoleResponse404 | GetCloudAccessRolesForAzureRoleResponse500]:
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

) -> Response[GetCloudAccessRolesForAzureRoleResponse200 | GetCloudAccessRolesForAzureRoleResponse401 | GetCloudAccessRolesForAzureRoleResponse403 | GetCloudAccessRolesForAzureRoleResponse404 | GetCloudAccessRolesForAzureRoleResponse500]:
    """ Returns a list of Cloud Access Roles that are attached to an Azure Role.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCloudAccessRolesForAzureRoleResponse200 | GetCloudAccessRolesForAzureRoleResponse401 | GetCloudAccessRolesForAzureRoleResponse403 | GetCloudAccessRolesForAzureRoleResponse404 | GetCloudAccessRolesForAzureRoleResponse500]
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

) -> GetCloudAccessRolesForAzureRoleResponse200 | GetCloudAccessRolesForAzureRoleResponse401 | GetCloudAccessRolesForAzureRoleResponse403 | GetCloudAccessRolesForAzureRoleResponse404 | GetCloudAccessRolesForAzureRoleResponse500 | None:
    """ Returns a list of Cloud Access Roles that are attached to an Azure Role.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCloudAccessRolesForAzureRoleResponse200 | GetCloudAccessRolesForAzureRoleResponse401 | GetCloudAccessRolesForAzureRoleResponse403 | GetCloudAccessRolesForAzureRoleResponse404 | GetCloudAccessRolesForAzureRoleResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetCloudAccessRolesForAzureRoleResponse200 | GetCloudAccessRolesForAzureRoleResponse401 | GetCloudAccessRolesForAzureRoleResponse403 | GetCloudAccessRolesForAzureRoleResponse404 | GetCloudAccessRolesForAzureRoleResponse500]:
    """ Returns a list of Cloud Access Roles that are attached to an Azure Role.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCloudAccessRolesForAzureRoleResponse200 | GetCloudAccessRolesForAzureRoleResponse401 | GetCloudAccessRolesForAzureRoleResponse403 | GetCloudAccessRolesForAzureRoleResponse404 | GetCloudAccessRolesForAzureRoleResponse500]
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

) -> GetCloudAccessRolesForAzureRoleResponse200 | GetCloudAccessRolesForAzureRoleResponse401 | GetCloudAccessRolesForAzureRoleResponse403 | GetCloudAccessRolesForAzureRoleResponse404 | GetCloudAccessRolesForAzureRoleResponse500 | None:
    """ Returns a list of Cloud Access Roles that are attached to an Azure Role.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCloudAccessRolesForAzureRoleResponse200 | GetCloudAccessRolesForAzureRoleResponse401 | GetCloudAccessRolesForAzureRoleResponse403 | GetCloudAccessRolesForAzureRoleResponse404 | GetCloudAccessRolesForAzureRoleResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
