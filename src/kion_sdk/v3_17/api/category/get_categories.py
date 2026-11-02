from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_categories_response_200 import GetCategoriesResponse200
from ...models.get_categories_response_401 import GetCategoriesResponse401
from ...models.get_categories_response_500 import GetCategoriesResponse500
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/category",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetCategoriesResponse200 | GetCategoriesResponse401 | GetCategoriesResponse500 | None:
    if response.status_code == 200:
        response_200 = GetCategoriesResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetCategoriesResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 500:
        response_500 = GetCategoriesResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetCategoriesResponse200 | GetCategoriesResponse401 | GetCategoriesResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetCategoriesResponse200 | GetCategoriesResponse401 | GetCategoriesResponse500]:
    """ Gets a list of the categories in the system.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCategoriesResponse200 | GetCategoriesResponse401 | GetCategoriesResponse500]
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

) -> GetCategoriesResponse200 | GetCategoriesResponse401 | GetCategoriesResponse500 | None:
    """ Gets a list of the categories in the system.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCategoriesResponse200 | GetCategoriesResponse401 | GetCategoriesResponse500
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetCategoriesResponse200 | GetCategoriesResponse401 | GetCategoriesResponse500]:
    """ Gets a list of the categories in the system.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCategoriesResponse200 | GetCategoriesResponse401 | GetCategoriesResponse500]
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

) -> GetCategoriesResponse200 | GetCategoriesResponse401 | GetCategoriesResponse500 | None:
    """ Gets a list of the categories in the system.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCategoriesResponse200 | GetCategoriesResponse401 | GetCategoriesResponse500
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
