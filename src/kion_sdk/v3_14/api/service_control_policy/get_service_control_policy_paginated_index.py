from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_service_control_policy_paginated_index_response_200 import GetServiceControlPolicyPaginatedIndexResponse200
from ...models.get_service_control_policy_paginated_index_response_400 import GetServiceControlPolicyPaginatedIndexResponse400
from ...models.get_service_control_policy_paginated_index_response_401 import GetServiceControlPolicyPaginatedIndexResponse401
from ...models.get_service_control_policy_paginated_index_response_500 import GetServiceControlPolicyPaginatedIndexResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    page: int | Unset = UNSET,
    count: int | Unset = UNSET,
    query: str | Unset = UNSET,
    policy_type: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["page"] = page

    params["count"] = count

    params["query"] = query

    params["policy-type"] = policy_type


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v4/service-control-policy",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetServiceControlPolicyPaginatedIndexResponse200 | GetServiceControlPolicyPaginatedIndexResponse400 | GetServiceControlPolicyPaginatedIndexResponse401 | GetServiceControlPolicyPaginatedIndexResponse500 | None:
    if response.status_code == 200:
        response_200 = GetServiceControlPolicyPaginatedIndexResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetServiceControlPolicyPaginatedIndexResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetServiceControlPolicyPaginatedIndexResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 500:
        response_500 = GetServiceControlPolicyPaginatedIndexResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetServiceControlPolicyPaginatedIndexResponse200 | GetServiceControlPolicyPaginatedIndexResponse400 | GetServiceControlPolicyPaginatedIndexResponse401 | GetServiceControlPolicyPaginatedIndexResponse500]:
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
    query: str | Unset = UNSET,
    policy_type: str | Unset = UNSET,

) -> Response[GetServiceControlPolicyPaginatedIndexResponse200 | GetServiceControlPolicyPaginatedIndexResponse400 | GetServiceControlPolicyPaginatedIndexResponse401 | GetServiceControlPolicyPaginatedIndexResponse500]:
    """ Returns a paginated list of Service Control Policies from the application.

    Args:
        page (int | Unset):
        count (int | Unset):
        query (str | Unset):
        policy_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServiceControlPolicyPaginatedIndexResponse200 | GetServiceControlPolicyPaginatedIndexResponse400 | GetServiceControlPolicyPaginatedIndexResponse401 | GetServiceControlPolicyPaginatedIndexResponse500]
     """


    kwargs = _get_kwargs(
        page=page,
count=count,
query=query,
policy_type=policy_type,

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
    query: str | Unset = UNSET,
    policy_type: str | Unset = UNSET,

) -> GetServiceControlPolicyPaginatedIndexResponse200 | GetServiceControlPolicyPaginatedIndexResponse400 | GetServiceControlPolicyPaginatedIndexResponse401 | GetServiceControlPolicyPaginatedIndexResponse500 | None:
    """ Returns a paginated list of Service Control Policies from the application.

    Args:
        page (int | Unset):
        count (int | Unset):
        query (str | Unset):
        policy_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServiceControlPolicyPaginatedIndexResponse200 | GetServiceControlPolicyPaginatedIndexResponse400 | GetServiceControlPolicyPaginatedIndexResponse401 | GetServiceControlPolicyPaginatedIndexResponse500
     """


    return sync_detailed(
        client=client,
page=page,
count=count,
query=query,
policy_type=policy_type,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    count: int | Unset = UNSET,
    query: str | Unset = UNSET,
    policy_type: str | Unset = UNSET,

) -> Response[GetServiceControlPolicyPaginatedIndexResponse200 | GetServiceControlPolicyPaginatedIndexResponse400 | GetServiceControlPolicyPaginatedIndexResponse401 | GetServiceControlPolicyPaginatedIndexResponse500]:
    """ Returns a paginated list of Service Control Policies from the application.

    Args:
        page (int | Unset):
        count (int | Unset):
        query (str | Unset):
        policy_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetServiceControlPolicyPaginatedIndexResponse200 | GetServiceControlPolicyPaginatedIndexResponse400 | GetServiceControlPolicyPaginatedIndexResponse401 | GetServiceControlPolicyPaginatedIndexResponse500]
     """


    kwargs = _get_kwargs(
        page=page,
count=count,
query=query,
policy_type=policy_type,

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
    query: str | Unset = UNSET,
    policy_type: str | Unset = UNSET,

) -> GetServiceControlPolicyPaginatedIndexResponse200 | GetServiceControlPolicyPaginatedIndexResponse400 | GetServiceControlPolicyPaginatedIndexResponse401 | GetServiceControlPolicyPaginatedIndexResponse500 | None:
    """ Returns a paginated list of Service Control Policies from the application.

    Args:
        page (int | Unset):
        count (int | Unset):
        query (str | Unset):
        policy_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetServiceControlPolicyPaginatedIndexResponse200 | GetServiceControlPolicyPaginatedIndexResponse400 | GetServiceControlPolicyPaginatedIndexResponse401 | GetServiceControlPolicyPaginatedIndexResponse500
     """


    return (await asyncio_detailed(
        client=client,
page=page,
count=count,
query=query,
policy_type=policy_type,

    )).parsed
