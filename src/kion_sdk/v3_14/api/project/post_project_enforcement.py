from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_project_enforcement_response_201 import PostProjectEnforcementResponse201
from ...models.post_project_enforcement_response_400 import PostProjectEnforcementResponse400
from ...models.post_project_enforcement_response_401 import PostProjectEnforcementResponse401
from ...models.post_project_enforcement_response_403 import PostProjectEnforcementResponse403
from ...models.post_project_enforcement_response_404 import PostProjectEnforcementResponse404
from ...models.post_project_enforcement_response_422 import PostProjectEnforcementResponse422
from ...models.post_project_enforcement_response_500 import PostProjectEnforcementResponse500
from ...models.project_enforcement_create import ProjectEnforcementCreate
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: ProjectEnforcementCreate | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/project/{id}/enforcement".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostProjectEnforcementResponse201 | PostProjectEnforcementResponse400 | PostProjectEnforcementResponse401 | PostProjectEnforcementResponse403 | PostProjectEnforcementResponse404 | PostProjectEnforcementResponse422 | PostProjectEnforcementResponse500 | None:
    if response.status_code == 201:
        response_201 = PostProjectEnforcementResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostProjectEnforcementResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostProjectEnforcementResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostProjectEnforcementResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PostProjectEnforcementResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PostProjectEnforcementResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostProjectEnforcementResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostProjectEnforcementResponse201 | PostProjectEnforcementResponse400 | PostProjectEnforcementResponse401 | PostProjectEnforcementResponse403 | PostProjectEnforcementResponse404 | PostProjectEnforcementResponse422 | PostProjectEnforcementResponse500]:
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
    body: ProjectEnforcementCreate | Unset = UNSET,

) -> Response[PostProjectEnforcementResponse201 | PostProjectEnforcementResponse400 | PostProjectEnforcementResponse401 | PostProjectEnforcementResponse403 | PostProjectEnforcementResponse404 | PostProjectEnforcementResponse422 | PostProjectEnforcementResponse500]:
    """ Creates a project enforcement in the application.

    Args:
        id (int):
        body (ProjectEnforcementCreate | Unset): ProjectEnforcementCreate .

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostProjectEnforcementResponse201 | PostProjectEnforcementResponse400 | PostProjectEnforcementResponse401 | PostProjectEnforcementResponse403 | PostProjectEnforcementResponse404 | PostProjectEnforcementResponse422 | PostProjectEnforcementResponse500]
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
    body: ProjectEnforcementCreate | Unset = UNSET,

) -> PostProjectEnforcementResponse201 | PostProjectEnforcementResponse400 | PostProjectEnforcementResponse401 | PostProjectEnforcementResponse403 | PostProjectEnforcementResponse404 | PostProjectEnforcementResponse422 | PostProjectEnforcementResponse500 | None:
    """ Creates a project enforcement in the application.

    Args:
        id (int):
        body (ProjectEnforcementCreate | Unset): ProjectEnforcementCreate .

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostProjectEnforcementResponse201 | PostProjectEnforcementResponse400 | PostProjectEnforcementResponse401 | PostProjectEnforcementResponse403 | PostProjectEnforcementResponse404 | PostProjectEnforcementResponse422 | PostProjectEnforcementResponse500
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
    body: ProjectEnforcementCreate | Unset = UNSET,

) -> Response[PostProjectEnforcementResponse201 | PostProjectEnforcementResponse400 | PostProjectEnforcementResponse401 | PostProjectEnforcementResponse403 | PostProjectEnforcementResponse404 | PostProjectEnforcementResponse422 | PostProjectEnforcementResponse500]:
    """ Creates a project enforcement in the application.

    Args:
        id (int):
        body (ProjectEnforcementCreate | Unset): ProjectEnforcementCreate .

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostProjectEnforcementResponse201 | PostProjectEnforcementResponse400 | PostProjectEnforcementResponse401 | PostProjectEnforcementResponse403 | PostProjectEnforcementResponse404 | PostProjectEnforcementResponse422 | PostProjectEnforcementResponse500]
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
    body: ProjectEnforcementCreate | Unset = UNSET,

) -> PostProjectEnforcementResponse201 | PostProjectEnforcementResponse400 | PostProjectEnforcementResponse401 | PostProjectEnforcementResponse403 | PostProjectEnforcementResponse404 | PostProjectEnforcementResponse422 | PostProjectEnforcementResponse500 | None:
    """ Creates a project enforcement in the application.

    Args:
        id (int):
        body (ProjectEnforcementCreate | Unset): ProjectEnforcementCreate .

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostProjectEnforcementResponse201 | PostProjectEnforcementResponse400 | PostProjectEnforcementResponse401 | PostProjectEnforcementResponse403 | PostProjectEnforcementResponse404 | PostProjectEnforcementResponse422 | PostProjectEnforcementResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
