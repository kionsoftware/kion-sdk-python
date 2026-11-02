from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_ou_cloud_access_role_response_200 import DeleteOUCloudAccessRoleResponse200
from ...models.delete_ou_cloud_access_role_response_400 import DeleteOUCloudAccessRoleResponse400
from ...models.delete_ou_cloud_access_role_response_401 import DeleteOUCloudAccessRoleResponse401
from ...models.delete_ou_cloud_access_role_response_403 import DeleteOUCloudAccessRoleResponse403
from ...models.delete_ou_cloud_access_role_response_404 import DeleteOUCloudAccessRoleResponse404
from ...models.delete_ou_cloud_access_role_response_500 import DeleteOUCloudAccessRoleResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/ou-cloud-access-role/{id}".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteOUCloudAccessRoleResponse200 | DeleteOUCloudAccessRoleResponse400 | DeleteOUCloudAccessRoleResponse401 | DeleteOUCloudAccessRoleResponse403 | DeleteOUCloudAccessRoleResponse404 | DeleteOUCloudAccessRoleResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteOUCloudAccessRoleResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DeleteOUCloudAccessRoleResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteOUCloudAccessRoleResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteOUCloudAccessRoleResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteOUCloudAccessRoleResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = DeleteOUCloudAccessRoleResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteOUCloudAccessRoleResponse200 | DeleteOUCloudAccessRoleResponse400 | DeleteOUCloudAccessRoleResponse401 | DeleteOUCloudAccessRoleResponse403 | DeleteOUCloudAccessRoleResponse404 | DeleteOUCloudAccessRoleResponse500]:
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

) -> Response[DeleteOUCloudAccessRoleResponse200 | DeleteOUCloudAccessRoleResponse400 | DeleteOUCloudAccessRoleResponse401 | DeleteOUCloudAccessRoleResponse403 | DeleteOUCloudAccessRoleResponse404 | DeleteOUCloudAccessRoleResponse500]:
    """ Deletes the OU Cloud Access Role.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteOUCloudAccessRoleResponse200 | DeleteOUCloudAccessRoleResponse400 | DeleteOUCloudAccessRoleResponse401 | DeleteOUCloudAccessRoleResponse403 | DeleteOUCloudAccessRoleResponse404 | DeleteOUCloudAccessRoleResponse500]
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

) -> DeleteOUCloudAccessRoleResponse200 | DeleteOUCloudAccessRoleResponse400 | DeleteOUCloudAccessRoleResponse401 | DeleteOUCloudAccessRoleResponse403 | DeleteOUCloudAccessRoleResponse404 | DeleteOUCloudAccessRoleResponse500 | None:
    """ Deletes the OU Cloud Access Role.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteOUCloudAccessRoleResponse200 | DeleteOUCloudAccessRoleResponse400 | DeleteOUCloudAccessRoleResponse401 | DeleteOUCloudAccessRoleResponse403 | DeleteOUCloudAccessRoleResponse404 | DeleteOUCloudAccessRoleResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteOUCloudAccessRoleResponse200 | DeleteOUCloudAccessRoleResponse400 | DeleteOUCloudAccessRoleResponse401 | DeleteOUCloudAccessRoleResponse403 | DeleteOUCloudAccessRoleResponse404 | DeleteOUCloudAccessRoleResponse500]:
    """ Deletes the OU Cloud Access Role.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteOUCloudAccessRoleResponse200 | DeleteOUCloudAccessRoleResponse400 | DeleteOUCloudAccessRoleResponse401 | DeleteOUCloudAccessRoleResponse403 | DeleteOUCloudAccessRoleResponse404 | DeleteOUCloudAccessRoleResponse500]
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

) -> DeleteOUCloudAccessRoleResponse200 | DeleteOUCloudAccessRoleResponse400 | DeleteOUCloudAccessRoleResponse401 | DeleteOUCloudAccessRoleResponse403 | DeleteOUCloudAccessRoleResponse404 | DeleteOUCloudAccessRoleResponse500 | None:
    """ Deletes the OU Cloud Access Role.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteOUCloudAccessRoleResponse200 | DeleteOUCloudAccessRoleResponse400 | DeleteOUCloudAccessRoleResponse401 | DeleteOUCloudAccessRoleResponse403 | DeleteOUCloudAccessRoleResponse404 | DeleteOUCloudAccessRoleResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
