from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_project_note_response_201 import PostProjectNoteResponse201
from ...models.post_project_note_response_400 import PostProjectNoteResponse400
from ...models.post_project_note_response_401 import PostProjectNoteResponse401
from ...models.post_project_note_response_403 import PostProjectNoteResponse403
from ...models.post_project_note_response_422 import PostProjectNoteResponse422
from ...models.post_project_note_response_500 import PostProjectNoteResponse500
from ...models.project_note_create import ProjectNoteCreate
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: ProjectNoteCreate | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/project-note",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostProjectNoteResponse201 | PostProjectNoteResponse400 | PostProjectNoteResponse401 | PostProjectNoteResponse403 | PostProjectNoteResponse422 | PostProjectNoteResponse500 | None:
    if response.status_code == 201:
        response_201 = PostProjectNoteResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostProjectNoteResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostProjectNoteResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostProjectNoteResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostProjectNoteResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostProjectNoteResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostProjectNoteResponse201 | PostProjectNoteResponse400 | PostProjectNoteResponse401 | PostProjectNoteResponse403 | PostProjectNoteResponse422 | PostProjectNoteResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ProjectNoteCreate | Unset = UNSET,

) -> Response[PostProjectNoteResponse201 | PostProjectNoteResponse400 | PostProjectNoteResponse401 | PostProjectNoteResponse403 | PostProjectNoteResponse422 | PostProjectNoteResponse500]:
    """ Creates a Project Note.

    Args:
        body (ProjectNoteCreate | Unset): ProjectNoteCreate represents the creation of a
            ProjectNote.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostProjectNoteResponse201 | PostProjectNoteResponse400 | PostProjectNoteResponse401 | PostProjectNoteResponse403 | PostProjectNoteResponse422 | PostProjectNoteResponse500]
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
    body: ProjectNoteCreate | Unset = UNSET,

) -> PostProjectNoteResponse201 | PostProjectNoteResponse400 | PostProjectNoteResponse401 | PostProjectNoteResponse403 | PostProjectNoteResponse422 | PostProjectNoteResponse500 | None:
    """ Creates a Project Note.

    Args:
        body (ProjectNoteCreate | Unset): ProjectNoteCreate represents the creation of a
            ProjectNote.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostProjectNoteResponse201 | PostProjectNoteResponse400 | PostProjectNoteResponse401 | PostProjectNoteResponse403 | PostProjectNoteResponse422 | PostProjectNoteResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ProjectNoteCreate | Unset = UNSET,

) -> Response[PostProjectNoteResponse201 | PostProjectNoteResponse400 | PostProjectNoteResponse401 | PostProjectNoteResponse403 | PostProjectNoteResponse422 | PostProjectNoteResponse500]:
    """ Creates a Project Note.

    Args:
        body (ProjectNoteCreate | Unset): ProjectNoteCreate represents the creation of a
            ProjectNote.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostProjectNoteResponse201 | PostProjectNoteResponse400 | PostProjectNoteResponse401 | PostProjectNoteResponse403 | PostProjectNoteResponse422 | PostProjectNoteResponse500]
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
    body: ProjectNoteCreate | Unset = UNSET,

) -> PostProjectNoteResponse201 | PostProjectNoteResponse400 | PostProjectNoteResponse401 | PostProjectNoteResponse403 | PostProjectNoteResponse422 | PostProjectNoteResponse500 | None:
    """ Creates a Project Note.

    Args:
        body (ProjectNoteCreate | Unset): ProjectNoteCreate represents the creation of a
            ProjectNote.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostProjectNoteResponse201 | PostProjectNoteResponse400 | PostProjectNoteResponse401 | PostProjectNoteResponse403 | PostProjectNoteResponse422 | PostProjectNoteResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
