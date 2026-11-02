from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_open_id_group_association_index_response_200 import GetOpenIDGroupAssociationIndexResponse200
from ...models.get_open_id_group_association_index_response_400 import GetOpenIDGroupAssociationIndexResponse400
from ...models.get_open_id_group_association_index_response_401 import GetOpenIDGroupAssociationIndexResponse401
from ...models.get_open_id_group_association_index_response_403 import GetOpenIDGroupAssociationIndexResponse403
from ...models.get_open_id_group_association_index_response_404 import GetOpenIDGroupAssociationIndexResponse404
from ...models.get_open_id_group_association_index_response_500 import GetOpenIDGroupAssociationIndexResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v4/idms/open-id/{id}/group-association".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetOpenIDGroupAssociationIndexResponse200 | GetOpenIDGroupAssociationIndexResponse400 | GetOpenIDGroupAssociationIndexResponse401 | GetOpenIDGroupAssociationIndexResponse403 | GetOpenIDGroupAssociationIndexResponse404 | GetOpenIDGroupAssociationIndexResponse500 | None:
    if response.status_code == 200:
        response_200 = GetOpenIDGroupAssociationIndexResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetOpenIDGroupAssociationIndexResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetOpenIDGroupAssociationIndexResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetOpenIDGroupAssociationIndexResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetOpenIDGroupAssociationIndexResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetOpenIDGroupAssociationIndexResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetOpenIDGroupAssociationIndexResponse200 | GetOpenIDGroupAssociationIndexResponse400 | GetOpenIDGroupAssociationIndexResponse401 | GetOpenIDGroupAssociationIndexResponse403 | GetOpenIDGroupAssociationIndexResponse404 | GetOpenIDGroupAssociationIndexResponse500]:
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

) -> Response[GetOpenIDGroupAssociationIndexResponse200 | GetOpenIDGroupAssociationIndexResponse400 | GetOpenIDGroupAssociationIndexResponse401 | GetOpenIDGroupAssociationIndexResponse403 | GetOpenIDGroupAssociationIndexResponse404 | GetOpenIDGroupAssociationIndexResponse500]:
    """ Returns a list of openID IDMS user group associations from the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOpenIDGroupAssociationIndexResponse200 | GetOpenIDGroupAssociationIndexResponse400 | GetOpenIDGroupAssociationIndexResponse401 | GetOpenIDGroupAssociationIndexResponse403 | GetOpenIDGroupAssociationIndexResponse404 | GetOpenIDGroupAssociationIndexResponse500]
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

) -> GetOpenIDGroupAssociationIndexResponse200 | GetOpenIDGroupAssociationIndexResponse400 | GetOpenIDGroupAssociationIndexResponse401 | GetOpenIDGroupAssociationIndexResponse403 | GetOpenIDGroupAssociationIndexResponse404 | GetOpenIDGroupAssociationIndexResponse500 | None:
    """ Returns a list of openID IDMS user group associations from the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOpenIDGroupAssociationIndexResponse200 | GetOpenIDGroupAssociationIndexResponse400 | GetOpenIDGroupAssociationIndexResponse401 | GetOpenIDGroupAssociationIndexResponse403 | GetOpenIDGroupAssociationIndexResponse404 | GetOpenIDGroupAssociationIndexResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetOpenIDGroupAssociationIndexResponse200 | GetOpenIDGroupAssociationIndexResponse400 | GetOpenIDGroupAssociationIndexResponse401 | GetOpenIDGroupAssociationIndexResponse403 | GetOpenIDGroupAssociationIndexResponse404 | GetOpenIDGroupAssociationIndexResponse500]:
    """ Returns a list of openID IDMS user group associations from the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOpenIDGroupAssociationIndexResponse200 | GetOpenIDGroupAssociationIndexResponse400 | GetOpenIDGroupAssociationIndexResponse401 | GetOpenIDGroupAssociationIndexResponse403 | GetOpenIDGroupAssociationIndexResponse404 | GetOpenIDGroupAssociationIndexResponse500]
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

) -> GetOpenIDGroupAssociationIndexResponse200 | GetOpenIDGroupAssociationIndexResponse400 | GetOpenIDGroupAssociationIndexResponse401 | GetOpenIDGroupAssociationIndexResponse403 | GetOpenIDGroupAssociationIndexResponse404 | GetOpenIDGroupAssociationIndexResponse500 | None:
    """ Returns a list of openID IDMS user group associations from the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOpenIDGroupAssociationIndexResponse200 | GetOpenIDGroupAssociationIndexResponse400 | GetOpenIDGroupAssociationIndexResponse401 | GetOpenIDGroupAssociationIndexResponse403 | GetOpenIDGroupAssociationIndexResponse404 | GetOpenIDGroupAssociationIndexResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
