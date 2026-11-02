from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_compliance_o_us_paginated_response_200 import GetComplianceOUsPaginatedResponse200
from ...models.get_compliance_o_us_paginated_response_400 import GetComplianceOUsPaginatedResponse400
from ...models.get_compliance_o_us_paginated_response_401 import GetComplianceOUsPaginatedResponse401
from ...models.get_compliance_o_us_paginated_response_403 import GetComplianceOUsPaginatedResponse403
from ...models.get_compliance_o_us_paginated_response_500 import GetComplianceOUsPaginatedResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    non_compliant: bool | Unset = False,
    detailed: bool | Unset = True,
    standard_id: int | Unset = UNSET,
    check_id: int | Unset = UNSET,
    page: int | Unset = 1,
    count: int | Unset = 15,
    query: str | Unset = UNSET,
    sort_method: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["non_compliant"] = non_compliant

    params["detailed"] = detailed

    params["standard_id"] = standard_id

    params["check_id"] = check_id

    params["page"] = page

    params["count"] = count

    params["query"] = query

    params["sortMethod"] = sort_method

    params["sortOrder"] = sort_order


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v4/compliance/ou",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetComplianceOUsPaginatedResponse200 | GetComplianceOUsPaginatedResponse400 | GetComplianceOUsPaginatedResponse401 | GetComplianceOUsPaginatedResponse403 | GetComplianceOUsPaginatedResponse500 | None:
    if response.status_code == 200:
        response_200 = GetComplianceOUsPaginatedResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetComplianceOUsPaginatedResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetComplianceOUsPaginatedResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetComplianceOUsPaginatedResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetComplianceOUsPaginatedResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetComplianceOUsPaginatedResponse200 | GetComplianceOUsPaginatedResponse400 | GetComplianceOUsPaginatedResponse401 | GetComplianceOUsPaginatedResponse403 | GetComplianceOUsPaginatedResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    non_compliant: bool | Unset = False,
    detailed: bool | Unset = True,
    standard_id: int | Unset = UNSET,
    check_id: int | Unset = UNSET,
    page: int | Unset = 1,
    count: int | Unset = 15,
    query: str | Unset = UNSET,
    sort_method: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,

) -> Response[GetComplianceOUsPaginatedResponse200 | GetComplianceOUsPaginatedResponse400 | GetComplianceOUsPaginatedResponse401 | GetComplianceOUsPaginatedResponse403 | GetComplianceOUsPaginatedResponse500]:
    """ Finds a paginated ou list based on their compliance records.

    Args:
        non_compliant (bool | Unset):  Default: False.
        detailed (bool | Unset):  Default: True.
        standard_id (int | Unset):
        check_id (int | Unset):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 15.
        query (str | Unset):
        sort_method (str | Unset):
        sort_order (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetComplianceOUsPaginatedResponse200 | GetComplianceOUsPaginatedResponse400 | GetComplianceOUsPaginatedResponse401 | GetComplianceOUsPaginatedResponse403 | GetComplianceOUsPaginatedResponse500]
     """


    kwargs = _get_kwargs(
        non_compliant=non_compliant,
detailed=detailed,
standard_id=standard_id,
check_id=check_id,
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
    non_compliant: bool | Unset = False,
    detailed: bool | Unset = True,
    standard_id: int | Unset = UNSET,
    check_id: int | Unset = UNSET,
    page: int | Unset = 1,
    count: int | Unset = 15,
    query: str | Unset = UNSET,
    sort_method: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,

) -> GetComplianceOUsPaginatedResponse200 | GetComplianceOUsPaginatedResponse400 | GetComplianceOUsPaginatedResponse401 | GetComplianceOUsPaginatedResponse403 | GetComplianceOUsPaginatedResponse500 | None:
    """ Finds a paginated ou list based on their compliance records.

    Args:
        non_compliant (bool | Unset):  Default: False.
        detailed (bool | Unset):  Default: True.
        standard_id (int | Unset):
        check_id (int | Unset):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 15.
        query (str | Unset):
        sort_method (str | Unset):
        sort_order (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetComplianceOUsPaginatedResponse200 | GetComplianceOUsPaginatedResponse400 | GetComplianceOUsPaginatedResponse401 | GetComplianceOUsPaginatedResponse403 | GetComplianceOUsPaginatedResponse500
     """


    return sync_detailed(
        client=client,
non_compliant=non_compliant,
detailed=detailed,
standard_id=standard_id,
check_id=check_id,
page=page,
count=count,
query=query,
sort_method=sort_method,
sort_order=sort_order,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    non_compliant: bool | Unset = False,
    detailed: bool | Unset = True,
    standard_id: int | Unset = UNSET,
    check_id: int | Unset = UNSET,
    page: int | Unset = 1,
    count: int | Unset = 15,
    query: str | Unset = UNSET,
    sort_method: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,

) -> Response[GetComplianceOUsPaginatedResponse200 | GetComplianceOUsPaginatedResponse400 | GetComplianceOUsPaginatedResponse401 | GetComplianceOUsPaginatedResponse403 | GetComplianceOUsPaginatedResponse500]:
    """ Finds a paginated ou list based on their compliance records.

    Args:
        non_compliant (bool | Unset):  Default: False.
        detailed (bool | Unset):  Default: True.
        standard_id (int | Unset):
        check_id (int | Unset):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 15.
        query (str | Unset):
        sort_method (str | Unset):
        sort_order (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetComplianceOUsPaginatedResponse200 | GetComplianceOUsPaginatedResponse400 | GetComplianceOUsPaginatedResponse401 | GetComplianceOUsPaginatedResponse403 | GetComplianceOUsPaginatedResponse500]
     """


    kwargs = _get_kwargs(
        non_compliant=non_compliant,
detailed=detailed,
standard_id=standard_id,
check_id=check_id,
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
    non_compliant: bool | Unset = False,
    detailed: bool | Unset = True,
    standard_id: int | Unset = UNSET,
    check_id: int | Unset = UNSET,
    page: int | Unset = 1,
    count: int | Unset = 15,
    query: str | Unset = UNSET,
    sort_method: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,

) -> GetComplianceOUsPaginatedResponse200 | GetComplianceOUsPaginatedResponse400 | GetComplianceOUsPaginatedResponse401 | GetComplianceOUsPaginatedResponse403 | GetComplianceOUsPaginatedResponse500 | None:
    """ Finds a paginated ou list based on their compliance records.

    Args:
        non_compliant (bool | Unset):  Default: False.
        detailed (bool | Unset):  Default: True.
        standard_id (int | Unset):
        check_id (int | Unset):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 15.
        query (str | Unset):
        sort_method (str | Unset):
        sort_order (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetComplianceOUsPaginatedResponse200 | GetComplianceOUsPaginatedResponse400 | GetComplianceOUsPaginatedResponse401 | GetComplianceOUsPaginatedResponse403 | GetComplianceOUsPaginatedResponse500
     """


    return (await asyncio_detailed(
        client=client,
non_compliant=non_compliant,
detailed=detailed,
standard_id=standard_id,
check_id=check_id,
page=page,
count=count,
query=query,
sort_method=sort_method,
sort_order=sort_order,

    )).parsed
