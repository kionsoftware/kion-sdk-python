from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_all_global_custom_variables_response_200 import GetAllGlobalCustomVariablesResponse200
from ...models.get_all_global_custom_variables_response_400 import GetAllGlobalCustomVariablesResponse400
from ...models.get_all_global_custom_variables_response_401 import GetAllGlobalCustomVariablesResponse401
from ...models.get_all_global_custom_variables_response_403 import GetAllGlobalCustomVariablesResponse403
from ...models.get_all_global_custom_variables_response_500 import GetAllGlobalCustomVariablesResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    page: int | Unset = 1,
    count: int | Unset = 10,
    sort_method: str | Unset = 'alphabetical',
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
        "url": "/v3/custom-variable",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetAllGlobalCustomVariablesResponse200 | GetAllGlobalCustomVariablesResponse400 | GetAllGlobalCustomVariablesResponse401 | GetAllGlobalCustomVariablesResponse403 | GetAllGlobalCustomVariablesResponse500 | None:
    if response.status_code == 200:
        response_200 = GetAllGlobalCustomVariablesResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetAllGlobalCustomVariablesResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetAllGlobalCustomVariablesResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetAllGlobalCustomVariablesResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetAllGlobalCustomVariablesResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetAllGlobalCustomVariablesResponse200 | GetAllGlobalCustomVariablesResponse400 | GetAllGlobalCustomVariablesResponse401 | GetAllGlobalCustomVariablesResponse403 | GetAllGlobalCustomVariablesResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    count: int | Unset = 10,
    sort_method: str | Unset = 'alphabetical',
    sort_order: str | Unset = 'ASC',

) -> Response[GetAllGlobalCustomVariablesResponse200 | GetAllGlobalCustomVariablesResponse400 | GetAllGlobalCustomVariablesResponse401 | GetAllGlobalCustomVariablesResponse403 | GetAllGlobalCustomVariablesResponse500]:
    """ Gets all global custom variables.

    Args:
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        sort_method (str | Unset):  Default: 'alphabetical'.
        sort_order (str | Unset):  Default: 'ASC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllGlobalCustomVariablesResponse200 | GetAllGlobalCustomVariablesResponse400 | GetAllGlobalCustomVariablesResponse401 | GetAllGlobalCustomVariablesResponse403 | GetAllGlobalCustomVariablesResponse500]
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
    page: int | Unset = 1,
    count: int | Unset = 10,
    sort_method: str | Unset = 'alphabetical',
    sort_order: str | Unset = 'ASC',

) -> GetAllGlobalCustomVariablesResponse200 | GetAllGlobalCustomVariablesResponse400 | GetAllGlobalCustomVariablesResponse401 | GetAllGlobalCustomVariablesResponse403 | GetAllGlobalCustomVariablesResponse500 | None:
    """ Gets all global custom variables.

    Args:
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        sort_method (str | Unset):  Default: 'alphabetical'.
        sort_order (str | Unset):  Default: 'ASC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllGlobalCustomVariablesResponse200 | GetAllGlobalCustomVariablesResponse400 | GetAllGlobalCustomVariablesResponse401 | GetAllGlobalCustomVariablesResponse403 | GetAllGlobalCustomVariablesResponse500
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
    page: int | Unset = 1,
    count: int | Unset = 10,
    sort_method: str | Unset = 'alphabetical',
    sort_order: str | Unset = 'ASC',

) -> Response[GetAllGlobalCustomVariablesResponse200 | GetAllGlobalCustomVariablesResponse400 | GetAllGlobalCustomVariablesResponse401 | GetAllGlobalCustomVariablesResponse403 | GetAllGlobalCustomVariablesResponse500]:
    """ Gets all global custom variables.

    Args:
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        sort_method (str | Unset):  Default: 'alphabetical'.
        sort_order (str | Unset):  Default: 'ASC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllGlobalCustomVariablesResponse200 | GetAllGlobalCustomVariablesResponse400 | GetAllGlobalCustomVariablesResponse401 | GetAllGlobalCustomVariablesResponse403 | GetAllGlobalCustomVariablesResponse500]
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
    page: int | Unset = 1,
    count: int | Unset = 10,
    sort_method: str | Unset = 'alphabetical',
    sort_order: str | Unset = 'ASC',

) -> GetAllGlobalCustomVariablesResponse200 | GetAllGlobalCustomVariablesResponse400 | GetAllGlobalCustomVariablesResponse401 | GetAllGlobalCustomVariablesResponse403 | GetAllGlobalCustomVariablesResponse500 | None:
    """ Gets all global custom variables.

    Args:
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        sort_method (str | Unset):  Default: 'alphabetical'.
        sort_order (str | Unset):  Default: 'ASC'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllGlobalCustomVariablesResponse200 | GetAllGlobalCustomVariablesResponse400 | GetAllGlobalCustomVariablesResponse401 | GetAllGlobalCustomVariablesResponse403 | GetAllGlobalCustomVariablesResponse500
     """


    return (await asyncio_detailed(
        client=client,
page=page,
count=count,
sort_method=sort_method,
sort_order=sort_order,

    )).parsed
