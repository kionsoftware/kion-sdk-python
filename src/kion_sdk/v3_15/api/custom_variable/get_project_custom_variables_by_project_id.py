from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_project_custom_variables_by_project_id_response_200 import GetProjectCustomVariablesByProjectIDResponse200
from ...models.get_project_custom_variables_by_project_id_response_400 import GetProjectCustomVariablesByProjectIDResponse400
from ...models.get_project_custom_variables_by_project_id_response_401 import GetProjectCustomVariablesByProjectIDResponse401
from ...models.get_project_custom_variables_by_project_id_response_403 import GetProjectCustomVariablesByProjectIDResponse403
from ...models.get_project_custom_variables_by_project_id_response_404 import GetProjectCustomVariablesByProjectIDResponse404
from ...models.get_project_custom_variables_by_project_id_response_500 import GetProjectCustomVariablesByProjectIDResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    project_id: int,
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
        "url": "/v3/project/{project_id}/custom-variable".format(project_id=quote(str(project_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetProjectCustomVariablesByProjectIDResponse200 | GetProjectCustomVariablesByProjectIDResponse400 | GetProjectCustomVariablesByProjectIDResponse401 | GetProjectCustomVariablesByProjectIDResponse403 | GetProjectCustomVariablesByProjectIDResponse404 | GetProjectCustomVariablesByProjectIDResponse500 | None:
    if response.status_code == 200:
        response_200 = GetProjectCustomVariablesByProjectIDResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetProjectCustomVariablesByProjectIDResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetProjectCustomVariablesByProjectIDResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetProjectCustomVariablesByProjectIDResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetProjectCustomVariablesByProjectIDResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetProjectCustomVariablesByProjectIDResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetProjectCustomVariablesByProjectIDResponse200 | GetProjectCustomVariablesByProjectIDResponse400 | GetProjectCustomVariablesByProjectIDResponse401 | GetProjectCustomVariablesByProjectIDResponse403 | GetProjectCustomVariablesByProjectIDResponse404 | GetProjectCustomVariablesByProjectIDResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    count: int | Unset = 10,
    sort_method: str | Unset = 'alphabetical',
    sort_order: str | Unset = 'ASC',
    keyword: str | Unset = '\\"\\"',

) -> Response[GetProjectCustomVariablesByProjectIDResponse200 | GetProjectCustomVariablesByProjectIDResponse400 | GetProjectCustomVariablesByProjectIDResponse401 | GetProjectCustomVariablesByProjectIDResponse403 | GetProjectCustomVariablesByProjectIDResponse404 | GetProjectCustomVariablesByProjectIDResponse500]:
    r""" Returns a list of project custom variable overrides.

    Args:
        project_id (int):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        sort_method (str | Unset):  Default: 'alphabetical'.
        sort_order (str | Unset):  Default: 'ASC'.
        keyword (str | Unset):  Default: '\\"\\"'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProjectCustomVariablesByProjectIDResponse200 | GetProjectCustomVariablesByProjectIDResponse400 | GetProjectCustomVariablesByProjectIDResponse401 | GetProjectCustomVariablesByProjectIDResponse403 | GetProjectCustomVariablesByProjectIDResponse404 | GetProjectCustomVariablesByProjectIDResponse500]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
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
    project_id: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    count: int | Unset = 10,
    sort_method: str | Unset = 'alphabetical',
    sort_order: str | Unset = 'ASC',
    keyword: str | Unset = '\\"\\"',

) -> GetProjectCustomVariablesByProjectIDResponse200 | GetProjectCustomVariablesByProjectIDResponse400 | GetProjectCustomVariablesByProjectIDResponse401 | GetProjectCustomVariablesByProjectIDResponse403 | GetProjectCustomVariablesByProjectIDResponse404 | GetProjectCustomVariablesByProjectIDResponse500 | None:
    r""" Returns a list of project custom variable overrides.

    Args:
        project_id (int):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        sort_method (str | Unset):  Default: 'alphabetical'.
        sort_order (str | Unset):  Default: 'ASC'.
        keyword (str | Unset):  Default: '\\"\\"'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProjectCustomVariablesByProjectIDResponse200 | GetProjectCustomVariablesByProjectIDResponse400 | GetProjectCustomVariablesByProjectIDResponse401 | GetProjectCustomVariablesByProjectIDResponse403 | GetProjectCustomVariablesByProjectIDResponse404 | GetProjectCustomVariablesByProjectIDResponse500
     """


    return sync_detailed(
        project_id=project_id,
client=client,
page=page,
count=count,
sort_method=sort_method,
sort_order=sort_order,
keyword=keyword,

    ).parsed

async def asyncio_detailed(
    project_id: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    count: int | Unset = 10,
    sort_method: str | Unset = 'alphabetical',
    sort_order: str | Unset = 'ASC',
    keyword: str | Unset = '\\"\\"',

) -> Response[GetProjectCustomVariablesByProjectIDResponse200 | GetProjectCustomVariablesByProjectIDResponse400 | GetProjectCustomVariablesByProjectIDResponse401 | GetProjectCustomVariablesByProjectIDResponse403 | GetProjectCustomVariablesByProjectIDResponse404 | GetProjectCustomVariablesByProjectIDResponse500]:
    r""" Returns a list of project custom variable overrides.

    Args:
        project_id (int):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        sort_method (str | Unset):  Default: 'alphabetical'.
        sort_order (str | Unset):  Default: 'ASC'.
        keyword (str | Unset):  Default: '\\"\\"'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProjectCustomVariablesByProjectIDResponse200 | GetProjectCustomVariablesByProjectIDResponse400 | GetProjectCustomVariablesByProjectIDResponse401 | GetProjectCustomVariablesByProjectIDResponse403 | GetProjectCustomVariablesByProjectIDResponse404 | GetProjectCustomVariablesByProjectIDResponse500]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
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
    project_id: int,
    *,
    client: AuthenticatedClient,
    page: int | Unset = 1,
    count: int | Unset = 10,
    sort_method: str | Unset = 'alphabetical',
    sort_order: str | Unset = 'ASC',
    keyword: str | Unset = '\\"\\"',

) -> GetProjectCustomVariablesByProjectIDResponse200 | GetProjectCustomVariablesByProjectIDResponse400 | GetProjectCustomVariablesByProjectIDResponse401 | GetProjectCustomVariablesByProjectIDResponse403 | GetProjectCustomVariablesByProjectIDResponse404 | GetProjectCustomVariablesByProjectIDResponse500 | None:
    r""" Returns a list of project custom variable overrides.

    Args:
        project_id (int):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 10.
        sort_method (str | Unset):  Default: 'alphabetical'.
        sort_order (str | Unset):  Default: 'ASC'.
        keyword (str | Unset):  Default: '\\"\\"'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProjectCustomVariablesByProjectIDResponse200 | GetProjectCustomVariablesByProjectIDResponse400 | GetProjectCustomVariablesByProjectIDResponse401 | GetProjectCustomVariablesByProjectIDResponse403 | GetProjectCustomVariablesByProjectIDResponse404 | GetProjectCustomVariablesByProjectIDResponse500
     """


    return (await asyncio_detailed(
        project_id=project_id,
client=client,
page=page,
count=count,
sort_method=sort_method,
sort_order=sort_order,
keyword=keyword,

    )).parsed
