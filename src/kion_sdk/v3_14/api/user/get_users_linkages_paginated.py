from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_users_linkages_paginated_response_200 import GetUsersLinkagesPaginatedResponse200
from ...models.get_users_linkages_paginated_response_400 import GetUsersLinkagesPaginatedResponse400
from ...models.get_users_linkages_paginated_response_401 import GetUsersLinkagesPaginatedResponse401
from ...models.get_users_linkages_paginated_response_403 import GetUsersLinkagesPaginatedResponse403
from ...models.get_users_linkages_paginated_response_422 import GetUsersLinkagesPaginatedResponse422
from ...models.get_users_linkages_paginated_response_500 import GetUsersLinkagesPaginatedResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: list[int],
    include_deleted: bool | Unset = False,
    exclude_finalized: bool | Unset = False,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["include-deleted"] = include_deleted

    params["exclude-finalized"] = exclude_finalized


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v4/user/azure-account-linkages",
        "params": params,
    }

    _kwargs["json"] = body



    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetUsersLinkagesPaginatedResponse200 | GetUsersLinkagesPaginatedResponse400 | GetUsersLinkagesPaginatedResponse401 | GetUsersLinkagesPaginatedResponse403 | GetUsersLinkagesPaginatedResponse422 | GetUsersLinkagesPaginatedResponse500 | None:
    if response.status_code == 200:
        response_200 = GetUsersLinkagesPaginatedResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetUsersLinkagesPaginatedResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetUsersLinkagesPaginatedResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetUsersLinkagesPaginatedResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = GetUsersLinkagesPaginatedResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = GetUsersLinkagesPaginatedResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetUsersLinkagesPaginatedResponse200 | GetUsersLinkagesPaginatedResponse400 | GetUsersLinkagesPaginatedResponse401 | GetUsersLinkagesPaginatedResponse403 | GetUsersLinkagesPaginatedResponse422 | GetUsersLinkagesPaginatedResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: list[int],
    include_deleted: bool | Unset = False,
    exclude_finalized: bool | Unset = False,

) -> Response[GetUsersLinkagesPaginatedResponse200 | GetUsersLinkagesPaginatedResponse400 | GetUsersLinkagesPaginatedResponse401 | GetUsersLinkagesPaginatedResponse403 | GetUsersLinkagesPaginatedResponse422 | GetUsersLinkagesPaginatedResponse500]:
    """ Fetch a paginated set of azure account links for a set of Kion users.

    Args:
        include_deleted (bool | Unset):  Default: False.
        exclude_finalized (bool | Unset):  Default: False.
        body (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsersLinkagesPaginatedResponse200 | GetUsersLinkagesPaginatedResponse400 | GetUsersLinkagesPaginatedResponse401 | GetUsersLinkagesPaginatedResponse403 | GetUsersLinkagesPaginatedResponse422 | GetUsersLinkagesPaginatedResponse500]
     """


    kwargs = _get_kwargs(
        body=body,
include_deleted=include_deleted,
exclude_finalized=exclude_finalized,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: list[int],
    include_deleted: bool | Unset = False,
    exclude_finalized: bool | Unset = False,

) -> GetUsersLinkagesPaginatedResponse200 | GetUsersLinkagesPaginatedResponse400 | GetUsersLinkagesPaginatedResponse401 | GetUsersLinkagesPaginatedResponse403 | GetUsersLinkagesPaginatedResponse422 | GetUsersLinkagesPaginatedResponse500 | None:
    """ Fetch a paginated set of azure account links for a set of Kion users.

    Args:
        include_deleted (bool | Unset):  Default: False.
        exclude_finalized (bool | Unset):  Default: False.
        body (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsersLinkagesPaginatedResponse200 | GetUsersLinkagesPaginatedResponse400 | GetUsersLinkagesPaginatedResponse401 | GetUsersLinkagesPaginatedResponse403 | GetUsersLinkagesPaginatedResponse422 | GetUsersLinkagesPaginatedResponse500
     """


    return sync_detailed(
        client=client,
body=body,
include_deleted=include_deleted,
exclude_finalized=exclude_finalized,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: list[int],
    include_deleted: bool | Unset = False,
    exclude_finalized: bool | Unset = False,

) -> Response[GetUsersLinkagesPaginatedResponse200 | GetUsersLinkagesPaginatedResponse400 | GetUsersLinkagesPaginatedResponse401 | GetUsersLinkagesPaginatedResponse403 | GetUsersLinkagesPaginatedResponse422 | GetUsersLinkagesPaginatedResponse500]:
    """ Fetch a paginated set of azure account links for a set of Kion users.

    Args:
        include_deleted (bool | Unset):  Default: False.
        exclude_finalized (bool | Unset):  Default: False.
        body (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetUsersLinkagesPaginatedResponse200 | GetUsersLinkagesPaginatedResponse400 | GetUsersLinkagesPaginatedResponse401 | GetUsersLinkagesPaginatedResponse403 | GetUsersLinkagesPaginatedResponse422 | GetUsersLinkagesPaginatedResponse500]
     """


    kwargs = _get_kwargs(
        body=body,
include_deleted=include_deleted,
exclude_finalized=exclude_finalized,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: list[int],
    include_deleted: bool | Unset = False,
    exclude_finalized: bool | Unset = False,

) -> GetUsersLinkagesPaginatedResponse200 | GetUsersLinkagesPaginatedResponse400 | GetUsersLinkagesPaginatedResponse401 | GetUsersLinkagesPaginatedResponse403 | GetUsersLinkagesPaginatedResponse422 | GetUsersLinkagesPaginatedResponse500 | None:
    """ Fetch a paginated set of azure account links for a set of Kion users.

    Args:
        include_deleted (bool | Unset):  Default: False.
        exclude_finalized (bool | Unset):  Default: False.
        body (list[int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetUsersLinkagesPaginatedResponse200 | GetUsersLinkagesPaginatedResponse400 | GetUsersLinkagesPaginatedResponse401 | GetUsersLinkagesPaginatedResponse403 | GetUsersLinkagesPaginatedResponse422 | GetUsersLinkagesPaginatedResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,
include_deleted=include_deleted,
exclude_finalized=exclude_finalized,

    )).parsed
