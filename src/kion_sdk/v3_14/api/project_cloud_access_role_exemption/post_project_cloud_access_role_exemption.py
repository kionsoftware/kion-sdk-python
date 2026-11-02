from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_project_cloud_access_role_exemption_response_201 import PostProjectCloudAccessRoleExemptionResponse201
from ...models.post_project_cloud_access_role_exemption_response_400 import PostProjectCloudAccessRoleExemptionResponse400
from ...models.post_project_cloud_access_role_exemption_response_401 import PostProjectCloudAccessRoleExemptionResponse401
from ...models.post_project_cloud_access_role_exemption_response_403 import PostProjectCloudAccessRoleExemptionResponse403
from ...models.post_project_cloud_access_role_exemption_response_422 import PostProjectCloudAccessRoleExemptionResponse422
from ...models.post_project_cloud_access_role_exemption_response_500 import PostProjectCloudAccessRoleExemptionResponse500
from ...models.project_cloud_access_role_exemption import ProjectCloudAccessRoleExemption
from typing import cast



def _get_kwargs(
    *,
    body: ProjectCloudAccessRoleExemption,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/project-cloud-access-role-exemption",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostProjectCloudAccessRoleExemptionResponse201 | PostProjectCloudAccessRoleExemptionResponse400 | PostProjectCloudAccessRoleExemptionResponse401 | PostProjectCloudAccessRoleExemptionResponse403 | PostProjectCloudAccessRoleExemptionResponse422 | PostProjectCloudAccessRoleExemptionResponse500 | None:
    if response.status_code == 201:
        response_201 = PostProjectCloudAccessRoleExemptionResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostProjectCloudAccessRoleExemptionResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostProjectCloudAccessRoleExemptionResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostProjectCloudAccessRoleExemptionResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostProjectCloudAccessRoleExemptionResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostProjectCloudAccessRoleExemptionResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostProjectCloudAccessRoleExemptionResponse201 | PostProjectCloudAccessRoleExemptionResponse400 | PostProjectCloudAccessRoleExemptionResponse401 | PostProjectCloudAccessRoleExemptionResponse403 | PostProjectCloudAccessRoleExemptionResponse422 | PostProjectCloudAccessRoleExemptionResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ProjectCloudAccessRoleExemption,

) -> Response[PostProjectCloudAccessRoleExemptionResponse201 | PostProjectCloudAccessRoleExemptionResponse400 | PostProjectCloudAccessRoleExemptionResponse401 | PostProjectCloudAccessRoleExemptionResponse403 | PostProjectCloudAccessRoleExemptionResponse422 | PostProjectCloudAccessRoleExemptionResponse500]:
    """ Exempts a Project from an inherited OU Cloud Access Role.

    Args:
        body (ProjectCloudAccessRoleExemption): ProjectCloudAccessRoleExemption defines an
            exemption of an ou cloud access role for a project.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostProjectCloudAccessRoleExemptionResponse201 | PostProjectCloudAccessRoleExemptionResponse400 | PostProjectCloudAccessRoleExemptionResponse401 | PostProjectCloudAccessRoleExemptionResponse403 | PostProjectCloudAccessRoleExemptionResponse422 | PostProjectCloudAccessRoleExemptionResponse500]
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
    body: ProjectCloudAccessRoleExemption,

) -> PostProjectCloudAccessRoleExemptionResponse201 | PostProjectCloudAccessRoleExemptionResponse400 | PostProjectCloudAccessRoleExemptionResponse401 | PostProjectCloudAccessRoleExemptionResponse403 | PostProjectCloudAccessRoleExemptionResponse422 | PostProjectCloudAccessRoleExemptionResponse500 | None:
    """ Exempts a Project from an inherited OU Cloud Access Role.

    Args:
        body (ProjectCloudAccessRoleExemption): ProjectCloudAccessRoleExemption defines an
            exemption of an ou cloud access role for a project.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostProjectCloudAccessRoleExemptionResponse201 | PostProjectCloudAccessRoleExemptionResponse400 | PostProjectCloudAccessRoleExemptionResponse401 | PostProjectCloudAccessRoleExemptionResponse403 | PostProjectCloudAccessRoleExemptionResponse422 | PostProjectCloudAccessRoleExemptionResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ProjectCloudAccessRoleExemption,

) -> Response[PostProjectCloudAccessRoleExemptionResponse201 | PostProjectCloudAccessRoleExemptionResponse400 | PostProjectCloudAccessRoleExemptionResponse401 | PostProjectCloudAccessRoleExemptionResponse403 | PostProjectCloudAccessRoleExemptionResponse422 | PostProjectCloudAccessRoleExemptionResponse500]:
    """ Exempts a Project from an inherited OU Cloud Access Role.

    Args:
        body (ProjectCloudAccessRoleExemption): ProjectCloudAccessRoleExemption defines an
            exemption of an ou cloud access role for a project.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostProjectCloudAccessRoleExemptionResponse201 | PostProjectCloudAccessRoleExemptionResponse400 | PostProjectCloudAccessRoleExemptionResponse401 | PostProjectCloudAccessRoleExemptionResponse403 | PostProjectCloudAccessRoleExemptionResponse422 | PostProjectCloudAccessRoleExemptionResponse500]
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
    body: ProjectCloudAccessRoleExemption,

) -> PostProjectCloudAccessRoleExemptionResponse201 | PostProjectCloudAccessRoleExemptionResponse400 | PostProjectCloudAccessRoleExemptionResponse401 | PostProjectCloudAccessRoleExemptionResponse403 | PostProjectCloudAccessRoleExemptionResponse422 | PostProjectCloudAccessRoleExemptionResponse500 | None:
    """ Exempts a Project from an inherited OU Cloud Access Role.

    Args:
        body (ProjectCloudAccessRoleExemption): ProjectCloudAccessRoleExemption defines an
            exemption of an ou cloud access role for a project.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostProjectCloudAccessRoleExemptionResponse201 | PostProjectCloudAccessRoleExemptionResponse400 | PostProjectCloudAccessRoleExemptionResponse401 | PostProjectCloudAccessRoleExemptionResponse403 | PostProjectCloudAccessRoleExemptionResponse422 | PostProjectCloudAccessRoleExemptionResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
