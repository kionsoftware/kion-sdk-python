from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_azure_role_index_response_200 import GetAzureRoleIndexResponse200
from ...models.get_azure_role_index_response_400 import GetAzureRoleIndexResponse400
from ...models.get_azure_role_index_response_401 import GetAzureRoleIndexResponse401
from ...models.get_azure_role_index_response_500 import GetAzureRoleIndexResponse500
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/azure-role",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetAzureRoleIndexResponse200 | GetAzureRoleIndexResponse400 | GetAzureRoleIndexResponse401 | GetAzureRoleIndexResponse500 | None:
    if response.status_code == 200:
        response_200 = GetAzureRoleIndexResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetAzureRoleIndexResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetAzureRoleIndexResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 500:
        response_500 = GetAzureRoleIndexResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetAzureRoleIndexResponse200 | GetAzureRoleIndexResponse400 | GetAzureRoleIndexResponse401 | GetAzureRoleIndexResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetAzureRoleIndexResponse200 | GetAzureRoleIndexResponse400 | GetAzureRoleIndexResponse401 | GetAzureRoleIndexResponse500]:
    """ Returns a list of Azure Roles from the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAzureRoleIndexResponse200 | GetAzureRoleIndexResponse400 | GetAzureRoleIndexResponse401 | GetAzureRoleIndexResponse500]
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

) -> GetAzureRoleIndexResponse200 | GetAzureRoleIndexResponse400 | GetAzureRoleIndexResponse401 | GetAzureRoleIndexResponse500 | None:
    """ Returns a list of Azure Roles from the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAzureRoleIndexResponse200 | GetAzureRoleIndexResponse400 | GetAzureRoleIndexResponse401 | GetAzureRoleIndexResponse500
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetAzureRoleIndexResponse200 | GetAzureRoleIndexResponse400 | GetAzureRoleIndexResponse401 | GetAzureRoleIndexResponse500]:
    """ Returns a list of Azure Roles from the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAzureRoleIndexResponse200 | GetAzureRoleIndexResponse400 | GetAzureRoleIndexResponse401 | GetAzureRoleIndexResponse500]
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

) -> GetAzureRoleIndexResponse200 | GetAzureRoleIndexResponse400 | GetAzureRoleIndexResponse401 | GetAzureRoleIndexResponse500 | None:
    """ Returns a list of Azure Roles from the application.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAzureRoleIndexResponse200 | GetAzureRoleIndexResponse400 | GetAzureRoleIndexResponse401 | GetAzureRoleIndexResponse500
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
