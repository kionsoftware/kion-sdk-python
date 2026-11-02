from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.u_group_viewers import UGroupViewers
from ...models.update_u_group_viewers_response_200 import UpdateUGroupViewersResponse200
from ...models.update_u_group_viewers_response_400 import UpdateUGroupViewersResponse400
from ...models.update_u_group_viewers_response_401 import UpdateUGroupViewersResponse401
from ...models.update_u_group_viewers_response_403 import UpdateUGroupViewersResponse403
from ...models.update_u_group_viewers_response_404 import UpdateUGroupViewersResponse404
from ...models.update_u_group_viewers_response_422 import UpdateUGroupViewersResponse422
from ...models.update_u_group_viewers_response_500 import UpdateUGroupViewersResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: UGroupViewers,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/user-group/{id}/viewer".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UpdateUGroupViewersResponse200 | UpdateUGroupViewersResponse400 | UpdateUGroupViewersResponse401 | UpdateUGroupViewersResponse403 | UpdateUGroupViewersResponse404 | UpdateUGroupViewersResponse422 | UpdateUGroupViewersResponse500 | None:
    if response.status_code == 200:
        response_200 = UpdateUGroupViewersResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = UpdateUGroupViewersResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = UpdateUGroupViewersResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = UpdateUGroupViewersResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = UpdateUGroupViewersResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = UpdateUGroupViewersResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = UpdateUGroupViewersResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UpdateUGroupViewersResponse200 | UpdateUGroupViewersResponse400 | UpdateUGroupViewersResponse401 | UpdateUGroupViewersResponse403 | UpdateUGroupViewersResponse404 | UpdateUGroupViewersResponse422 | UpdateUGroupViewersResponse500]:
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
    body: UGroupViewers,

) -> Response[UpdateUGroupViewersResponse200 | UpdateUGroupViewersResponse400 | UpdateUGroupViewersResponse401 | UpdateUGroupViewersResponse403 | UpdateUGroupViewersResponse404 | UpdateUGroupViewersResponse422 | UpdateUGroupViewersResponse500]:
    """ Adds users and groups as viewers of a user group in the application.

    Args:
        id (int):
        body (UGroupViewers): UGroupViewers defines a user group viewer update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateUGroupViewersResponse200 | UpdateUGroupViewersResponse400 | UpdateUGroupViewersResponse401 | UpdateUGroupViewersResponse403 | UpdateUGroupViewersResponse404 | UpdateUGroupViewersResponse422 | UpdateUGroupViewersResponse500]
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
    body: UGroupViewers,

) -> UpdateUGroupViewersResponse200 | UpdateUGroupViewersResponse400 | UpdateUGroupViewersResponse401 | UpdateUGroupViewersResponse403 | UpdateUGroupViewersResponse404 | UpdateUGroupViewersResponse422 | UpdateUGroupViewersResponse500 | None:
    """ Adds users and groups as viewers of a user group in the application.

    Args:
        id (int):
        body (UGroupViewers): UGroupViewers defines a user group viewer update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateUGroupViewersResponse200 | UpdateUGroupViewersResponse400 | UpdateUGroupViewersResponse401 | UpdateUGroupViewersResponse403 | UpdateUGroupViewersResponse404 | UpdateUGroupViewersResponse422 | UpdateUGroupViewersResponse500
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
    body: UGroupViewers,

) -> Response[UpdateUGroupViewersResponse200 | UpdateUGroupViewersResponse400 | UpdateUGroupViewersResponse401 | UpdateUGroupViewersResponse403 | UpdateUGroupViewersResponse404 | UpdateUGroupViewersResponse422 | UpdateUGroupViewersResponse500]:
    """ Adds users and groups as viewers of a user group in the application.

    Args:
        id (int):
        body (UGroupViewers): UGroupViewers defines a user group viewer update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateUGroupViewersResponse200 | UpdateUGroupViewersResponse400 | UpdateUGroupViewersResponse401 | UpdateUGroupViewersResponse403 | UpdateUGroupViewersResponse404 | UpdateUGroupViewersResponse422 | UpdateUGroupViewersResponse500]
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
    body: UGroupViewers,

) -> UpdateUGroupViewersResponse200 | UpdateUGroupViewersResponse400 | UpdateUGroupViewersResponse401 | UpdateUGroupViewersResponse403 | UpdateUGroupViewersResponse404 | UpdateUGroupViewersResponse422 | UpdateUGroupViewersResponse500 | None:
    """ Adds users and groups as viewers of a user group in the application.

    Args:
        id (int):
        body (UGroupViewers): UGroupViewers defines a user group viewer update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateUGroupViewersResponse200 | UpdateUGroupViewersResponse400 | UpdateUGroupViewersResponse401 | UpdateUGroupViewersResponse403 | UpdateUGroupViewersResponse404 | UpdateUGroupViewersResponse422 | UpdateUGroupViewersResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
