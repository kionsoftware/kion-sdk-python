from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.project_owners import ProjectOwners
from ...models.update_project_owners_response_200 import UpdateProjectOwnersResponse200
from ...models.update_project_owners_response_400 import UpdateProjectOwnersResponse400
from ...models.update_project_owners_response_401 import UpdateProjectOwnersResponse401
from ...models.update_project_owners_response_403 import UpdateProjectOwnersResponse403
from ...models.update_project_owners_response_404 import UpdateProjectOwnersResponse404
from ...models.update_project_owners_response_422 import UpdateProjectOwnersResponse422
from ...models.update_project_owners_response_500 import UpdateProjectOwnersResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: ProjectOwners,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/project/{id}/owner".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UpdateProjectOwnersResponse200 | UpdateProjectOwnersResponse400 | UpdateProjectOwnersResponse401 | UpdateProjectOwnersResponse403 | UpdateProjectOwnersResponse404 | UpdateProjectOwnersResponse422 | UpdateProjectOwnersResponse500 | None:
    if response.status_code == 200:
        response_200 = UpdateProjectOwnersResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = UpdateProjectOwnersResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = UpdateProjectOwnersResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = UpdateProjectOwnersResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = UpdateProjectOwnersResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = UpdateProjectOwnersResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = UpdateProjectOwnersResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UpdateProjectOwnersResponse200 | UpdateProjectOwnersResponse400 | UpdateProjectOwnersResponse401 | UpdateProjectOwnersResponse403 | UpdateProjectOwnersResponse404 | UpdateProjectOwnersResponse422 | UpdateProjectOwnersResponse500]:
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
    body: ProjectOwners,

) -> Response[UpdateProjectOwnersResponse200 | UpdateProjectOwnersResponse400 | UpdateProjectOwnersResponse401 | UpdateProjectOwnersResponse403 | UpdateProjectOwnersResponse404 | UpdateProjectOwnersResponse422 | UpdateProjectOwnersResponse500]:
    """ Adds or removes users and groups as owners of a project in the application.

    Args:
        id (int):
        body (ProjectOwners): ProjectOwners defines a project owner update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateProjectOwnersResponse200 | UpdateProjectOwnersResponse400 | UpdateProjectOwnersResponse401 | UpdateProjectOwnersResponse403 | UpdateProjectOwnersResponse404 | UpdateProjectOwnersResponse422 | UpdateProjectOwnersResponse500]
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
    body: ProjectOwners,

) -> UpdateProjectOwnersResponse200 | UpdateProjectOwnersResponse400 | UpdateProjectOwnersResponse401 | UpdateProjectOwnersResponse403 | UpdateProjectOwnersResponse404 | UpdateProjectOwnersResponse422 | UpdateProjectOwnersResponse500 | None:
    """ Adds or removes users and groups as owners of a project in the application.

    Args:
        id (int):
        body (ProjectOwners): ProjectOwners defines a project owner update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateProjectOwnersResponse200 | UpdateProjectOwnersResponse400 | UpdateProjectOwnersResponse401 | UpdateProjectOwnersResponse403 | UpdateProjectOwnersResponse404 | UpdateProjectOwnersResponse422 | UpdateProjectOwnersResponse500
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
    body: ProjectOwners,

) -> Response[UpdateProjectOwnersResponse200 | UpdateProjectOwnersResponse400 | UpdateProjectOwnersResponse401 | UpdateProjectOwnersResponse403 | UpdateProjectOwnersResponse404 | UpdateProjectOwnersResponse422 | UpdateProjectOwnersResponse500]:
    """ Adds or removes users and groups as owners of a project in the application.

    Args:
        id (int):
        body (ProjectOwners): ProjectOwners defines a project owner update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateProjectOwnersResponse200 | UpdateProjectOwnersResponse400 | UpdateProjectOwnersResponse401 | UpdateProjectOwnersResponse403 | UpdateProjectOwnersResponse404 | UpdateProjectOwnersResponse422 | UpdateProjectOwnersResponse500]
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
    body: ProjectOwners,

) -> UpdateProjectOwnersResponse200 | UpdateProjectOwnersResponse400 | UpdateProjectOwnersResponse401 | UpdateProjectOwnersResponse403 | UpdateProjectOwnersResponse404 | UpdateProjectOwnersResponse422 | UpdateProjectOwnersResponse500 | None:
    """ Adds or removes users and groups as owners of a project in the application.

    Args:
        id (int):
        body (ProjectOwners): ProjectOwners defines a project owner update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateProjectOwnersResponse200 | UpdateProjectOwnersResponse400 | UpdateProjectOwnersResponse401 | UpdateProjectOwnersResponse403 | UpdateProjectOwnersResponse404 | UpdateProjectOwnersResponse422 | UpdateProjectOwnersResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
