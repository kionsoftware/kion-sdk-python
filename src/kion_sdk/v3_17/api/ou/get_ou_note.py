from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_ou_note_response_200 import GetOUNoteResponse200
from ...models.get_ou_note_response_400 import GetOUNoteResponse400
from ...models.get_ou_note_response_401 import GetOUNoteResponse401
from ...models.get_ou_note_response_403 import GetOUNoteResponse403
from ...models.get_ou_note_response_404 import GetOUNoteResponse404
from ...models.get_ou_note_response_500 import GetOUNoteResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/ou-note/{id}".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetOUNoteResponse200 | GetOUNoteResponse400 | GetOUNoteResponse401 | GetOUNoteResponse403 | GetOUNoteResponse404 | GetOUNoteResponse500 | None:
    if response.status_code == 200:
        response_200 = GetOUNoteResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetOUNoteResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetOUNoteResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetOUNoteResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetOUNoteResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetOUNoteResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetOUNoteResponse200 | GetOUNoteResponse400 | GetOUNoteResponse401 | GetOUNoteResponse403 | GetOUNoteResponse404 | GetOUNoteResponse500]:
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

) -> Response[GetOUNoteResponse200 | GetOUNoteResponse400 | GetOUNoteResponse401 | GetOUNoteResponse403 | GetOUNoteResponse404 | GetOUNoteResponse500]:
    """ Finds an OU note by ID in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOUNoteResponse200 | GetOUNoteResponse400 | GetOUNoteResponse401 | GetOUNoteResponse403 | GetOUNoteResponse404 | GetOUNoteResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,

) -> GetOUNoteResponse200 | GetOUNoteResponse400 | GetOUNoteResponse401 | GetOUNoteResponse403 | GetOUNoteResponse404 | GetOUNoteResponse500 | None:
    """ Finds an OU note by ID in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOUNoteResponse200 | GetOUNoteResponse400 | GetOUNoteResponse401 | GetOUNoteResponse403 | GetOUNoteResponse404 | GetOUNoteResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetOUNoteResponse200 | GetOUNoteResponse400 | GetOUNoteResponse401 | GetOUNoteResponse403 | GetOUNoteResponse404 | GetOUNoteResponse500]:
    """ Finds an OU note by ID in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOUNoteResponse200 | GetOUNoteResponse400 | GetOUNoteResponse401 | GetOUNoteResponse403 | GetOUNoteResponse404 | GetOUNoteResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,

) -> GetOUNoteResponse200 | GetOUNoteResponse400 | GetOUNoteResponse401 | GetOUNoteResponse403 | GetOUNoteResponse404 | GetOUNoteResponse500 | None:
    """ Finds an OU note by ID in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOUNoteResponse200 | GetOUNoteResponse400 | GetOUNoteResponse401 | GetOUNoteResponse403 | GetOUNoteResponse404 | GetOUNoteResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
