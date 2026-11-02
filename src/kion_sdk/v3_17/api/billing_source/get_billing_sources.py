from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_billing_sources_response_200 import GetBillingSourcesResponse200
from ...models.get_billing_sources_response_400 import GetBillingSourcesResponse400
from ...models.get_billing_sources_response_401 import GetBillingSourcesResponse401
from ...models.get_billing_sources_response_403 import GetBillingSourcesResponse403
from ...models.get_billing_sources_response_500 import GetBillingSourcesResponse500
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
        "url": "/v4/billing-source",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetBillingSourcesResponse200 | GetBillingSourcesResponse400 | GetBillingSourcesResponse401 | GetBillingSourcesResponse403 | GetBillingSourcesResponse500 | None:
    if response.status_code == 200:
        response_200 = GetBillingSourcesResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetBillingSourcesResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetBillingSourcesResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetBillingSourcesResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetBillingSourcesResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetBillingSourcesResponse200 | GetBillingSourcesResponse400 | GetBillingSourcesResponse401 | GetBillingSourcesResponse403 | GetBillingSourcesResponse500]:
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

) -> Response[GetBillingSourcesResponse200 | GetBillingSourcesResponse400 | GetBillingSourcesResponse401 | GetBillingSourcesResponse403 | GetBillingSourcesResponse500]:
    """ Gets all billing sources in the system.

    Args:
        page (int | Unset):
        count (int | Unset):
        sort_method (str | Unset):
        sort_order (str | Unset):  Default: 'ASC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBillingSourcesResponse200 | GetBillingSourcesResponse400 | GetBillingSourcesResponse401 | GetBillingSourcesResponse403 | GetBillingSourcesResponse500]
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

) -> GetBillingSourcesResponse200 | GetBillingSourcesResponse400 | GetBillingSourcesResponse401 | GetBillingSourcesResponse403 | GetBillingSourcesResponse500 | None:
    """ Gets all billing sources in the system.

    Args:
        page (int | Unset):
        count (int | Unset):
        sort_method (str | Unset):
        sort_order (str | Unset):  Default: 'ASC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBillingSourcesResponse200 | GetBillingSourcesResponse400 | GetBillingSourcesResponse401 | GetBillingSourcesResponse403 | GetBillingSourcesResponse500
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

) -> Response[GetBillingSourcesResponse200 | GetBillingSourcesResponse400 | GetBillingSourcesResponse401 | GetBillingSourcesResponse403 | GetBillingSourcesResponse500]:
    """ Gets all billing sources in the system.

    Args:
        page (int | Unset):
        count (int | Unset):
        sort_method (str | Unset):
        sort_order (str | Unset):  Default: 'ASC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetBillingSourcesResponse200 | GetBillingSourcesResponse400 | GetBillingSourcesResponse401 | GetBillingSourcesResponse403 | GetBillingSourcesResponse500]
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

) -> GetBillingSourcesResponse200 | GetBillingSourcesResponse400 | GetBillingSourcesResponse401 | GetBillingSourcesResponse403 | GetBillingSourcesResponse500 | None:
    """ Gets all billing sources in the system.

    Args:
        page (int | Unset):
        count (int | Unset):
        sort_method (str | Unset):
        sort_order (str | Unset):  Default: 'ASC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetBillingSourcesResponse200 | GetBillingSourcesResponse400 | GetBillingSourcesResponse401 | GetBillingSourcesResponse403 | GetBillingSourcesResponse500
     """


    return (await asyncio_detailed(
        client=client,
page=page,
count=count,
sort_method=sort_method,
sort_order=sort_order,

    )).parsed
