from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.patch_project_cloud_access_role_response_201 import PatchProjectCloudAccessRoleResponse201
from ...models.patch_project_cloud_access_role_response_400 import PatchProjectCloudAccessRoleResponse400
from ...models.patch_project_cloud_access_role_response_401 import PatchProjectCloudAccessRoleResponse401
from ...models.patch_project_cloud_access_role_response_403 import PatchProjectCloudAccessRoleResponse403
from ...models.patch_project_cloud_access_role_response_422 import PatchProjectCloudAccessRoleResponse422
from ...models.patch_project_cloud_access_role_response_500 import PatchProjectCloudAccessRoleResponse500
from ...models.project_cloud_access_role_update import ProjectCloudAccessRoleUpdate
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: ProjectCloudAccessRoleUpdate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/project-cloud-access-role/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchProjectCloudAccessRoleResponse201 | PatchProjectCloudAccessRoleResponse400 | PatchProjectCloudAccessRoleResponse401 | PatchProjectCloudAccessRoleResponse403 | PatchProjectCloudAccessRoleResponse422 | PatchProjectCloudAccessRoleResponse500 | None:
    if response.status_code == 201:
        response_201 = PatchProjectCloudAccessRoleResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PatchProjectCloudAccessRoleResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchProjectCloudAccessRoleResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchProjectCloudAccessRoleResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PatchProjectCloudAccessRoleResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchProjectCloudAccessRoleResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchProjectCloudAccessRoleResponse201 | PatchProjectCloudAccessRoleResponse400 | PatchProjectCloudAccessRoleResponse401 | PatchProjectCloudAccessRoleResponse403 | PatchProjectCloudAccessRoleResponse422 | PatchProjectCloudAccessRoleResponse500]:
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
    body: ProjectCloudAccessRoleUpdate,

) -> Response[PatchProjectCloudAccessRoleResponse201 | PatchProjectCloudAccessRoleResponse400 | PatchProjectCloudAccessRoleResponse401 | PatchProjectCloudAccessRoleResponse403 | PatchProjectCloudAccessRoleResponse422 | PatchProjectCloudAccessRoleResponse500]:
    """ Updates a project cloud access role in the application.

     For non-User CAR types (Custom Trust, Account, Service), per-type trust
    fields may be updated (`aws_iam_role_trust_policy`, `aws_trusted_account_numbers`,
    `aws_trusted_services`). The CAR type itself is not mutable via update.
    `web_access`, `short_term_access_keys`, and `long_term_access_keys` remain
    forced to false for non-User types.

    Args:
        id (int):
        body (ProjectCloudAccessRoleUpdate): ProjectCloudAccessRoleUpdate defines the json
            structure for the project cloud access role's update action.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchProjectCloudAccessRoleResponse201 | PatchProjectCloudAccessRoleResponse400 | PatchProjectCloudAccessRoleResponse401 | PatchProjectCloudAccessRoleResponse403 | PatchProjectCloudAccessRoleResponse422 | PatchProjectCloudAccessRoleResponse500]
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
    body: ProjectCloudAccessRoleUpdate,

) -> PatchProjectCloudAccessRoleResponse201 | PatchProjectCloudAccessRoleResponse400 | PatchProjectCloudAccessRoleResponse401 | PatchProjectCloudAccessRoleResponse403 | PatchProjectCloudAccessRoleResponse422 | PatchProjectCloudAccessRoleResponse500 | None:
    """ Updates a project cloud access role in the application.

     For non-User CAR types (Custom Trust, Account, Service), per-type trust
    fields may be updated (`aws_iam_role_trust_policy`, `aws_trusted_account_numbers`,
    `aws_trusted_services`). The CAR type itself is not mutable via update.
    `web_access`, `short_term_access_keys`, and `long_term_access_keys` remain
    forced to false for non-User types.

    Args:
        id (int):
        body (ProjectCloudAccessRoleUpdate): ProjectCloudAccessRoleUpdate defines the json
            structure for the project cloud access role's update action.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchProjectCloudAccessRoleResponse201 | PatchProjectCloudAccessRoleResponse400 | PatchProjectCloudAccessRoleResponse401 | PatchProjectCloudAccessRoleResponse403 | PatchProjectCloudAccessRoleResponse422 | PatchProjectCloudAccessRoleResponse500
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
    body: ProjectCloudAccessRoleUpdate,

) -> Response[PatchProjectCloudAccessRoleResponse201 | PatchProjectCloudAccessRoleResponse400 | PatchProjectCloudAccessRoleResponse401 | PatchProjectCloudAccessRoleResponse403 | PatchProjectCloudAccessRoleResponse422 | PatchProjectCloudAccessRoleResponse500]:
    """ Updates a project cloud access role in the application.

     For non-User CAR types (Custom Trust, Account, Service), per-type trust
    fields may be updated (`aws_iam_role_trust_policy`, `aws_trusted_account_numbers`,
    `aws_trusted_services`). The CAR type itself is not mutable via update.
    `web_access`, `short_term_access_keys`, and `long_term_access_keys` remain
    forced to false for non-User types.

    Args:
        id (int):
        body (ProjectCloudAccessRoleUpdate): ProjectCloudAccessRoleUpdate defines the json
            structure for the project cloud access role's update action.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchProjectCloudAccessRoleResponse201 | PatchProjectCloudAccessRoleResponse400 | PatchProjectCloudAccessRoleResponse401 | PatchProjectCloudAccessRoleResponse403 | PatchProjectCloudAccessRoleResponse422 | PatchProjectCloudAccessRoleResponse500]
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
    body: ProjectCloudAccessRoleUpdate,

) -> PatchProjectCloudAccessRoleResponse201 | PatchProjectCloudAccessRoleResponse400 | PatchProjectCloudAccessRoleResponse401 | PatchProjectCloudAccessRoleResponse403 | PatchProjectCloudAccessRoleResponse422 | PatchProjectCloudAccessRoleResponse500 | None:
    """ Updates a project cloud access role in the application.

     For non-User CAR types (Custom Trust, Account, Service), per-type trust
    fields may be updated (`aws_iam_role_trust_policy`, `aws_trusted_account_numbers`,
    `aws_trusted_services`). The CAR type itself is not mutable via update.
    `web_access`, `short_term_access_keys`, and `long_term_access_keys` remain
    forced to false for non-User types.

    Args:
        id (int):
        body (ProjectCloudAccessRoleUpdate): ProjectCloudAccessRoleUpdate defines the json
            structure for the project cloud access role's update action.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchProjectCloudAccessRoleResponse201 | PatchProjectCloudAccessRoleResponse400 | PatchProjectCloudAccessRoleResponse401 | PatchProjectCloudAccessRoleResponse403 | PatchProjectCloudAccessRoleResponse422 | PatchProjectCloudAccessRoleResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
