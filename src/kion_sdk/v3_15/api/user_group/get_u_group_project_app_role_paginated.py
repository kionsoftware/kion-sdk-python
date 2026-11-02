from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_u_group_project_app_role_paginated_response_200 import GetUGroupProjectAppRolePaginatedResponse200
from ...models.get_u_group_project_app_role_paginated_response_400 import GetUGroupProjectAppRolePaginatedResponse400
from ...models.get_u_group_project_app_role_paginated_response_401 import GetUGroupProjectAppRolePaginatedResponse401
from ...models.get_u_group_project_app_role_paginated_response_403 import GetUGroupProjectAppRolePaginatedResponse403
from ...models.get_u_group_project_app_role_paginated_response_500 import GetUGroupProjectAppRolePaginatedResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    page: int | Unset = 1,
    count: int | Unset = 15,
    query: str | Unset = UNSET,
    sort_method: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["count"] = count

    params["query"] = query

    params["sort_method"] = sort_method

    params["sort_order"] = sort_order


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/user-group/{id}/project-app-role".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetUGroupProjectAppRolePaginatedResponse200 | GetUGroupProjectAppRolePaginatedResponse400 | GetUGroupProjectAppRolePaginatedResponse401 | GetUGroupProjectAppRolePaginatedResponse403 | GetUGroupProjectAppRolePaginatedResponse500 | None:
    if response.status_code == 200:
        response_200 = GetUGroupProjectAppRolePaginatedResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetUGroupProjectAppRolePaginatedResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetUGroupProjectAppRolePaginatedResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetUGroupProjectAppRolePaginatedResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetUGroupProjectAppRolePaginatedResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetUGroupProjectAppRolePaginatedResponse200 | GetUGroupProjectAppRolePaginatedResponse400 | GetUGroupProjectAppRolePaginatedResponse401 | GetUGroupProjectAppRolePaginatedResponse403 | GetUGroupProjectAppRolePaginatedResponse500]:
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
    count: int | Unset = 15,
    query: str | Unset = UNSET,
    sort_method: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,

) -> Response[GetUGroupProjectAppRolePaginatedResponse200 | GetUGroupProjectAppRolePaginatedResponse400 | GetUGroupProjectAppRolePaginatedResponse401 | GetUGroupProjectAppRolePaginatedResponse403 | GetUGroupProjectAppRolePaginatedResponse500]:
    """ UGroupOUAppRole will return a list of augmented project app roles for a given a group id.

    Args:
        id (int):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 15.
        query (str | Unset):
        sort_method (str | Unset):
        sort_order (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUGroupProjectAppRolePaginatedResponse200 | GetUGroupProjectAppRolePaginatedResponse400 | GetUGroupProjectAppRolePaginatedResponse401 | GetUGroupProjectAppRolePaginatedResponse403 | GetUGroupProjectAppRolePaginatedResponse500]
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
    count: int | Unset = 15,
    query: str | Unset = UNSET,
    sort_method: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,

) -> GetUGroupProjectAppRolePaginatedResponse200 | GetUGroupProjectAppRolePaginatedResponse400 | GetUGroupProjectAppRolePaginatedResponse401 | GetUGroupProjectAppRolePaginatedResponse403 | GetUGroupProjectAppRolePaginatedResponse500 | None:
    """ UGroupOUAppRole will return a list of augmented project app roles for a given a group id.

    Args:
        id (int):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 15.
        query (str | Unset):
        sort_method (str | Unset):
        sort_order (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUGroupProjectAppRolePaginatedResponse200 | GetUGroupProjectAppRolePaginatedResponse400 | GetUGroupProjectAppRolePaginatedResponse401 | GetUGroupProjectAppRolePaginatedResponse403 | GetUGroupProjectAppRolePaginatedResponse500
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
    count: int | Unset = 15,
    query: str | Unset = UNSET,
    sort_method: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,

) -> Response[GetUGroupProjectAppRolePaginatedResponse200 | GetUGroupProjectAppRolePaginatedResponse400 | GetUGroupProjectAppRolePaginatedResponse401 | GetUGroupProjectAppRolePaginatedResponse403 | GetUGroupProjectAppRolePaginatedResponse500]:
    """ UGroupOUAppRole will return a list of augmented project app roles for a given a group id.

    Args:
        id (int):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 15.
        query (str | Unset):
        sort_method (str | Unset):
        sort_order (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUGroupProjectAppRolePaginatedResponse200 | GetUGroupProjectAppRolePaginatedResponse400 | GetUGroupProjectAppRolePaginatedResponse401 | GetUGroupProjectAppRolePaginatedResponse403 | GetUGroupProjectAppRolePaginatedResponse500]
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
    count: int | Unset = 15,
    query: str | Unset = UNSET,
    sort_method: str | Unset = UNSET,
    sort_order: str | Unset = UNSET,

) -> GetUGroupProjectAppRolePaginatedResponse200 | GetUGroupProjectAppRolePaginatedResponse400 | GetUGroupProjectAppRolePaginatedResponse401 | GetUGroupProjectAppRolePaginatedResponse403 | GetUGroupProjectAppRolePaginatedResponse500 | None:
    """ UGroupOUAppRole will return a list of augmented project app roles for a given a group id.

    Args:
        id (int):
        page (int | Unset):  Default: 1.
        count (int | Unset):  Default: 15.
        query (str | Unset):
        sort_method (str | Unset):
        sort_order (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUGroupProjectAppRolePaginatedResponse200 | GetUGroupProjectAppRolePaginatedResponse400 | GetUGroupProjectAppRolePaginatedResponse401 | GetUGroupProjectAppRolePaginatedResponse403 | GetUGroupProjectAppRolePaginatedResponse500
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
