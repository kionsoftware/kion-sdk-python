from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.patch_project_enforcements_response_200 import PatchProjectEnforcementsResponse200
from ...models.patch_project_enforcements_response_400 import PatchProjectEnforcementsResponse400
from ...models.patch_project_enforcements_response_401 import PatchProjectEnforcementsResponse401
from ...models.patch_project_enforcements_response_403 import PatchProjectEnforcementsResponse403
from ...models.patch_project_enforcements_response_404 import PatchProjectEnforcementsResponse404
from ...models.patch_project_enforcements_response_422 import PatchProjectEnforcementsResponse422
from ...models.patch_project_enforcements_response_500 import PatchProjectEnforcementsResponse500
from ...models.project_enforcement_update import ProjectEnforcementUpdate
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    enforcement_id: int,
    *,
    body: ProjectEnforcementUpdate | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/project/{id}/enforcement/{enforcement_id}".format(id=quote(str(id), safe=""),enforcement_id=quote(str(enforcement_id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchProjectEnforcementsResponse200 | PatchProjectEnforcementsResponse400 | PatchProjectEnforcementsResponse401 | PatchProjectEnforcementsResponse403 | PatchProjectEnforcementsResponse404 | PatchProjectEnforcementsResponse422 | PatchProjectEnforcementsResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchProjectEnforcementsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchProjectEnforcementsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchProjectEnforcementsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchProjectEnforcementsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PatchProjectEnforcementsResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PatchProjectEnforcementsResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchProjectEnforcementsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchProjectEnforcementsResponse200 | PatchProjectEnforcementsResponse400 | PatchProjectEnforcementsResponse401 | PatchProjectEnforcementsResponse403 | PatchProjectEnforcementsResponse404 | PatchProjectEnforcementsResponse422 | PatchProjectEnforcementsResponse500]:
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
    body: ProjectEnforcementUpdate | Unset = UNSET,

) -> Response[PatchProjectEnforcementsResponse200 | PatchProjectEnforcementsResponse400 | PatchProjectEnforcementsResponse401 | PatchProjectEnforcementsResponse403 | PatchProjectEnforcementsResponse404 | PatchProjectEnforcementsResponse422 | PatchProjectEnforcementsResponse500]:
    """ Updates a project enforcement in the application.

    Args:
        id (int):
        enforcement_id (int):
        body (ProjectEnforcementUpdate | Unset): ProjectEnforcementUpdate .

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchProjectEnforcementsResponse200 | PatchProjectEnforcementsResponse400 | PatchProjectEnforcementsResponse401 | PatchProjectEnforcementsResponse403 | PatchProjectEnforcementsResponse404 | PatchProjectEnforcementsResponse422 | PatchProjectEnforcementsResponse500]
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
    body: ProjectEnforcementUpdate | Unset = UNSET,

) -> PatchProjectEnforcementsResponse200 | PatchProjectEnforcementsResponse400 | PatchProjectEnforcementsResponse401 | PatchProjectEnforcementsResponse403 | PatchProjectEnforcementsResponse404 | PatchProjectEnforcementsResponse422 | PatchProjectEnforcementsResponse500 | None:
    """ Updates a project enforcement in the application.

    Args:
        id (int):
        enforcement_id (int):
        body (ProjectEnforcementUpdate | Unset): ProjectEnforcementUpdate .

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchProjectEnforcementsResponse200 | PatchProjectEnforcementsResponse400 | PatchProjectEnforcementsResponse401 | PatchProjectEnforcementsResponse403 | PatchProjectEnforcementsResponse404 | PatchProjectEnforcementsResponse422 | PatchProjectEnforcementsResponse500
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
    body: ProjectEnforcementUpdate | Unset = UNSET,

) -> Response[PatchProjectEnforcementsResponse200 | PatchProjectEnforcementsResponse400 | PatchProjectEnforcementsResponse401 | PatchProjectEnforcementsResponse403 | PatchProjectEnforcementsResponse404 | PatchProjectEnforcementsResponse422 | PatchProjectEnforcementsResponse500]:
    """ Updates a project enforcement in the application.

    Args:
        id (int):
        enforcement_id (int):
        body (ProjectEnforcementUpdate | Unset): ProjectEnforcementUpdate .

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchProjectEnforcementsResponse200 | PatchProjectEnforcementsResponse400 | PatchProjectEnforcementsResponse401 | PatchProjectEnforcementsResponse403 | PatchProjectEnforcementsResponse404 | PatchProjectEnforcementsResponse422 | PatchProjectEnforcementsResponse500]
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
    body: ProjectEnforcementUpdate | Unset = UNSET,

) -> PatchProjectEnforcementsResponse200 | PatchProjectEnforcementsResponse400 | PatchProjectEnforcementsResponse401 | PatchProjectEnforcementsResponse403 | PatchProjectEnforcementsResponse404 | PatchProjectEnforcementsResponse422 | PatchProjectEnforcementsResponse500 | None:
    """ Updates a project enforcement in the application.

    Args:
        id (int):
        enforcement_id (int):
        body (ProjectEnforcementUpdate | Unset): ProjectEnforcementUpdate .

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchProjectEnforcementsResponse200 | PatchProjectEnforcementsResponse400 | PatchProjectEnforcementsResponse401 | PatchProjectEnforcementsResponse403 | PatchProjectEnforcementsResponse404 | PatchProjectEnforcementsResponse422 | PatchProjectEnforcementsResponse500
     """


    return (await asyncio_detailed(
        id=id,
enforcement_id=enforcement_id,
client=client,
body=body,

    )).parsed
