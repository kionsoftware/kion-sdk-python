from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_azure_policy_paginated_index_response_200 import GetAzurePolicyPaginatedIndexResponse200
from ...models.get_azure_policy_paginated_index_response_400 import GetAzurePolicyPaginatedIndexResponse400
from ...models.get_azure_policy_paginated_index_response_401 import GetAzurePolicyPaginatedIndexResponse401
from ...models.get_azure_policy_paginated_index_response_403 import GetAzurePolicyPaginatedIndexResponse403
from ...models.get_azure_policy_paginated_index_response_500 import GetAzurePolicyPaginatedIndexResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    page: int | Unset = UNSET,
    count: int | Unset = UNSET,
    sort_method: str | Unset = UNSET,
    sort_order: str | Unset = 'ASC',

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["count"] = count

    params["sortMethod"] = sort_method

    params["sortOrder"] = sort_order


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v4/azure-policy",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetAzurePolicyPaginatedIndexResponse200 | GetAzurePolicyPaginatedIndexResponse400 | GetAzurePolicyPaginatedIndexResponse401 | GetAzurePolicyPaginatedIndexResponse403 | GetAzurePolicyPaginatedIndexResponse500 | None:
    if response.status_code == 200:
        response_200 = GetAzurePolicyPaginatedIndexResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetAzurePolicyPaginatedIndexResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetAzurePolicyPaginatedIndexResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetAzurePolicyPaginatedIndexResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetAzurePolicyPaginatedIndexResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetAzurePolicyPaginatedIndexResponse200 | GetAzurePolicyPaginatedIndexResponse400 | GetAzurePolicyPaginatedIndexResponse401 | GetAzurePolicyPaginatedIndexResponse403 | GetAzurePolicyPaginatedIndexResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    count: int | Unset = UNSET,
    sort_method: str | Unset = UNSET,
    sort_order: str | Unset = 'ASC',

) -> Response[GetAzurePolicyPaginatedIndexResponse200 | GetAzurePolicyPaginatedIndexResponse400 | GetAzurePolicyPaginatedIndexResponse401 | GetAzurePolicyPaginatedIndexResponse403 | GetAzurePolicyPaginatedIndexResponse500]:
    """ Gets all Azure policies definitions in cloudtamer.io and returns them paginated.

    Args:
        page (int | Unset):
        count (int | Unset):
        sort_method (str | Unset):
        sort_order (str | Unset):  Default: 'ASC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAzurePolicyPaginatedIndexResponse200 | GetAzurePolicyPaginatedIndexResponse400 | GetAzurePolicyPaginatedIndexResponse401 | GetAzurePolicyPaginatedIndexResponse403 | GetAzurePolicyPaginatedIndexResponse500]
     """


    kwargs = _get_kwargs(
        page=page,
count=count,
sort_method=sort_method,
sort_order=sort_order,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    count: int | Unset = UNSET,
    sort_method: str | Unset = UNSET,
    sort_order: str | Unset = 'ASC',

) -> GetAzurePolicyPaginatedIndexResponse200 | GetAzurePolicyPaginatedIndexResponse400 | GetAzurePolicyPaginatedIndexResponse401 | GetAzurePolicyPaginatedIndexResponse403 | GetAzurePolicyPaginatedIndexResponse500 | None:
    """ Gets all Azure policies definitions in cloudtamer.io and returns them paginated.

    Args:
        page (int | Unset):
        count (int | Unset):
        sort_method (str | Unset):
        sort_order (str | Unset):  Default: 'ASC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAzurePolicyPaginatedIndexResponse200 | GetAzurePolicyPaginatedIndexResponse400 | GetAzurePolicyPaginatedIndexResponse401 | GetAzurePolicyPaginatedIndexResponse403 | GetAzurePolicyPaginatedIndexResponse500
     """


    return sync_detailed(
        client=client,
page=page,
count=count,
sort_method=sort_method,
sort_order=sort_order,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    count: int | Unset = UNSET,
    sort_method: str | Unset = UNSET,
    sort_order: str | Unset = 'ASC',

) -> Response[GetAzurePolicyPaginatedIndexResponse200 | GetAzurePolicyPaginatedIndexResponse400 | GetAzurePolicyPaginatedIndexResponse401 | GetAzurePolicyPaginatedIndexResponse403 | GetAzurePolicyPaginatedIndexResponse500]:
    """ Gets all Azure policies definitions in cloudtamer.io and returns them paginated.

    Args:
        page (int | Unset):
        count (int | Unset):
        sort_method (str | Unset):
        sort_order (str | Unset):  Default: 'ASC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAzurePolicyPaginatedIndexResponse200 | GetAzurePolicyPaginatedIndexResponse400 | GetAzurePolicyPaginatedIndexResponse401 | GetAzurePolicyPaginatedIndexResponse403 | GetAzurePolicyPaginatedIndexResponse500]
     """


    kwargs = _get_kwargs(
        page=page,
count=count,
sort_method=sort_method,
sort_order=sort_order,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    count: int | Unset = UNSET,
    sort_method: str | Unset = UNSET,
    sort_order: str | Unset = 'ASC',

) -> GetAzurePolicyPaginatedIndexResponse200 | GetAzurePolicyPaginatedIndexResponse400 | GetAzurePolicyPaginatedIndexResponse401 | GetAzurePolicyPaginatedIndexResponse403 | GetAzurePolicyPaginatedIndexResponse500 | None:
    """ Gets all Azure policies definitions in cloudtamer.io and returns them paginated.

    Args:
        page (int | Unset):
        count (int | Unset):
        sort_method (str | Unset):
        sort_order (str | Unset):  Default: 'ASC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAzurePolicyPaginatedIndexResponse200 | GetAzurePolicyPaginatedIndexResponse400 | GetAzurePolicyPaginatedIndexResponse401 | GetAzurePolicyPaginatedIndexResponse403 | GetAzurePolicyPaginatedIndexResponse500
     """


    return (await asyncio_detailed(
        client=client,
page=page,
count=count,
sort_method=sort_method,
sort_order=sort_order,

    )).parsed
