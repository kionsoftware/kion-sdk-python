from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_compliance_program_paginated_index_response_200 import GetComplianceProgramPaginatedIndexResponse200
from ...models.get_compliance_program_paginated_index_response_400 import GetComplianceProgramPaginatedIndexResponse400
from ...models.get_compliance_program_paginated_index_response_401 import GetComplianceProgramPaginatedIndexResponse401
from ...models.get_compliance_program_paginated_index_response_403 import GetComplianceProgramPaginatedIndexResponse403
from ...models.get_compliance_program_paginated_index_response_500 import GetComplianceProgramPaginatedIndexResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    system_managed_only: bool | Unset = UNSET,
    page: int | Unset = 1,
    count: int | Unset = 10,
    query: str | Unset = UNSET,
    sort_method: str | Unset = UNSET,
    sort_order: str | Unset = 'ASC',

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["system_managed_only"] = system_managed_only

    params["page"] = page

    params["count"] = count

    params["query"] = query

    params["sortMethod"] = sort_method

    params["sortOrder"] = sort_order


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v4/compliance/program",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetComplianceProgramPaginatedIndexResponse200 | GetComplianceProgramPaginatedIndexResponse400 | GetComplianceProgramPaginatedIndexResponse401 | GetComplianceProgramPaginatedIndexResponse403 | GetComplianceProgramPaginatedIndexResponse500 | None:
    if response.status_code == 200:
        response_200 = GetComplianceProgramPaginatedIndexResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetComplianceProgramPaginatedIndexResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetComplianceProgramPaginatedIndexResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetComplianceProgramPaginatedIndexResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetComplianceProgramPaginatedIndexResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetComplianceProgramPaginatedIndexResponse200 | GetComplianceProgramPaginatedIndexResponse400 | GetComplianceProgramPaginatedIndexResponse401 | GetComplianceProgramPaginatedIndexResponse403 | GetComplianceProgramPaginatedIndexResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    system_managed_only: bool | Unset = UNSET,
    page: int | Unset = 1,
    count: int | Unset = 10,
    query: str | Unset = UNSET,
    sort_method: str | Unset = UNSET,
    sort_order: str | Unset = 'ASC',

) -> Response[GetComplianceProgramPaginatedIndexResponse200 | GetComplianceProgramPaginatedIndexResponse400 | GetComplianceProgramPaginatedIndexResponse401 | GetComplianceProgramPaginatedIndexResponse403 | GetComplianceProgramPaginatedIndexResponse500]:
    """ Returns a paginated list of Compliance Programs from the application.

    Args:
        system_managed_only (bool | Unset):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        query (str | Unset):
        sort_method (str | Unset):
        sort_order (str | Unset):  Default: 'ASC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetComplianceProgramPaginatedIndexResponse200 | GetComplianceProgramPaginatedIndexResponse400 | GetComplianceProgramPaginatedIndexResponse401 | GetComplianceProgramPaginatedIndexResponse403 | GetComplianceProgramPaginatedIndexResponse500]
     """


    kwargs = _get_kwargs(
        system_managed_only=system_managed_only,
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
    *,
    client: AuthenticatedClient,
    system_managed_only: bool | Unset = UNSET,
    page: int | Unset = 1,
    count: int | Unset = 10,
    query: str | Unset = UNSET,
    sort_method: str | Unset = UNSET,
    sort_order: str | Unset = 'ASC',

) -> GetComplianceProgramPaginatedIndexResponse200 | GetComplianceProgramPaginatedIndexResponse400 | GetComplianceProgramPaginatedIndexResponse401 | GetComplianceProgramPaginatedIndexResponse403 | GetComplianceProgramPaginatedIndexResponse500 | None:
    """ Returns a paginated list of Compliance Programs from the application.

    Args:
        system_managed_only (bool | Unset):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        query (str | Unset):
        sort_method (str | Unset):
        sort_order (str | Unset):  Default: 'ASC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetComplianceProgramPaginatedIndexResponse200 | GetComplianceProgramPaginatedIndexResponse400 | GetComplianceProgramPaginatedIndexResponse401 | GetComplianceProgramPaginatedIndexResponse403 | GetComplianceProgramPaginatedIndexResponse500
     """


    return sync_detailed(
        client=client,
system_managed_only=system_managed_only,
page=page,
count=count,
query=query,
sort_method=sort_method,
sort_order=sort_order,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    system_managed_only: bool | Unset = UNSET,
    page: int | Unset = 1,
    count: int | Unset = 10,
    query: str | Unset = UNSET,
    sort_method: str | Unset = UNSET,
    sort_order: str | Unset = 'ASC',

) -> Response[GetComplianceProgramPaginatedIndexResponse200 | GetComplianceProgramPaginatedIndexResponse400 | GetComplianceProgramPaginatedIndexResponse401 | GetComplianceProgramPaginatedIndexResponse403 | GetComplianceProgramPaginatedIndexResponse500]:
    """ Returns a paginated list of Compliance Programs from the application.

    Args:
        system_managed_only (bool | Unset):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        query (str | Unset):
        sort_method (str | Unset):
        sort_order (str | Unset):  Default: 'ASC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetComplianceProgramPaginatedIndexResponse200 | GetComplianceProgramPaginatedIndexResponse400 | GetComplianceProgramPaginatedIndexResponse401 | GetComplianceProgramPaginatedIndexResponse403 | GetComplianceProgramPaginatedIndexResponse500]
     """


    kwargs = _get_kwargs(
        system_managed_only=system_managed_only,
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
    *,
    client: AuthenticatedClient,
    system_managed_only: bool | Unset = UNSET,
    page: int | Unset = 1,
    count: int | Unset = 10,
    query: str | Unset = UNSET,
    sort_method: str | Unset = UNSET,
    sort_order: str | Unset = 'ASC',

) -> GetComplianceProgramPaginatedIndexResponse200 | GetComplianceProgramPaginatedIndexResponse400 | GetComplianceProgramPaginatedIndexResponse401 | GetComplianceProgramPaginatedIndexResponse403 | GetComplianceProgramPaginatedIndexResponse500 | None:
    """ Returns a paginated list of Compliance Programs from the application.

    Args:
        system_managed_only (bool | Unset):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        query (str | Unset):
        sort_method (str | Unset):
        sort_order (str | Unset):  Default: 'ASC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetComplianceProgramPaginatedIndexResponse200 | GetComplianceProgramPaginatedIndexResponse400 | GetComplianceProgramPaginatedIndexResponse401 | GetComplianceProgramPaginatedIndexResponse403 | GetComplianceProgramPaginatedIndexResponse500
     """


    return (await asyncio_detailed(
        client=client,
system_managed_only=system_managed_only,
page=page,
count=count,
query=query,
sort_method=sort_method,
sort_order=sort_order,

    )).parsed
