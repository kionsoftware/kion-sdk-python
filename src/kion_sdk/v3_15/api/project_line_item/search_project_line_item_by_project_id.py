from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.search_project_line_item_by_project_id_response_200 import SearchProjectLineItemByProjectIDResponse200
from ...models.search_project_line_item_by_project_id_response_400 import SearchProjectLineItemByProjectIDResponse400
from ...models.search_project_line_item_by_project_id_response_401 import SearchProjectLineItemByProjectIDResponse401
from ...models.search_project_line_item_by_project_id_response_403 import SearchProjectLineItemByProjectIDResponse403
from ...models.search_project_line_item_by_project_id_response_404 import SearchProjectLineItemByProjectIDResponse404
from ...models.search_project_line_item_by_project_id_response_500 import SearchProjectLineItemByProjectIDResponse500
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/project-line-item/search",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SearchProjectLineItemByProjectIDResponse200 | SearchProjectLineItemByProjectIDResponse400 | SearchProjectLineItemByProjectIDResponse401 | SearchProjectLineItemByProjectIDResponse403 | SearchProjectLineItemByProjectIDResponse404 | SearchProjectLineItemByProjectIDResponse500 | None:
    if response.status_code == 200:
        response_200 = SearchProjectLineItemByProjectIDResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = SearchProjectLineItemByProjectIDResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = SearchProjectLineItemByProjectIDResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = SearchProjectLineItemByProjectIDResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = SearchProjectLineItemByProjectIDResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = SearchProjectLineItemByProjectIDResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SearchProjectLineItemByProjectIDResponse200 | SearchProjectLineItemByProjectIDResponse400 | SearchProjectLineItemByProjectIDResponse401 | SearchProjectLineItemByProjectIDResponse403 | SearchProjectLineItemByProjectIDResponse404 | SearchProjectLineItemByProjectIDResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[SearchProjectLineItemByProjectIDResponse200 | SearchProjectLineItemByProjectIDResponse400 | SearchProjectLineItemByProjectIDResponse401 | SearchProjectLineItemByProjectIDResponse403 | SearchProjectLineItemByProjectIDResponse404 | SearchProjectLineItemByProjectIDResponse500]:
    """ Returns a keyword search filtered list of project line items from the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchProjectLineItemByProjectIDResponse200 | SearchProjectLineItemByProjectIDResponse400 | SearchProjectLineItemByProjectIDResponse401 | SearchProjectLineItemByProjectIDResponse403 | SearchProjectLineItemByProjectIDResponse404 | SearchProjectLineItemByProjectIDResponse500]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,

) -> SearchProjectLineItemByProjectIDResponse200 | SearchProjectLineItemByProjectIDResponse400 | SearchProjectLineItemByProjectIDResponse401 | SearchProjectLineItemByProjectIDResponse403 | SearchProjectLineItemByProjectIDResponse404 | SearchProjectLineItemByProjectIDResponse500 | None:
    """ Returns a keyword search filtered list of project line items from the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchProjectLineItemByProjectIDResponse200 | SearchProjectLineItemByProjectIDResponse400 | SearchProjectLineItemByProjectIDResponse401 | SearchProjectLineItemByProjectIDResponse403 | SearchProjectLineItemByProjectIDResponse404 | SearchProjectLineItemByProjectIDResponse500
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[SearchProjectLineItemByProjectIDResponse200 | SearchProjectLineItemByProjectIDResponse400 | SearchProjectLineItemByProjectIDResponse401 | SearchProjectLineItemByProjectIDResponse403 | SearchProjectLineItemByProjectIDResponse404 | SearchProjectLineItemByProjectIDResponse500]:
    """ Returns a keyword search filtered list of project line items from the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchProjectLineItemByProjectIDResponse200 | SearchProjectLineItemByProjectIDResponse400 | SearchProjectLineItemByProjectIDResponse401 | SearchProjectLineItemByProjectIDResponse403 | SearchProjectLineItemByProjectIDResponse404 | SearchProjectLineItemByProjectIDResponse500]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,

) -> SearchProjectLineItemByProjectIDResponse200 | SearchProjectLineItemByProjectIDResponse400 | SearchProjectLineItemByProjectIDResponse401 | SearchProjectLineItemByProjectIDResponse403 | SearchProjectLineItemByProjectIDResponse404 | SearchProjectLineItemByProjectIDResponse500 | None:
    """ Returns a keyword search filtered list of project line items from the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchProjectLineItemByProjectIDResponse200 | SearchProjectLineItemByProjectIDResponse400 | SearchProjectLineItemByProjectIDResponse401 | SearchProjectLineItemByProjectIDResponse403 | SearchProjectLineItemByProjectIDResponse404 | SearchProjectLineItemByProjectIDResponse500
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
