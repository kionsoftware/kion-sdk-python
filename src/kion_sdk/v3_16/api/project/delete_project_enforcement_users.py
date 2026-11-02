from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_project_enforcement_users_response_200 import DeleteProjectEnforcementUsersResponse200
from ...models.delete_project_enforcement_users_response_400 import DeleteProjectEnforcementUsersResponse400
from ...models.delete_project_enforcement_users_response_401 import DeleteProjectEnforcementUsersResponse401
from ...models.delete_project_enforcement_users_response_403 import DeleteProjectEnforcementUsersResponse403
from ...models.delete_project_enforcement_users_response_404 import DeleteProjectEnforcementUsersResponse404
from ...models.delete_project_enforcement_users_response_422 import DeleteProjectEnforcementUsersResponse422
from ...models.delete_project_enforcement_users_response_500 import DeleteProjectEnforcementUsersResponse500
from ...models.project_enforcement_users import ProjectEnforcementUsers
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    enforcement_id: int,
    *,
    body: ProjectEnforcementUsers | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/project/{id}/enforcement/{enforcement_id}/user".format(id=quote(str(id), safe=""),enforcement_id=quote(str(enforcement_id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteProjectEnforcementUsersResponse200 | DeleteProjectEnforcementUsersResponse400 | DeleteProjectEnforcementUsersResponse401 | DeleteProjectEnforcementUsersResponse403 | DeleteProjectEnforcementUsersResponse404 | DeleteProjectEnforcementUsersResponse422 | DeleteProjectEnforcementUsersResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteProjectEnforcementUsersResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DeleteProjectEnforcementUsersResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteProjectEnforcementUsersResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteProjectEnforcementUsersResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteProjectEnforcementUsersResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = DeleteProjectEnforcementUsersResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = DeleteProjectEnforcementUsersResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteProjectEnforcementUsersResponse200 | DeleteProjectEnforcementUsersResponse400 | DeleteProjectEnforcementUsersResponse401 | DeleteProjectEnforcementUsersResponse403 | DeleteProjectEnforcementUsersResponse404 | DeleteProjectEnforcementUsersResponse422 | DeleteProjectEnforcementUsersResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    enforcement_id: int,
    *,
    client: AuthenticatedClient,
    body: ProjectEnforcementUsers | Unset = UNSET,

) -> Response[DeleteProjectEnforcementUsersResponse200 | DeleteProjectEnforcementUsersResponse400 | DeleteProjectEnforcementUsersResponse401 | DeleteProjectEnforcementUsersResponse403 | DeleteProjectEnforcementUsersResponse404 | DeleteProjectEnforcementUsersResponse422 | DeleteProjectEnforcementUsersResponse500]:
    """ Removes users and groups from a project enforcement.

    Args:
        id (int):
        enforcement_id (int):
        body (ProjectEnforcementUsers | Unset): ProjectEnforcementUsers .

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteProjectEnforcementUsersResponse200 | DeleteProjectEnforcementUsersResponse400 | DeleteProjectEnforcementUsersResponse401 | DeleteProjectEnforcementUsersResponse403 | DeleteProjectEnforcementUsersResponse404 | DeleteProjectEnforcementUsersResponse422 | DeleteProjectEnforcementUsersResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
enforcement_id=enforcement_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    enforcement_id: int,
    *,
    client: AuthenticatedClient,
    body: ProjectEnforcementUsers | Unset = UNSET,

) -> DeleteProjectEnforcementUsersResponse200 | DeleteProjectEnforcementUsersResponse400 | DeleteProjectEnforcementUsersResponse401 | DeleteProjectEnforcementUsersResponse403 | DeleteProjectEnforcementUsersResponse404 | DeleteProjectEnforcementUsersResponse422 | DeleteProjectEnforcementUsersResponse500 | None:
    """ Removes users and groups from a project enforcement.

    Args:
        id (int):
        enforcement_id (int):
        body (ProjectEnforcementUsers | Unset): ProjectEnforcementUsers .

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteProjectEnforcementUsersResponse200 | DeleteProjectEnforcementUsersResponse400 | DeleteProjectEnforcementUsersResponse401 | DeleteProjectEnforcementUsersResponse403 | DeleteProjectEnforcementUsersResponse404 | DeleteProjectEnforcementUsersResponse422 | DeleteProjectEnforcementUsersResponse500
     """


    return sync_detailed(
        id=id,
enforcement_id=enforcement_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: int,
    enforcement_id: int,
    *,
    client: AuthenticatedClient,
    body: ProjectEnforcementUsers | Unset = UNSET,

) -> Response[DeleteProjectEnforcementUsersResponse200 | DeleteProjectEnforcementUsersResponse400 | DeleteProjectEnforcementUsersResponse401 | DeleteProjectEnforcementUsersResponse403 | DeleteProjectEnforcementUsersResponse404 | DeleteProjectEnforcementUsersResponse422 | DeleteProjectEnforcementUsersResponse500]:
    """ Removes users and groups from a project enforcement.

    Args:
        id (int):
        enforcement_id (int):
        body (ProjectEnforcementUsers | Unset): ProjectEnforcementUsers .

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteProjectEnforcementUsersResponse200 | DeleteProjectEnforcementUsersResponse400 | DeleteProjectEnforcementUsersResponse401 | DeleteProjectEnforcementUsersResponse403 | DeleteProjectEnforcementUsersResponse404 | DeleteProjectEnforcementUsersResponse422 | DeleteProjectEnforcementUsersResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
enforcement_id=enforcement_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    enforcement_id: int,
    *,
    client: AuthenticatedClient,
    body: ProjectEnforcementUsers | Unset = UNSET,

) -> DeleteProjectEnforcementUsersResponse200 | DeleteProjectEnforcementUsersResponse400 | DeleteProjectEnforcementUsersResponse401 | DeleteProjectEnforcementUsersResponse403 | DeleteProjectEnforcementUsersResponse404 | DeleteProjectEnforcementUsersResponse422 | DeleteProjectEnforcementUsersResponse500 | None:
    """ Removes users and groups from a project enforcement.

    Args:
        id (int):
        enforcement_id (int):
        body (ProjectEnforcementUsers | Unset): ProjectEnforcementUsers .

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteProjectEnforcementUsersResponse200 | DeleteProjectEnforcementUsersResponse400 | DeleteProjectEnforcementUsersResponse401 | DeleteProjectEnforcementUsersResponse403 | DeleteProjectEnforcementUsersResponse404 | DeleteProjectEnforcementUsersResponse422 | DeleteProjectEnforcementUsersResponse500
     """


    return (await asyncio_detailed(
        id=id,
enforcement_id=enforcement_id,
client=client,
body=body,

    )).parsed
