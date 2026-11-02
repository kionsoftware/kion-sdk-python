from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_project_enforcements_response_200 import GetProjectEnforcementsResponse200
from ...models.get_project_enforcements_response_400 import GetProjectEnforcementsResponse400
from ...models.get_project_enforcements_response_401 import GetProjectEnforcementsResponse401
from ...models.get_project_enforcements_response_403 import GetProjectEnforcementsResponse403
from ...models.get_project_enforcements_response_404 import GetProjectEnforcementsResponse404
from ...models.get_project_enforcements_response_500 import GetProjectEnforcementsResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/project/{id}/enforcement".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetProjectEnforcementsResponse200 | GetProjectEnforcementsResponse400 | GetProjectEnforcementsResponse401 | GetProjectEnforcementsResponse403 | GetProjectEnforcementsResponse404 | GetProjectEnforcementsResponse500 | None:
    if response.status_code == 200:
        response_200 = GetProjectEnforcementsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetProjectEnforcementsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetProjectEnforcementsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetProjectEnforcementsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetProjectEnforcementsResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetProjectEnforcementsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetProjectEnforcementsResponse200 | GetProjectEnforcementsResponse400 | GetProjectEnforcementsResponse401 | GetProjectEnforcementsResponse403 | GetProjectEnforcementsResponse404 | GetProjectEnforcementsResponse500]:
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

) -> Response[GetProjectEnforcementsResponse200 | GetProjectEnforcementsResponse400 | GetProjectEnforcementsResponse401 | GetProjectEnforcementsResponse403 | GetProjectEnforcementsResponse404 | GetProjectEnforcementsResponse500]:
    """ Returns a list of enforcments that are on a project.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProjectEnforcementsResponse200 | GetProjectEnforcementsResponse400 | GetProjectEnforcementsResponse401 | GetProjectEnforcementsResponse403 | GetProjectEnforcementsResponse404 | GetProjectEnforcementsResponse500]
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

) -> GetProjectEnforcementsResponse200 | GetProjectEnforcementsResponse400 | GetProjectEnforcementsResponse401 | GetProjectEnforcementsResponse403 | GetProjectEnforcementsResponse404 | GetProjectEnforcementsResponse500 | None:
    """ Returns a list of enforcments that are on a project.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProjectEnforcementsResponse200 | GetProjectEnforcementsResponse400 | GetProjectEnforcementsResponse401 | GetProjectEnforcementsResponse403 | GetProjectEnforcementsResponse404 | GetProjectEnforcementsResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetProjectEnforcementsResponse200 | GetProjectEnforcementsResponse400 | GetProjectEnforcementsResponse401 | GetProjectEnforcementsResponse403 | GetProjectEnforcementsResponse404 | GetProjectEnforcementsResponse500]:
    """ Returns a list of enforcments that are on a project.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProjectEnforcementsResponse200 | GetProjectEnforcementsResponse400 | GetProjectEnforcementsResponse401 | GetProjectEnforcementsResponse403 | GetProjectEnforcementsResponse404 | GetProjectEnforcementsResponse500]
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

) -> GetProjectEnforcementsResponse200 | GetProjectEnforcementsResponse400 | GetProjectEnforcementsResponse401 | GetProjectEnforcementsResponse403 | GetProjectEnforcementsResponse404 | GetProjectEnforcementsResponse500 | None:
    """ Returns a list of enforcments that are on a project.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProjectEnforcementsResponse200 | GetProjectEnforcementsResponse400 | GetProjectEnforcementsResponse401 | GetProjectEnforcementsResponse403 | GetProjectEnforcementsResponse404 | GetProjectEnforcementsResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
