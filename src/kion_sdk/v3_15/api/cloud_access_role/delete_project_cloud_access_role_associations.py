from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_project_cloud_access_role_associations_response_200 import DeleteProjectCloudAccessRoleAssociationsResponse200
from ...models.delete_project_cloud_access_role_associations_response_400 import DeleteProjectCloudAccessRoleAssociationsResponse400
from ...models.delete_project_cloud_access_role_associations_response_401 import DeleteProjectCloudAccessRoleAssociationsResponse401
from ...models.delete_project_cloud_access_role_associations_response_403 import DeleteProjectCloudAccessRoleAssociationsResponse403
from ...models.delete_project_cloud_access_role_associations_response_404 import DeleteProjectCloudAccessRoleAssociationsResponse404
from ...models.delete_project_cloud_access_role_associations_response_422 import DeleteProjectCloudAccessRoleAssociationsResponse422
from ...models.delete_project_cloud_access_role_associations_response_500 import DeleteProjectCloudAccessRoleAssociationsResponse500
from ...models.project_cloud_access_role_associations import ProjectCloudAccessRoleAssociations
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: ProjectCloudAccessRoleAssociations,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/project-cloud-access-role/{id}/association".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteProjectCloudAccessRoleAssociationsResponse200 | DeleteProjectCloudAccessRoleAssociationsResponse400 | DeleteProjectCloudAccessRoleAssociationsResponse401 | DeleteProjectCloudAccessRoleAssociationsResponse403 | DeleteProjectCloudAccessRoleAssociationsResponse404 | DeleteProjectCloudAccessRoleAssociationsResponse422 | DeleteProjectCloudAccessRoleAssociationsResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteProjectCloudAccessRoleAssociationsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DeleteProjectCloudAccessRoleAssociationsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteProjectCloudAccessRoleAssociationsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteProjectCloudAccessRoleAssociationsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteProjectCloudAccessRoleAssociationsResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = DeleteProjectCloudAccessRoleAssociationsResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = DeleteProjectCloudAccessRoleAssociationsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteProjectCloudAccessRoleAssociationsResponse200 | DeleteProjectCloudAccessRoleAssociationsResponse400 | DeleteProjectCloudAccessRoleAssociationsResponse401 | DeleteProjectCloudAccessRoleAssociationsResponse403 | DeleteProjectCloudAccessRoleAssociationsResponse404 | DeleteProjectCloudAccessRoleAssociationsResponse422 | DeleteProjectCloudAccessRoleAssociationsResponse500]:
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
    body: ProjectCloudAccessRoleAssociations,

) -> Response[DeleteProjectCloudAccessRoleAssociationsResponse200 | DeleteProjectCloudAccessRoleAssociationsResponse400 | DeleteProjectCloudAccessRoleAssociationsResponse401 | DeleteProjectCloudAccessRoleAssociationsResponse403 | DeleteProjectCloudAccessRoleAssociationsResponse404 | DeleteProjectCloudAccessRoleAssociationsResponse422 | DeleteProjectCloudAccessRoleAssociationsResponse500]:
    """ Removes associations to a cloud access role in the application.

     For non-User CAR types, only AWS IAM policy associations are accepted.
    Requests that include user, user group, Azure, or GCP associations are rejected.

    Args:
        id (int):
        body (ProjectCloudAccessRoleAssociations): ProjectCloudAccessRoleAssociations defines the
            json structure for the project cloud access role's create action.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteProjectCloudAccessRoleAssociationsResponse200 | DeleteProjectCloudAccessRoleAssociationsResponse400 | DeleteProjectCloudAccessRoleAssociationsResponse401 | DeleteProjectCloudAccessRoleAssociationsResponse403 | DeleteProjectCloudAccessRoleAssociationsResponse404 | DeleteProjectCloudAccessRoleAssociationsResponse422 | DeleteProjectCloudAccessRoleAssociationsResponse500]
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
    body: ProjectCloudAccessRoleAssociations,

) -> DeleteProjectCloudAccessRoleAssociationsResponse200 | DeleteProjectCloudAccessRoleAssociationsResponse400 | DeleteProjectCloudAccessRoleAssociationsResponse401 | DeleteProjectCloudAccessRoleAssociationsResponse403 | DeleteProjectCloudAccessRoleAssociationsResponse404 | DeleteProjectCloudAccessRoleAssociationsResponse422 | DeleteProjectCloudAccessRoleAssociationsResponse500 | None:
    """ Removes associations to a cloud access role in the application.

     For non-User CAR types, only AWS IAM policy associations are accepted.
    Requests that include user, user group, Azure, or GCP associations are rejected.

    Args:
        id (int):
        body (ProjectCloudAccessRoleAssociations): ProjectCloudAccessRoleAssociations defines the
            json structure for the project cloud access role's create action.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteProjectCloudAccessRoleAssociationsResponse200 | DeleteProjectCloudAccessRoleAssociationsResponse400 | DeleteProjectCloudAccessRoleAssociationsResponse401 | DeleteProjectCloudAccessRoleAssociationsResponse403 | DeleteProjectCloudAccessRoleAssociationsResponse404 | DeleteProjectCloudAccessRoleAssociationsResponse422 | DeleteProjectCloudAccessRoleAssociationsResponse500
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
    body: ProjectCloudAccessRoleAssociations,

) -> Response[DeleteProjectCloudAccessRoleAssociationsResponse200 | DeleteProjectCloudAccessRoleAssociationsResponse400 | DeleteProjectCloudAccessRoleAssociationsResponse401 | DeleteProjectCloudAccessRoleAssociationsResponse403 | DeleteProjectCloudAccessRoleAssociationsResponse404 | DeleteProjectCloudAccessRoleAssociationsResponse422 | DeleteProjectCloudAccessRoleAssociationsResponse500]:
    """ Removes associations to a cloud access role in the application.

     For non-User CAR types, only AWS IAM policy associations are accepted.
    Requests that include user, user group, Azure, or GCP associations are rejected.

    Args:
        id (int):
        body (ProjectCloudAccessRoleAssociations): ProjectCloudAccessRoleAssociations defines the
            json structure for the project cloud access role's create action.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteProjectCloudAccessRoleAssociationsResponse200 | DeleteProjectCloudAccessRoleAssociationsResponse400 | DeleteProjectCloudAccessRoleAssociationsResponse401 | DeleteProjectCloudAccessRoleAssociationsResponse403 | DeleteProjectCloudAccessRoleAssociationsResponse404 | DeleteProjectCloudAccessRoleAssociationsResponse422 | DeleteProjectCloudAccessRoleAssociationsResponse500]
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
    body: ProjectCloudAccessRoleAssociations,

) -> DeleteProjectCloudAccessRoleAssociationsResponse200 | DeleteProjectCloudAccessRoleAssociationsResponse400 | DeleteProjectCloudAccessRoleAssociationsResponse401 | DeleteProjectCloudAccessRoleAssociationsResponse403 | DeleteProjectCloudAccessRoleAssociationsResponse404 | DeleteProjectCloudAccessRoleAssociationsResponse422 | DeleteProjectCloudAccessRoleAssociationsResponse500 | None:
    """ Removes associations to a cloud access role in the application.

     For non-User CAR types, only AWS IAM policy associations are accepted.
    Requests that include user, user group, Azure, or GCP associations are rejected.

    Args:
        id (int):
        body (ProjectCloudAccessRoleAssociations): ProjectCloudAccessRoleAssociations defines the
            json structure for the project cloud access role's create action.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteProjectCloudAccessRoleAssociationsResponse200 | DeleteProjectCloudAccessRoleAssociationsResponse400 | DeleteProjectCloudAccessRoleAssociationsResponse401 | DeleteProjectCloudAccessRoleAssociationsResponse403 | DeleteProjectCloudAccessRoleAssociationsResponse404 | DeleteProjectCloudAccessRoleAssociationsResponse422 | DeleteProjectCloudAccessRoleAssociationsResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
