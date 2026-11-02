from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.category_update import CategoryUpdate
from ...models.update_category_by_id_response_200 import UpdateCategoryByIDResponse200
from ...models.update_category_by_id_response_400 import UpdateCategoryByIDResponse400
from ...models.update_category_by_id_response_401 import UpdateCategoryByIDResponse401
from ...models.update_category_by_id_response_404 import UpdateCategoryByIDResponse404
from ...models.update_category_by_id_response_422 import UpdateCategoryByIDResponse422
from ...models.update_category_by_id_response_500 import UpdateCategoryByIDResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: CategoryUpdate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/category/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UpdateCategoryByIDResponse200 | UpdateCategoryByIDResponse400 | UpdateCategoryByIDResponse401 | UpdateCategoryByIDResponse404 | UpdateCategoryByIDResponse422 | UpdateCategoryByIDResponse500 | None:
    if response.status_code == 200:
        response_200 = UpdateCategoryByIDResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = UpdateCategoryByIDResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = UpdateCategoryByIDResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = UpdateCategoryByIDResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = UpdateCategoryByIDResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = UpdateCategoryByIDResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UpdateCategoryByIDResponse200 | UpdateCategoryByIDResponse400 | UpdateCategoryByIDResponse401 | UpdateCategoryByIDResponse404 | UpdateCategoryByIDResponse422 | UpdateCategoryByIDResponse500]:
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
    body: CategoryUpdate,

) -> Response[UpdateCategoryByIDResponse200 | UpdateCategoryByIDResponse400 | UpdateCategoryByIDResponse401 | UpdateCategoryByIDResponse404 | UpdateCategoryByIDResponse422 | UpdateCategoryByIDResponse500]:
    """ Updates a categories in the system.

    Args:
        id (int):
        body (CategoryUpdate): CategoryUpdate updates a Category.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateCategoryByIDResponse200 | UpdateCategoryByIDResponse400 | UpdateCategoryByIDResponse401 | UpdateCategoryByIDResponse404 | UpdateCategoryByIDResponse422 | UpdateCategoryByIDResponse500]
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
    body: CategoryUpdate,

) -> UpdateCategoryByIDResponse200 | UpdateCategoryByIDResponse400 | UpdateCategoryByIDResponse401 | UpdateCategoryByIDResponse404 | UpdateCategoryByIDResponse422 | UpdateCategoryByIDResponse500 | None:
    """ Updates a categories in the system.

    Args:
        id (int):
        body (CategoryUpdate): CategoryUpdate updates a Category.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateCategoryByIDResponse200 | UpdateCategoryByIDResponse400 | UpdateCategoryByIDResponse401 | UpdateCategoryByIDResponse404 | UpdateCategoryByIDResponse422 | UpdateCategoryByIDResponse500
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
    body: CategoryUpdate,

) -> Response[UpdateCategoryByIDResponse200 | UpdateCategoryByIDResponse400 | UpdateCategoryByIDResponse401 | UpdateCategoryByIDResponse404 | UpdateCategoryByIDResponse422 | UpdateCategoryByIDResponse500]:
    """ Updates a categories in the system.

    Args:
        id (int):
        body (CategoryUpdate): CategoryUpdate updates a Category.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateCategoryByIDResponse200 | UpdateCategoryByIDResponse400 | UpdateCategoryByIDResponse401 | UpdateCategoryByIDResponse404 | UpdateCategoryByIDResponse422 | UpdateCategoryByIDResponse500]
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
    body: CategoryUpdate,

) -> UpdateCategoryByIDResponse200 | UpdateCategoryByIDResponse400 | UpdateCategoryByIDResponse401 | UpdateCategoryByIDResponse404 | UpdateCategoryByIDResponse422 | UpdateCategoryByIDResponse500 | None:
    """ Updates a categories in the system.

    Args:
        id (int):
        body (CategoryUpdate): CategoryUpdate updates a Category.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateCategoryByIDResponse200 | UpdateCategoryByIDResponse400 | UpdateCategoryByIDResponse401 | UpdateCategoryByIDResponse404 | UpdateCategoryByIDResponse422 | UpdateCategoryByIDResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
