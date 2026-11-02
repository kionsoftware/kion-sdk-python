from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_azure_role_index_2_response_200 import GetAzureRoleIndex2Response200
from ...models.get_azure_role_index_2_response_400 import GetAzureRoleIndex2Response400
from ...models.get_azure_role_index_2_response_401 import GetAzureRoleIndex2Response401
from ...models.get_azure_role_index_2_response_500 import GetAzureRoleIndex2Response500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    managed_by: str | Unset = UNSET,
    status: str | Unset = UNSET,
    q: str | Unset = UNSET,
    p: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["managed_by"] = managed_by

    params["status"] = status

    params["q"] = q

    params["p"] = p


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v4/azure-role",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetAzureRoleIndex2Response200 | GetAzureRoleIndex2Response400 | GetAzureRoleIndex2Response401 | GetAzureRoleIndex2Response500 | None:
    if response.status_code == 200:
        response_200 = GetAzureRoleIndex2Response200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetAzureRoleIndex2Response400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetAzureRoleIndex2Response401.from_dict(response.json())



        return response_401

    if response.status_code == 500:
        response_500 = GetAzureRoleIndex2Response500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetAzureRoleIndex2Response200 | GetAzureRoleIndex2Response400 | GetAzureRoleIndex2Response401 | GetAzureRoleIndex2Response500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    managed_by: str | Unset = UNSET,
    status: str | Unset = UNSET,
    q: str | Unset = UNSET,
    p: str | Unset = UNSET,

) -> Response[GetAzureRoleIndex2Response200 | GetAzureRoleIndex2Response400 | GetAzureRoleIndex2Response401 | GetAzureRoleIndex2Response500]:
    r""" Returns a paginated list of Azure Roles from the application.

     The following query parameters can be provided to further filter the list of Azure Roles:
    1. \"q\" - This defines the keyword to search for within all Azure Roles
    2. \"p\" - This defines the policy creator to filter results by. Options are \"user\", \"system\" or
    Kion, and \"azure\".

    Args:
        managed_by (str | Unset):
        status (str | Unset):
        q (str | Unset):
        p (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAzureRoleIndex2Response200 | GetAzureRoleIndex2Response400 | GetAzureRoleIndex2Response401 | GetAzureRoleIndex2Response500]
     """


    kwargs = _get_kwargs(
        managed_by=managed_by,
status=status,
q=q,
p=p,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    managed_by: str | Unset = UNSET,
    status: str | Unset = UNSET,
    q: str | Unset = UNSET,
    p: str | Unset = UNSET,

) -> GetAzureRoleIndex2Response200 | GetAzureRoleIndex2Response400 | GetAzureRoleIndex2Response401 | GetAzureRoleIndex2Response500 | None:
    r""" Returns a paginated list of Azure Roles from the application.

     The following query parameters can be provided to further filter the list of Azure Roles:
    1. \"q\" - This defines the keyword to search for within all Azure Roles
    2. \"p\" - This defines the policy creator to filter results by. Options are \"user\", \"system\" or
    Kion, and \"azure\".

    Args:
        managed_by (str | Unset):
        status (str | Unset):
        q (str | Unset):
        p (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAzureRoleIndex2Response200 | GetAzureRoleIndex2Response400 | GetAzureRoleIndex2Response401 | GetAzureRoleIndex2Response500
     """


    return sync_detailed(
        client=client,
managed_by=managed_by,
status=status,
q=q,
p=p,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    managed_by: str | Unset = UNSET,
    status: str | Unset = UNSET,
    q: str | Unset = UNSET,
    p: str | Unset = UNSET,

) -> Response[GetAzureRoleIndex2Response200 | GetAzureRoleIndex2Response400 | GetAzureRoleIndex2Response401 | GetAzureRoleIndex2Response500]:
    r""" Returns a paginated list of Azure Roles from the application.

     The following query parameters can be provided to further filter the list of Azure Roles:
    1. \"q\" - This defines the keyword to search for within all Azure Roles
    2. \"p\" - This defines the policy creator to filter results by. Options are \"user\", \"system\" or
    Kion, and \"azure\".

    Args:
        managed_by (str | Unset):
        status (str | Unset):
        q (str | Unset):
        p (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAzureRoleIndex2Response200 | GetAzureRoleIndex2Response400 | GetAzureRoleIndex2Response401 | GetAzureRoleIndex2Response500]
     """


    kwargs = _get_kwargs(
        managed_by=managed_by,
status=status,
q=q,
p=p,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    managed_by: str | Unset = UNSET,
    status: str | Unset = UNSET,
    q: str | Unset = UNSET,
    p: str | Unset = UNSET,

) -> GetAzureRoleIndex2Response200 | GetAzureRoleIndex2Response400 | GetAzureRoleIndex2Response401 | GetAzureRoleIndex2Response500 | None:
    r""" Returns a paginated list of Azure Roles from the application.

     The following query parameters can be provided to further filter the list of Azure Roles:
    1. \"q\" - This defines the keyword to search for within all Azure Roles
    2. \"p\" - This defines the policy creator to filter results by. Options are \"user\", \"system\" or
    Kion, and \"azure\".

    Args:
        managed_by (str | Unset):
        status (str | Unset):
        q (str | Unset):
        p (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAzureRoleIndex2Response200 | GetAzureRoleIndex2Response400 | GetAzureRoleIndex2Response401 | GetAzureRoleIndex2Response500
     """


    return (await asyncio_detailed(
        client=client,
managed_by=managed_by,
status=status,
q=q,
p=p,

    )).parsed
