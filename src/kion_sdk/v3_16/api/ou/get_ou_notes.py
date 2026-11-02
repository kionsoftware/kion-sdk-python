from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_ou_notes_response_200 import GetOUNotesResponse200
from ...models.get_ou_notes_response_400 import GetOUNotesResponse400
from ...models.get_ou_notes_response_401 import GetOUNotesResponse401
from ...models.get_ou_notes_response_403 import GetOUNotesResponse403
from ...models.get_ou_notes_response_404 import GetOUNotesResponse404
from ...models.get_ou_notes_response_500 import GetOUNotesResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    page: int | Unset = 1,
    count: int | Unset = 15,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["count"] = count


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/ou/{id}/ou-note".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetOUNotesResponse200 | GetOUNotesResponse400 | GetOUNotesResponse401 | GetOUNotesResponse403 | GetOUNotesResponse404 | GetOUNotesResponse500 | None:
    if response.status_code == 200:
        response_200 = GetOUNotesResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetOUNotesResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetOUNotesResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetOUNotesResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetOUNotesResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetOUNotesResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetOUNotesResponse200 | GetOUNotesResponse400 | GetOUNotesResponse401 | GetOUNotesResponse403 | GetOUNotesResponse404 | GetOUNotesResponse500]:
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
    page: int | Unset = 1,
    count: int | Unset = 15,

) -> Response[GetOUNotesResponse200 | GetOUNotesResponse400 | GetOUNotesResponse401 | GetOUNotesResponse403 | GetOUNotesResponse404 | GetOUNotesResponse500]:
    """ Returns a list of notes for an OU from the application.

    Args:
        id (int):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 15.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOUNotesResponse200 | GetOUNotesResponse400 | GetOUNotesResponse401 | GetOUNotesResponse403 | GetOUNotesResponse404 | GetOUNotesResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
page=page,
count=count,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    count: int | Unset = 15,

) -> GetOUNotesResponse200 | GetOUNotesResponse400 | GetOUNotesResponse401 | GetOUNotesResponse403 | GetOUNotesResponse404 | GetOUNotesResponse500 | None:
    """ Returns a list of notes for an OU from the application.

    Args:
        id (int):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 15.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOUNotesResponse200 | GetOUNotesResponse400 | GetOUNotesResponse401 | GetOUNotesResponse403 | GetOUNotesResponse404 | GetOUNotesResponse500
     """


    return sync_detailed(
        id=id,
client=client,
page=page,
count=count,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    count: int | Unset = 15,

) -> Response[GetOUNotesResponse200 | GetOUNotesResponse400 | GetOUNotesResponse401 | GetOUNotesResponse403 | GetOUNotesResponse404 | GetOUNotesResponse500]:
    """ Returns a list of notes for an OU from the application.

    Args:
        id (int):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 15.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOUNotesResponse200 | GetOUNotesResponse400 | GetOUNotesResponse401 | GetOUNotesResponse403 | GetOUNotesResponse404 | GetOUNotesResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
page=page,
count=count,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    count: int | Unset = 15,

) -> GetOUNotesResponse200 | GetOUNotesResponse400 | GetOUNotesResponse401 | GetOUNotesResponse403 | GetOUNotesResponse404 | GetOUNotesResponse500 | None:
    """ Returns a list of notes for an OU from the application.

    Args:
        id (int):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 15.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOUNotesResponse200 | GetOUNotesResponse400 | GetOUNotesResponse401 | GetOUNotesResponse403 | GetOUNotesResponse404 | GetOUNotesResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
page=page,
count=count,

    )).parsed
