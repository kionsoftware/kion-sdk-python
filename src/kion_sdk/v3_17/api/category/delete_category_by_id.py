from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_category_by_id_response_200 import DeleteCategoryByIDResponse200
from ...models.delete_category_by_id_response_400 import DeleteCategoryByIDResponse400
from ...models.delete_category_by_id_response_401 import DeleteCategoryByIDResponse401
from ...models.delete_category_by_id_response_404 import DeleteCategoryByIDResponse404
from ...models.delete_category_by_id_response_500 import DeleteCategoryByIDResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/category/{id}".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteCategoryByIDResponse200 | DeleteCategoryByIDResponse400 | DeleteCategoryByIDResponse401 | DeleteCategoryByIDResponse404 | DeleteCategoryByIDResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteCategoryByIDResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DeleteCategoryByIDResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteCategoryByIDResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = DeleteCategoryByIDResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = DeleteCategoryByIDResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteCategoryByIDResponse200 | DeleteCategoryByIDResponse400 | DeleteCategoryByIDResponse401 | DeleteCategoryByIDResponse404 | DeleteCategoryByIDResponse500]:
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

) -> Response[DeleteCategoryByIDResponse200 | DeleteCategoryByIDResponse400 | DeleteCategoryByIDResponse401 | DeleteCategoryByIDResponse404 | DeleteCategoryByIDResponse500]:
    """ Deletes a categories in the system.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteCategoryByIDResponse200 | DeleteCategoryByIDResponse400 | DeleteCategoryByIDResponse401 | DeleteCategoryByIDResponse404 | DeleteCategoryByIDResponse500]
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

) -> DeleteCategoryByIDResponse200 | DeleteCategoryByIDResponse400 | DeleteCategoryByIDResponse401 | DeleteCategoryByIDResponse404 | DeleteCategoryByIDResponse500 | None:
    """ Deletes a categories in the system.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteCategoryByIDResponse200 | DeleteCategoryByIDResponse400 | DeleteCategoryByIDResponse401 | DeleteCategoryByIDResponse404 | DeleteCategoryByIDResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteCategoryByIDResponse200 | DeleteCategoryByIDResponse400 | DeleteCategoryByIDResponse401 | DeleteCategoryByIDResponse404 | DeleteCategoryByIDResponse500]:
    """ Deletes a categories in the system.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteCategoryByIDResponse200 | DeleteCategoryByIDResponse400 | DeleteCategoryByIDResponse401 | DeleteCategoryByIDResponse404 | DeleteCategoryByIDResponse500]
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

) -> DeleteCategoryByIDResponse200 | DeleteCategoryByIDResponse400 | DeleteCategoryByIDResponse401 | DeleteCategoryByIDResponse404 | DeleteCategoryByIDResponse500 | None:
    """ Deletes a categories in the system.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteCategoryByIDResponse200 | DeleteCategoryByIDResponse400 | DeleteCategoryByIDResponse401 | DeleteCategoryByIDResponse404 | DeleteCategoryByIDResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
