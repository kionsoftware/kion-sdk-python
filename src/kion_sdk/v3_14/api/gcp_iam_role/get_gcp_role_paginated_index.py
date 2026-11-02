from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_gcp_role_paginated_index_response_200 import GetGCPRolePaginatedIndexResponse200
from ...models.get_gcp_role_paginated_index_response_400 import GetGCPRolePaginatedIndexResponse400
from ...models.get_gcp_role_paginated_index_response_401 import GetGCPRolePaginatedIndexResponse401
from ...models.get_gcp_role_paginated_index_response_403 import GetGCPRolePaginatedIndexResponse403
from ...models.get_gcp_role_paginated_index_response_500 import GetGCPRolePaginatedIndexResponse500
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v4/gcp-iam-role",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetGCPRolePaginatedIndexResponse200 | GetGCPRolePaginatedIndexResponse400 | GetGCPRolePaginatedIndexResponse401 | GetGCPRolePaginatedIndexResponse403 | GetGCPRolePaginatedIndexResponse500 | None:
    if response.status_code == 200:
        response_200 = GetGCPRolePaginatedIndexResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetGCPRolePaginatedIndexResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetGCPRolePaginatedIndexResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetGCPRolePaginatedIndexResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetGCPRolePaginatedIndexResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetGCPRolePaginatedIndexResponse200 | GetGCPRolePaginatedIndexResponse400 | GetGCPRolePaginatedIndexResponse401 | GetGCPRolePaginatedIndexResponse403 | GetGCPRolePaginatedIndexResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetGCPRolePaginatedIndexResponse200 | GetGCPRolePaginatedIndexResponse400 | GetGCPRolePaginatedIndexResponse401 | GetGCPRolePaginatedIndexResponse403 | GetGCPRolePaginatedIndexResponse500]:
    r""" Gets all gcp iam roles in cloudtamer.io and returns them paginated.

     The following query parameters can be provided to further filter the list of GCP IAM Roles:
    1. \"q\" - This defines the keyword to search for within all GCP Roles
    2. \"p\" - This defines the role definition creator to further filter results by. Options are
    \"user\", \"system\" or Kion, and \"gcp\".

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGCPRolePaginatedIndexResponse200 | GetGCPRolePaginatedIndexResponse400 | GetGCPRolePaginatedIndexResponse401 | GetGCPRolePaginatedIndexResponse403 | GetGCPRolePaginatedIndexResponse500]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,

) -> GetGCPRolePaginatedIndexResponse200 | GetGCPRolePaginatedIndexResponse400 | GetGCPRolePaginatedIndexResponse401 | GetGCPRolePaginatedIndexResponse403 | GetGCPRolePaginatedIndexResponse500 | None:
    r""" Gets all gcp iam roles in cloudtamer.io and returns them paginated.

     The following query parameters can be provided to further filter the list of GCP IAM Roles:
    1. \"q\" - This defines the keyword to search for within all GCP Roles
    2. \"p\" - This defines the role definition creator to further filter results by. Options are
    \"user\", \"system\" or Kion, and \"gcp\".

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGCPRolePaginatedIndexResponse200 | GetGCPRolePaginatedIndexResponse400 | GetGCPRolePaginatedIndexResponse401 | GetGCPRolePaginatedIndexResponse403 | GetGCPRolePaginatedIndexResponse500
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetGCPRolePaginatedIndexResponse200 | GetGCPRolePaginatedIndexResponse400 | GetGCPRolePaginatedIndexResponse401 | GetGCPRolePaginatedIndexResponse403 | GetGCPRolePaginatedIndexResponse500]:
    r""" Gets all gcp iam roles in cloudtamer.io and returns them paginated.

     The following query parameters can be provided to further filter the list of GCP IAM Roles:
    1. \"q\" - This defines the keyword to search for within all GCP Roles
    2. \"p\" - This defines the role definition creator to further filter results by. Options are
    \"user\", \"system\" or Kion, and \"gcp\".

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGCPRolePaginatedIndexResponse200 | GetGCPRolePaginatedIndexResponse400 | GetGCPRolePaginatedIndexResponse401 | GetGCPRolePaginatedIndexResponse403 | GetGCPRolePaginatedIndexResponse500]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,

) -> GetGCPRolePaginatedIndexResponse200 | GetGCPRolePaginatedIndexResponse400 | GetGCPRolePaginatedIndexResponse401 | GetGCPRolePaginatedIndexResponse403 | GetGCPRolePaginatedIndexResponse500 | None:
    r""" Gets all gcp iam roles in cloudtamer.io and returns them paginated.

     The following query parameters can be provided to further filter the list of GCP IAM Roles:
    1. \"q\" - This defines the keyword to search for within all GCP Roles
    2. \"p\" - This defines the role definition creator to further filter results by. Options are
    \"user\", \"system\" or Kion, and \"gcp\".

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGCPRolePaginatedIndexResponse200 | GetGCPRolePaginatedIndexResponse400 | GetGCPRolePaginatedIndexResponse401 | GetGCPRolePaginatedIndexResponse403 | GetGCPRolePaginatedIndexResponse500
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
