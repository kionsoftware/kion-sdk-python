from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.ou_note_create import OUNoteCreate
from ...models.post_ou_note_response_201 import PostOUNoteResponse201
from ...models.post_ou_note_response_400 import PostOUNoteResponse400
from ...models.post_ou_note_response_401 import PostOUNoteResponse401
from ...models.post_ou_note_response_403 import PostOUNoteResponse403
from ...models.post_ou_note_response_422 import PostOUNoteResponse422
from ...models.post_ou_note_response_500 import PostOUNoteResponse500
from typing import cast



def _get_kwargs(
    *,
    body: OUNoteCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/ou-note",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostOUNoteResponse201 | PostOUNoteResponse400 | PostOUNoteResponse401 | PostOUNoteResponse403 | PostOUNoteResponse422 | PostOUNoteResponse500 | None:
    if response.status_code == 201:
        response_201 = PostOUNoteResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostOUNoteResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostOUNoteResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostOUNoteResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostOUNoteResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostOUNoteResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostOUNoteResponse201 | PostOUNoteResponse400 | PostOUNoteResponse401 | PostOUNoteResponse403 | PostOUNoteResponse422 | PostOUNoteResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: OUNoteCreate,

) -> Response[PostOUNoteResponse201 | PostOUNoteResponse400 | PostOUNoteResponse401 | PostOUNoteResponse403 | PostOUNoteResponse422 | PostOUNoteResponse500]:
    """ Creates an OU note in the application.

    Args:
        body (OUNoteCreate): OUNoteCreate defines the structure for creating an OU note.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostOUNoteResponse201 | PostOUNoteResponse400 | PostOUNoteResponse401 | PostOUNoteResponse403 | PostOUNoteResponse422 | PostOUNoteResponse500]
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
    body: OUNoteCreate,

) -> PostOUNoteResponse201 | PostOUNoteResponse400 | PostOUNoteResponse401 | PostOUNoteResponse403 | PostOUNoteResponse422 | PostOUNoteResponse500 | None:
    """ Creates an OU note in the application.

    Args:
        body (OUNoteCreate): OUNoteCreate defines the structure for creating an OU note.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostOUNoteResponse201 | PostOUNoteResponse400 | PostOUNoteResponse401 | PostOUNoteResponse403 | PostOUNoteResponse422 | PostOUNoteResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: OUNoteCreate,

) -> Response[PostOUNoteResponse201 | PostOUNoteResponse400 | PostOUNoteResponse401 | PostOUNoteResponse403 | PostOUNoteResponse422 | PostOUNoteResponse500]:
    """ Creates an OU note in the application.

    Args:
        body (OUNoteCreate): OUNoteCreate defines the structure for creating an OU note.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostOUNoteResponse201 | PostOUNoteResponse400 | PostOUNoteResponse401 | PostOUNoteResponse403 | PostOUNoteResponse422 | PostOUNoteResponse500]
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
    body: OUNoteCreate,

) -> PostOUNoteResponse201 | PostOUNoteResponse400 | PostOUNoteResponse401 | PostOUNoteResponse403 | PostOUNoteResponse422 | PostOUNoteResponse500 | None:
    """ Creates an OU note in the application.

    Args:
        body (OUNoteCreate): OUNoteCreate defines the structure for creating an OU note.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostOUNoteResponse201 | PostOUNoteResponse400 | PostOUNoteResponse401 | PostOUNoteResponse403 | PostOUNoteResponse422 | PostOUNoteResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
