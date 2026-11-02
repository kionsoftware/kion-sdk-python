from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_project_cloud_access_role_response_200 import GetProjectCloudAccessRoleResponse200
from ...models.get_project_cloud_access_role_response_401 import GetProjectCloudAccessRoleResponse401
from ...models.get_project_cloud_access_role_response_403 import GetProjectCloudAccessRoleResponse403
from ...models.get_project_cloud_access_role_response_404 import GetProjectCloudAccessRoleResponse404
from ...models.get_project_cloud_access_role_response_500 import GetProjectCloudAccessRoleResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    policy_type: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["policy-type"] = policy_type


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/project-cloud-access-role/{id}".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetProjectCloudAccessRoleResponse200 | GetProjectCloudAccessRoleResponse401 | GetProjectCloudAccessRoleResponse403 | GetProjectCloudAccessRoleResponse404 | GetProjectCloudAccessRoleResponse500 | None:
    if response.status_code == 200:
        response_200 = GetProjectCloudAccessRoleResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetProjectCloudAccessRoleResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetProjectCloudAccessRoleResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetProjectCloudAccessRoleResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetProjectCloudAccessRoleResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetProjectCloudAccessRoleResponse200 | GetProjectCloudAccessRoleResponse401 | GetProjectCloudAccessRoleResponse403 | GetProjectCloudAccessRoleResponse404 | GetProjectCloudAccessRoleResponse500]:
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
    policy_type: str | Unset = UNSET,

) -> Response[GetProjectCloudAccessRoleResponse200 | GetProjectCloudAccessRoleResponse401 | GetProjectCloudAccessRoleResponse403 | GetProjectCloudAccessRoleResponse404 | GetProjectCloudAccessRoleResponse500]:
    """ Finds a project cloud access role by ID in the application.

    Args:
        id (int):
        policy_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProjectCloudAccessRoleResponse200 | GetProjectCloudAccessRoleResponse401 | GetProjectCloudAccessRoleResponse403 | GetProjectCloudAccessRoleResponse404 | GetProjectCloudAccessRoleResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
policy_type=policy_type,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    policy_type: str | Unset = UNSET,

) -> GetProjectCloudAccessRoleResponse200 | GetProjectCloudAccessRoleResponse401 | GetProjectCloudAccessRoleResponse403 | GetProjectCloudAccessRoleResponse404 | GetProjectCloudAccessRoleResponse500 | None:
    """ Finds a project cloud access role by ID in the application.

    Args:
        id (int):
        policy_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProjectCloudAccessRoleResponse200 | GetProjectCloudAccessRoleResponse401 | GetProjectCloudAccessRoleResponse403 | GetProjectCloudAccessRoleResponse404 | GetProjectCloudAccessRoleResponse500
     """


    return sync_detailed(
        id=id,
client=client,
policy_type=policy_type,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    policy_type: str | Unset = UNSET,

) -> Response[GetProjectCloudAccessRoleResponse200 | GetProjectCloudAccessRoleResponse401 | GetProjectCloudAccessRoleResponse403 | GetProjectCloudAccessRoleResponse404 | GetProjectCloudAccessRoleResponse500]:
    """ Finds a project cloud access role by ID in the application.

    Args:
        id (int):
        policy_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProjectCloudAccessRoleResponse200 | GetProjectCloudAccessRoleResponse401 | GetProjectCloudAccessRoleResponse403 | GetProjectCloudAccessRoleResponse404 | GetProjectCloudAccessRoleResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
policy_type=policy_type,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    policy_type: str | Unset = UNSET,

) -> GetProjectCloudAccessRoleResponse200 | GetProjectCloudAccessRoleResponse401 | GetProjectCloudAccessRoleResponse403 | GetProjectCloudAccessRoleResponse404 | GetProjectCloudAccessRoleResponse500 | None:
    """ Finds a project cloud access role by ID in the application.

    Args:
        id (int):
        policy_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProjectCloudAccessRoleResponse200 | GetProjectCloudAccessRoleResponse401 | GetProjectCloudAccessRoleResponse403 | GetProjectCloudAccessRoleResponse404 | GetProjectCloudAccessRoleResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
policy_type=policy_type,

    )).parsed
