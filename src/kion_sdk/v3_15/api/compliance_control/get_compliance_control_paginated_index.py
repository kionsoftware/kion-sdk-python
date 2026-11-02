from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_compliance_control_paginated_index_response_200 import GetComplianceControlPaginatedIndexResponse200
from ...models.get_compliance_control_paginated_index_response_400 import GetComplianceControlPaginatedIndexResponse400
from ...models.get_compliance_control_paginated_index_response_401 import GetComplianceControlPaginatedIndexResponse401
from ...models.get_compliance_control_paginated_index_response_403 import GetComplianceControlPaginatedIndexResponse403
from ...models.get_compliance_control_paginated_index_response_500 import GetComplianceControlPaginatedIndexResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    page: int | Unset = 1,
    count: int | Unset = 10,
    query: str | Unset = UNSET,
    sort_method: str | Unset = UNSET,
    sort_order: str | Unset = 'ASC',

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["count"] = count

    params["query"] = query

    params["sortMethod"] = sort_method

    params["sortOrder"] = sort_order


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v4/compliance/program/{id}/control".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetComplianceControlPaginatedIndexResponse200 | GetComplianceControlPaginatedIndexResponse400 | GetComplianceControlPaginatedIndexResponse401 | GetComplianceControlPaginatedIndexResponse403 | GetComplianceControlPaginatedIndexResponse500 | None:
    if response.status_code == 200:
        response_200 = GetComplianceControlPaginatedIndexResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetComplianceControlPaginatedIndexResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetComplianceControlPaginatedIndexResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetComplianceControlPaginatedIndexResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetComplianceControlPaginatedIndexResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetComplianceControlPaginatedIndexResponse200 | GetComplianceControlPaginatedIndexResponse400 | GetComplianceControlPaginatedIndexResponse401 | GetComplianceControlPaginatedIndexResponse403 | GetComplianceControlPaginatedIndexResponse500]:
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
    count: int | Unset = 10,
    query: str | Unset = UNSET,
    sort_method: str | Unset = UNSET,
    sort_order: str | Unset = 'ASC',

) -> Response[GetComplianceControlPaginatedIndexResponse200 | GetComplianceControlPaginatedIndexResponse400 | GetComplianceControlPaginatedIndexResponse401 | GetComplianceControlPaginatedIndexResponse403 | GetComplianceControlPaginatedIndexResponse500]:
    """ Returns a paginated list of Compliance Controls from the application.

    Args:
        id (int):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        query (str | Unset):
        sort_method (str | Unset):
        sort_order (str | Unset):  Default: 'ASC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetComplianceControlPaginatedIndexResponse200 | GetComplianceControlPaginatedIndexResponse400 | GetComplianceControlPaginatedIndexResponse401 | GetComplianceControlPaginatedIndexResponse403 | GetComplianceControlPaginatedIndexResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
page=page,
count=count,
query=query,
sort_method=sort_method,
sort_order=sort_order,

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
    count: int | Unset = 10,
    query: str | Unset = UNSET,
    sort_method: str | Unset = UNSET,
    sort_order: str | Unset = 'ASC',

) -> GetComplianceControlPaginatedIndexResponse200 | GetComplianceControlPaginatedIndexResponse400 | GetComplianceControlPaginatedIndexResponse401 | GetComplianceControlPaginatedIndexResponse403 | GetComplianceControlPaginatedIndexResponse500 | None:
    """ Returns a paginated list of Compliance Controls from the application.

    Args:
        id (int):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        query (str | Unset):
        sort_method (str | Unset):
        sort_order (str | Unset):  Default: 'ASC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetComplianceControlPaginatedIndexResponse200 | GetComplianceControlPaginatedIndexResponse400 | GetComplianceControlPaginatedIndexResponse401 | GetComplianceControlPaginatedIndexResponse403 | GetComplianceControlPaginatedIndexResponse500
     """


    return sync_detailed(
        id=id,
client=client,
page=page,
count=count,
query=query,
sort_method=sort_method,
sort_order=sort_order,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    count: int | Unset = 10,
    query: str | Unset = UNSET,
    sort_method: str | Unset = UNSET,
    sort_order: str | Unset = 'ASC',

) -> Response[GetComplianceControlPaginatedIndexResponse200 | GetComplianceControlPaginatedIndexResponse400 | GetComplianceControlPaginatedIndexResponse401 | GetComplianceControlPaginatedIndexResponse403 | GetComplianceControlPaginatedIndexResponse500]:
    """ Returns a paginated list of Compliance Controls from the application.

    Args:
        id (int):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        query (str | Unset):
        sort_method (str | Unset):
        sort_order (str | Unset):  Default: 'ASC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetComplianceControlPaginatedIndexResponse200 | GetComplianceControlPaginatedIndexResponse400 | GetComplianceControlPaginatedIndexResponse401 | GetComplianceControlPaginatedIndexResponse403 | GetComplianceControlPaginatedIndexResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
page=page,
count=count,
query=query,
sort_method=sort_method,
sort_order=sort_order,

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
    count: int | Unset = 10,
    query: str | Unset = UNSET,
    sort_method: str | Unset = UNSET,
    sort_order: str | Unset = 'ASC',

) -> GetComplianceControlPaginatedIndexResponse200 | GetComplianceControlPaginatedIndexResponse400 | GetComplianceControlPaginatedIndexResponse401 | GetComplianceControlPaginatedIndexResponse403 | GetComplianceControlPaginatedIndexResponse500 | None:
    """ Returns a paginated list of Compliance Controls from the application.

    Args:
        id (int):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        query (str | Unset):
        sort_method (str | Unset):
        sort_order (str | Unset):  Default: 'ASC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetComplianceControlPaginatedIndexResponse200 | GetComplianceControlPaginatedIndexResponse400 | GetComplianceControlPaginatedIndexResponse401 | GetComplianceControlPaginatedIndexResponse403 | GetComplianceControlPaginatedIndexResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
page=page,
count=count,
query=query,
sort_method=sort_method,
sort_order=sort_order,

    )).parsed
