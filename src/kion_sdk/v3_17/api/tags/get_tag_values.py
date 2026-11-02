from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_tag_values_response_200 import GetTagValuesResponse200
from ...models.get_tag_values_response_400 import GetTagValuesResponse400
from ...models.get_tag_values_response_401 import GetTagValuesResponse401
from ...models.get_tag_values_response_404 import GetTagValuesResponse404
from ...models.get_tag_values_response_500 import GetTagValuesResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/tag/key/{id}/values".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetTagValuesResponse200 | GetTagValuesResponse400 | GetTagValuesResponse401 | GetTagValuesResponse404 | GetTagValuesResponse500 | None:
    if response.status_code == 200:
        response_200 = GetTagValuesResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetTagValuesResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetTagValuesResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = GetTagValuesResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetTagValuesResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetTagValuesResponse200 | GetTagValuesResponse400 | GetTagValuesResponse401 | GetTagValuesResponse404 | GetTagValuesResponse500]:
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

) -> Response[GetTagValuesResponse200 | GetTagValuesResponse400 | GetTagValuesResponse401 | GetTagValuesResponse404 | GetTagValuesResponse500]:
    """ Returns all values for a tag key in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTagValuesResponse200 | GetTagValuesResponse400 | GetTagValuesResponse401 | GetTagValuesResponse404 | GetTagValuesResponse500]
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

) -> GetTagValuesResponse200 | GetTagValuesResponse400 | GetTagValuesResponse401 | GetTagValuesResponse404 | GetTagValuesResponse500 | None:
    """ Returns all values for a tag key in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTagValuesResponse200 | GetTagValuesResponse400 | GetTagValuesResponse401 | GetTagValuesResponse404 | GetTagValuesResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetTagValuesResponse200 | GetTagValuesResponse400 | GetTagValuesResponse401 | GetTagValuesResponse404 | GetTagValuesResponse500]:
    """ Returns all values for a tag key in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTagValuesResponse200 | GetTagValuesResponse400 | GetTagValuesResponse401 | GetTagValuesResponse404 | GetTagValuesResponse500]
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

) -> GetTagValuesResponse200 | GetTagValuesResponse400 | GetTagValuesResponse401 | GetTagValuesResponse404 | GetTagValuesResponse500 | None:
    """ Returns all values for a tag key in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTagValuesResponse200 | GetTagValuesResponse400 | GetTagValuesResponse401 | GetTagValuesResponse404 | GetTagValuesResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
