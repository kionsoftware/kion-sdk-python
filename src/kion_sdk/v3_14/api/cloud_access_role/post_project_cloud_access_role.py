from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_project_cloud_access_role_response_201 import PostProjectCloudAccessRoleResponse201
from ...models.post_project_cloud_access_role_response_400 import PostProjectCloudAccessRoleResponse400
from ...models.post_project_cloud_access_role_response_401 import PostProjectCloudAccessRoleResponse401
from ...models.post_project_cloud_access_role_response_403 import PostProjectCloudAccessRoleResponse403
from ...models.post_project_cloud_access_role_response_422 import PostProjectCloudAccessRoleResponse422
from ...models.post_project_cloud_access_role_response_500 import PostProjectCloudAccessRoleResponse500
from ...models.project_cloud_access_role_create import ProjectCloudAccessRoleCreate
from typing import cast



def _get_kwargs(
    *,
    body: ProjectCloudAccessRoleCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/project-cloud-access-role",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostProjectCloudAccessRoleResponse201 | PostProjectCloudAccessRoleResponse400 | PostProjectCloudAccessRoleResponse401 | PostProjectCloudAccessRoleResponse403 | PostProjectCloudAccessRoleResponse422 | PostProjectCloudAccessRoleResponse500 | None:
    if response.status_code == 201:
        response_201 = PostProjectCloudAccessRoleResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostProjectCloudAccessRoleResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostProjectCloudAccessRoleResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostProjectCloudAccessRoleResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostProjectCloudAccessRoleResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostProjectCloudAccessRoleResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostProjectCloudAccessRoleResponse201 | PostProjectCloudAccessRoleResponse400 | PostProjectCloudAccessRoleResponse401 | PostProjectCloudAccessRoleResponse403 | PostProjectCloudAccessRoleResponse422 | PostProjectCloudAccessRoleResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ProjectCloudAccessRoleCreate,

) -> Response[PostProjectCloudAccessRoleResponse201 | PostProjectCloudAccessRoleResponse400 | PostProjectCloudAccessRoleResponse401 | PostProjectCloudAccessRoleResponse403 | PostProjectCloudAccessRoleResponse422 | PostProjectCloudAccessRoleResponse500]:
    """  Creates a project cloud access role in the application. Provided cloud provider IDs will be used to
    enforce
    that provided accounts, policies, and other entities are specific to the CSP.

    Args:
        body (ProjectCloudAccessRoleCreate): ProjectCloudAccessRoleCreate defines the json
            structure for the project cloud access role's create action.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostProjectCloudAccessRoleResponse201 | PostProjectCloudAccessRoleResponse400 | PostProjectCloudAccessRoleResponse401 | PostProjectCloudAccessRoleResponse403 | PostProjectCloudAccessRoleResponse422 | PostProjectCloudAccessRoleResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: ProjectCloudAccessRoleCreate,

) -> PostProjectCloudAccessRoleResponse201 | PostProjectCloudAccessRoleResponse400 | PostProjectCloudAccessRoleResponse401 | PostProjectCloudAccessRoleResponse403 | PostProjectCloudAccessRoleResponse422 | PostProjectCloudAccessRoleResponse500 | None:
    """  Creates a project cloud access role in the application. Provided cloud provider IDs will be used to
    enforce
    that provided accounts, policies, and other entities are specific to the CSP.

    Args:
        body (ProjectCloudAccessRoleCreate): ProjectCloudAccessRoleCreate defines the json
            structure for the project cloud access role's create action.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostProjectCloudAccessRoleResponse201 | PostProjectCloudAccessRoleResponse400 | PostProjectCloudAccessRoleResponse401 | PostProjectCloudAccessRoleResponse403 | PostProjectCloudAccessRoleResponse422 | PostProjectCloudAccessRoleResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ProjectCloudAccessRoleCreate,

) -> Response[PostProjectCloudAccessRoleResponse201 | PostProjectCloudAccessRoleResponse400 | PostProjectCloudAccessRoleResponse401 | PostProjectCloudAccessRoleResponse403 | PostProjectCloudAccessRoleResponse422 | PostProjectCloudAccessRoleResponse500]:
    """  Creates a project cloud access role in the application. Provided cloud provider IDs will be used to
    enforce
    that provided accounts, policies, and other entities are specific to the CSP.

    Args:
        body (ProjectCloudAccessRoleCreate): ProjectCloudAccessRoleCreate defines the json
            structure for the project cloud access role's create action.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostProjectCloudAccessRoleResponse201 | PostProjectCloudAccessRoleResponse400 | PostProjectCloudAccessRoleResponse401 | PostProjectCloudAccessRoleResponse403 | PostProjectCloudAccessRoleResponse422 | PostProjectCloudAccessRoleResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ProjectCloudAccessRoleCreate,

) -> PostProjectCloudAccessRoleResponse201 | PostProjectCloudAccessRoleResponse400 | PostProjectCloudAccessRoleResponse401 | PostProjectCloudAccessRoleResponse403 | PostProjectCloudAccessRoleResponse422 | PostProjectCloudAccessRoleResponse500 | None:
    """  Creates a project cloud access role in the application. Provided cloud provider IDs will be used to
    enforce
    that provided accounts, policies, and other entities are specific to the CSP.

    Args:
        body (ProjectCloudAccessRoleCreate): ProjectCloudAccessRoleCreate defines the json
            structure for the project cloud access role's create action.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostProjectCloudAccessRoleResponse201 | PostProjectCloudAccessRoleResponse400 | PostProjectCloudAccessRoleResponse401 | PostProjectCloudAccessRoleResponse403 | PostProjectCloudAccessRoleResponse422 | PostProjectCloudAccessRoleResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
