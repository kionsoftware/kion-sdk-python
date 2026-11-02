from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_azure_arm_template_all_paginated_response_200 import GetAzureARMTemplateAllPaginatedResponse200
from ...models.get_azure_arm_template_all_paginated_response_400 import GetAzureARMTemplateAllPaginatedResponse400
from ...models.get_azure_arm_template_all_paginated_response_401 import GetAzureARMTemplateAllPaginatedResponse401
from ...models.get_azure_arm_template_all_paginated_response_500 import GetAzureARMTemplateAllPaginatedResponse500
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v4/azure-arm-template",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetAzureARMTemplateAllPaginatedResponse200 | GetAzureARMTemplateAllPaginatedResponse400 | GetAzureARMTemplateAllPaginatedResponse401 | GetAzureARMTemplateAllPaginatedResponse500 | None:
    if response.status_code == 200:
        response_200 = GetAzureARMTemplateAllPaginatedResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetAzureARMTemplateAllPaginatedResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetAzureARMTemplateAllPaginatedResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 500:
        response_500 = GetAzureARMTemplateAllPaginatedResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetAzureARMTemplateAllPaginatedResponse200 | GetAzureARMTemplateAllPaginatedResponse400 | GetAzureARMTemplateAllPaginatedResponse401 | GetAzureARMTemplateAllPaginatedResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetAzureARMTemplateAllPaginatedResponse200 | GetAzureARMTemplateAllPaginatedResponse400 | GetAzureARMTemplateAllPaginatedResponse401 | GetAzureARMTemplateAllPaginatedResponse500]:
    """ Returns a paginated list of Azure ARM Templates with their respective owners.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAzureARMTemplateAllPaginatedResponse200 | GetAzureARMTemplateAllPaginatedResponse400 | GetAzureARMTemplateAllPaginatedResponse401 | GetAzureARMTemplateAllPaginatedResponse500]
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

) -> GetAzureARMTemplateAllPaginatedResponse200 | GetAzureARMTemplateAllPaginatedResponse400 | GetAzureARMTemplateAllPaginatedResponse401 | GetAzureARMTemplateAllPaginatedResponse500 | None:
    """ Returns a paginated list of Azure ARM Templates with their respective owners.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAzureARMTemplateAllPaginatedResponse200 | GetAzureARMTemplateAllPaginatedResponse400 | GetAzureARMTemplateAllPaginatedResponse401 | GetAzureARMTemplateAllPaginatedResponse500
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetAzureARMTemplateAllPaginatedResponse200 | GetAzureARMTemplateAllPaginatedResponse400 | GetAzureARMTemplateAllPaginatedResponse401 | GetAzureARMTemplateAllPaginatedResponse500]:
    """ Returns a paginated list of Azure ARM Templates with their respective owners.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAzureARMTemplateAllPaginatedResponse200 | GetAzureARMTemplateAllPaginatedResponse400 | GetAzureARMTemplateAllPaginatedResponse401 | GetAzureARMTemplateAllPaginatedResponse500]
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

) -> GetAzureARMTemplateAllPaginatedResponse200 | GetAzureARMTemplateAllPaginatedResponse400 | GetAzureARMTemplateAllPaginatedResponse401 | GetAzureARMTemplateAllPaginatedResponse500 | None:
    """ Returns a paginated list of Azure ARM Templates with their respective owners.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAzureARMTemplateAllPaginatedResponse200 | GetAzureARMTemplateAllPaginatedResponse400 | GetAzureARMTemplateAllPaginatedResponse401 | GetAzureARMTemplateAllPaginatedResponse500
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
