from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.patch_project_response_200 import PatchProjectResponse200
from ...models.patch_project_response_400 import PatchProjectResponse400
from ...models.patch_project_response_401 import PatchProjectResponse401
from ...models.patch_project_response_403 import PatchProjectResponse403
from ...models.patch_project_response_404 import PatchProjectResponse404
from ...models.patch_project_response_422 import PatchProjectResponse422
from ...models.patch_project_response_500 import PatchProjectResponse500
from ...models.project_update import ProjectUpdate
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: ProjectUpdate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/project/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchProjectResponse200 | PatchProjectResponse400 | PatchProjectResponse401 | PatchProjectResponse403 | PatchProjectResponse404 | PatchProjectResponse422 | PatchProjectResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchProjectResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchProjectResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchProjectResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchProjectResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PatchProjectResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PatchProjectResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchProjectResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchProjectResponse200 | PatchProjectResponse400 | PatchProjectResponse401 | PatchProjectResponse403 | PatchProjectResponse404 | PatchProjectResponse422 | PatchProjectResponse500]:
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
    body: ProjectUpdate,

) -> Response[PatchProjectResponse200 | PatchProjectResponse400 | PatchProjectResponse401 | PatchProjectResponse403 | PatchProjectResponse404 | PatchProjectResponse422 | PatchProjectResponse500]:
    """ Updates a project by ID in the application.

    Args:
        id (int):
        body (ProjectUpdate): ProjectUpdate defines a project update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchProjectResponse200 | PatchProjectResponse400 | PatchProjectResponse401 | PatchProjectResponse403 | PatchProjectResponse404 | PatchProjectResponse422 | PatchProjectResponse500]
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
    body: ProjectUpdate,

) -> PatchProjectResponse200 | PatchProjectResponse400 | PatchProjectResponse401 | PatchProjectResponse403 | PatchProjectResponse404 | PatchProjectResponse422 | PatchProjectResponse500 | None:
    """ Updates a project by ID in the application.

    Args:
        id (int):
        body (ProjectUpdate): ProjectUpdate defines a project update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchProjectResponse200 | PatchProjectResponse400 | PatchProjectResponse401 | PatchProjectResponse403 | PatchProjectResponse404 | PatchProjectResponse422 | PatchProjectResponse500
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
    body: ProjectUpdate,

) -> Response[PatchProjectResponse200 | PatchProjectResponse400 | PatchProjectResponse401 | PatchProjectResponse403 | PatchProjectResponse404 | PatchProjectResponse422 | PatchProjectResponse500]:
    """ Updates a project by ID in the application.

    Args:
        id (int):
        body (ProjectUpdate): ProjectUpdate defines a project update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchProjectResponse200 | PatchProjectResponse400 | PatchProjectResponse401 | PatchProjectResponse403 | PatchProjectResponse404 | PatchProjectResponse422 | PatchProjectResponse500]
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
    body: ProjectUpdate,

) -> PatchProjectResponse200 | PatchProjectResponse400 | PatchProjectResponse401 | PatchProjectResponse403 | PatchProjectResponse404 | PatchProjectResponse422 | PatchProjectResponse500 | None:
    """ Updates a project by ID in the application.

    Args:
        id (int):
        body (ProjectUpdate): ProjectUpdate defines a project update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchProjectResponse200 | PatchProjectResponse400 | PatchProjectResponse401 | PatchProjectResponse403 | PatchProjectResponse404 | PatchProjectResponse422 | PatchProjectResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
