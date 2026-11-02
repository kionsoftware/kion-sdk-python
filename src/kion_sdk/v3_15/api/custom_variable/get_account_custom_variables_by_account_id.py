from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_account_custom_variables_by_account_id_response_200 import GetAccountCustomVariablesByAccountIDResponse200
from ...models.get_account_custom_variables_by_account_id_response_400 import GetAccountCustomVariablesByAccountIDResponse400
from ...models.get_account_custom_variables_by_account_id_response_401 import GetAccountCustomVariablesByAccountIDResponse401
from ...models.get_account_custom_variables_by_account_id_response_403 import GetAccountCustomVariablesByAccountIDResponse403
from ...models.get_account_custom_variables_by_account_id_response_404 import GetAccountCustomVariablesByAccountIDResponse404
from ...models.get_account_custom_variables_by_account_id_response_500 import GetAccountCustomVariablesByAccountIDResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    account_id: int,
    *,
    page: int | Unset = 1,
    count: int | Unset = 10,
    sort_method: str | Unset = 'alphabetical',
    sort_order: str | Unset = 'ASC',
    keyword: str | Unset = '\\"\\"',

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["count"] = count

    params["sortMethod"] = sort_method

    params["sortOrder"] = sort_order

    params["keyword"] = keyword


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/account/{account_id}/custom-variable".format(account_id=quote(str(account_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetAccountCustomVariablesByAccountIDResponse200 | GetAccountCustomVariablesByAccountIDResponse400 | GetAccountCustomVariablesByAccountIDResponse401 | GetAccountCustomVariablesByAccountIDResponse403 | GetAccountCustomVariablesByAccountIDResponse404 | GetAccountCustomVariablesByAccountIDResponse500 | None:
    if response.status_code == 200:
        response_200 = GetAccountCustomVariablesByAccountIDResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetAccountCustomVariablesByAccountIDResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetAccountCustomVariablesByAccountIDResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetAccountCustomVariablesByAccountIDResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetAccountCustomVariablesByAccountIDResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetAccountCustomVariablesByAccountIDResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetAccountCustomVariablesByAccountIDResponse200 | GetAccountCustomVariablesByAccountIDResponse400 | GetAccountCustomVariablesByAccountIDResponse401 | GetAccountCustomVariablesByAccountIDResponse403 | GetAccountCustomVariablesByAccountIDResponse404 | GetAccountCustomVariablesByAccountIDResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    count: int | Unset = 10,
    sort_method: str | Unset = 'alphabetical',
    sort_order: str | Unset = 'ASC',
    keyword: str | Unset = '\\"\\"',

) -> Response[GetAccountCustomVariablesByAccountIDResponse200 | GetAccountCustomVariablesByAccountIDResponse400 | GetAccountCustomVariablesByAccountIDResponse401 | GetAccountCustomVariablesByAccountIDResponse403 | GetAccountCustomVariablesByAccountIDResponse404 | GetAccountCustomVariablesByAccountIDResponse500]:
    r""" Returns a list of account custom variable overrides.

    Args:
        account_id (int):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        sort_method (str | Unset):  Default: 'alphabetical'.
        sort_order (str | Unset):  Default: 'ASC'.
        keyword (str | Unset):  Default: '\\"\\"'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountCustomVariablesByAccountIDResponse200 | GetAccountCustomVariablesByAccountIDResponse400 | GetAccountCustomVariablesByAccountIDResponse401 | GetAccountCustomVariablesByAccountIDResponse403 | GetAccountCustomVariablesByAccountIDResponse404 | GetAccountCustomVariablesByAccountIDResponse500]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
page=page,
count=count,
sort_method=sort_method,
sort_order=sort_order,
keyword=keyword,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    account_id: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    count: int | Unset = 10,
    sort_method: str | Unset = 'alphabetical',
    sort_order: str | Unset = 'ASC',
    keyword: str | Unset = '\\"\\"',

) -> GetAccountCustomVariablesByAccountIDResponse200 | GetAccountCustomVariablesByAccountIDResponse400 | GetAccountCustomVariablesByAccountIDResponse401 | GetAccountCustomVariablesByAccountIDResponse403 | GetAccountCustomVariablesByAccountIDResponse404 | GetAccountCustomVariablesByAccountIDResponse500 | None:
    r""" Returns a list of account custom variable overrides.

    Args:
        account_id (int):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        sort_method (str | Unset):  Default: 'alphabetical'.
        sort_order (str | Unset):  Default: 'ASC'.
        keyword (str | Unset):  Default: '\\"\\"'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountCustomVariablesByAccountIDResponse200 | GetAccountCustomVariablesByAccountIDResponse400 | GetAccountCustomVariablesByAccountIDResponse401 | GetAccountCustomVariablesByAccountIDResponse403 | GetAccountCustomVariablesByAccountIDResponse404 | GetAccountCustomVariablesByAccountIDResponse500
     """


    return sync_detailed(
        account_id=account_id,
client=client,
page=page,
count=count,
sort_method=sort_method,
sort_order=sort_order,
keyword=keyword,

    ).parsed

async def asyncio_detailed(
    account_id: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    count: int | Unset = 10,
    sort_method: str | Unset = 'alphabetical',
    sort_order: str | Unset = 'ASC',
    keyword: str | Unset = '\\"\\"',

) -> Response[GetAccountCustomVariablesByAccountIDResponse200 | GetAccountCustomVariablesByAccountIDResponse400 | GetAccountCustomVariablesByAccountIDResponse401 | GetAccountCustomVariablesByAccountIDResponse403 | GetAccountCustomVariablesByAccountIDResponse404 | GetAccountCustomVariablesByAccountIDResponse500]:
    r""" Returns a list of account custom variable overrides.

    Args:
        account_id (int):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        sort_method (str | Unset):  Default: 'alphabetical'.
        sort_order (str | Unset):  Default: 'ASC'.
        keyword (str | Unset):  Default: '\\"\\"'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountCustomVariablesByAccountIDResponse200 | GetAccountCustomVariablesByAccountIDResponse400 | GetAccountCustomVariablesByAccountIDResponse401 | GetAccountCustomVariablesByAccountIDResponse403 | GetAccountCustomVariablesByAccountIDResponse404 | GetAccountCustomVariablesByAccountIDResponse500]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
page=page,
count=count,
sort_method=sort_method,
sort_order=sort_order,
keyword=keyword,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    account_id: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    count: int | Unset = 10,
    sort_method: str | Unset = 'alphabetical',
    sort_order: str | Unset = 'ASC',
    keyword: str | Unset = '\\"\\"',

) -> GetAccountCustomVariablesByAccountIDResponse200 | GetAccountCustomVariablesByAccountIDResponse400 | GetAccountCustomVariablesByAccountIDResponse401 | GetAccountCustomVariablesByAccountIDResponse403 | GetAccountCustomVariablesByAccountIDResponse404 | GetAccountCustomVariablesByAccountIDResponse500 | None:
    r""" Returns a list of account custom variable overrides.

    Args:
        account_id (int):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        sort_method (str | Unset):  Default: 'alphabetical'.
        sort_order (str | Unset):  Default: 'ASC'.
        keyword (str | Unset):  Default: '\\"\\"'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountCustomVariablesByAccountIDResponse200 | GetAccountCustomVariablesByAccountIDResponse400 | GetAccountCustomVariablesByAccountIDResponse401 | GetAccountCustomVariablesByAccountIDResponse403 | GetAccountCustomVariablesByAccountIDResponse404 | GetAccountCustomVariablesByAccountIDResponse500
     """


    return (await asyncio_detailed(
        account_id=account_id,
client=client,
page=page,
count=count,
sort_method=sort_method,
sort_order=sort_order,
keyword=keyword,

    )).parsed
