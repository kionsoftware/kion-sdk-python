from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.ou_cloud_access_role_update import OUCloudAccessRoleUpdate
from ...models.patch_ou_cloud_access_role_response_201 import PatchOUCloudAccessRoleResponse201
from ...models.patch_ou_cloud_access_role_response_400 import PatchOUCloudAccessRoleResponse400
from ...models.patch_ou_cloud_access_role_response_401 import PatchOUCloudAccessRoleResponse401
from ...models.patch_ou_cloud_access_role_response_403 import PatchOUCloudAccessRoleResponse403
from ...models.patch_ou_cloud_access_role_response_422 import PatchOUCloudAccessRoleResponse422
from ...models.patch_ou_cloud_access_role_response_500 import PatchOUCloudAccessRoleResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: OUCloudAccessRoleUpdate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/ou-cloud-access-role/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchOUCloudAccessRoleResponse201 | PatchOUCloudAccessRoleResponse400 | PatchOUCloudAccessRoleResponse401 | PatchOUCloudAccessRoleResponse403 | PatchOUCloudAccessRoleResponse422 | PatchOUCloudAccessRoleResponse500 | None:
    if response.status_code == 201:
        response_201 = PatchOUCloudAccessRoleResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PatchOUCloudAccessRoleResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchOUCloudAccessRoleResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchOUCloudAccessRoleResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PatchOUCloudAccessRoleResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchOUCloudAccessRoleResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchOUCloudAccessRoleResponse201 | PatchOUCloudAccessRoleResponse400 | PatchOUCloudAccessRoleResponse401 | PatchOUCloudAccessRoleResponse403 | PatchOUCloudAccessRoleResponse422 | PatchOUCloudAccessRoleResponse500]:
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
    body: OUCloudAccessRoleUpdate,

) -> Response[PatchOUCloudAccessRoleResponse201 | PatchOUCloudAccessRoleResponse400 | PatchOUCloudAccessRoleResponse401 | PatchOUCloudAccessRoleResponse403 | PatchOUCloudAccessRoleResponse422 | PatchOUCloudAccessRoleResponse500]:
    """ Updates an ou cloud access role in the application.

    Args:
        id (int):
        body (OUCloudAccessRoleUpdate): OUCloudAccessRoleUpdate defines an updatable cloud access
            role for an ou.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchOUCloudAccessRoleResponse201 | PatchOUCloudAccessRoleResponse400 | PatchOUCloudAccessRoleResponse401 | PatchOUCloudAccessRoleResponse403 | PatchOUCloudAccessRoleResponse422 | PatchOUCloudAccessRoleResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: OUCloudAccessRoleUpdate,

) -> PatchOUCloudAccessRoleResponse201 | PatchOUCloudAccessRoleResponse400 | PatchOUCloudAccessRoleResponse401 | PatchOUCloudAccessRoleResponse403 | PatchOUCloudAccessRoleResponse422 | PatchOUCloudAccessRoleResponse500 | None:
    """ Updates an ou cloud access role in the application.

    Args:
        id (int):
        body (OUCloudAccessRoleUpdate): OUCloudAccessRoleUpdate defines an updatable cloud access
            role for an ou.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchOUCloudAccessRoleResponse201 | PatchOUCloudAccessRoleResponse400 | PatchOUCloudAccessRoleResponse401 | PatchOUCloudAccessRoleResponse403 | PatchOUCloudAccessRoleResponse422 | PatchOUCloudAccessRoleResponse500
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: OUCloudAccessRoleUpdate,

) -> Response[PatchOUCloudAccessRoleResponse201 | PatchOUCloudAccessRoleResponse400 | PatchOUCloudAccessRoleResponse401 | PatchOUCloudAccessRoleResponse403 | PatchOUCloudAccessRoleResponse422 | PatchOUCloudAccessRoleResponse500]:
    """ Updates an ou cloud access role in the application.

    Args:
        id (int):
        body (OUCloudAccessRoleUpdate): OUCloudAccessRoleUpdate defines an updatable cloud access
            role for an ou.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchOUCloudAccessRoleResponse201 | PatchOUCloudAccessRoleResponse400 | PatchOUCloudAccessRoleResponse401 | PatchOUCloudAccessRoleResponse403 | PatchOUCloudAccessRoleResponse422 | PatchOUCloudAccessRoleResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: OUCloudAccessRoleUpdate,

) -> PatchOUCloudAccessRoleResponse201 | PatchOUCloudAccessRoleResponse400 | PatchOUCloudAccessRoleResponse401 | PatchOUCloudAccessRoleResponse403 | PatchOUCloudAccessRoleResponse422 | PatchOUCloudAccessRoleResponse500 | None:
    """ Updates an ou cloud access role in the application.

    Args:
        id (int):
        body (OUCloudAccessRoleUpdate): OUCloudAccessRoleUpdate defines an updatable cloud access
            role for an ou.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchOUCloudAccessRoleResponse201 | PatchOUCloudAccessRoleResponse400 | PatchOUCloudAccessRoleResponse401 | PatchOUCloudAccessRoleResponse403 | PatchOUCloudAccessRoleResponse422 | PatchOUCloudAccessRoleResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
