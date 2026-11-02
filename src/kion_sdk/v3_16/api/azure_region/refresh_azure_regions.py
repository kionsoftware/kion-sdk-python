from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.refresh_azure_regions_response_200 import RefreshAzureRegionsResponse200
from ...models.refresh_azure_regions_response_400 import RefreshAzureRegionsResponse400
from ...models.refresh_azure_regions_response_401 import RefreshAzureRegionsResponse401
from ...models.refresh_azure_regions_response_403 import RefreshAzureRegionsResponse403
from ...models.refresh_azure_regions_response_500 import RefreshAzureRegionsResponse500
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/azure-region/refresh",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RefreshAzureRegionsResponse200 | RefreshAzureRegionsResponse400 | RefreshAzureRegionsResponse401 | RefreshAzureRegionsResponse403 | RefreshAzureRegionsResponse500 | None:
    if response.status_code == 200:
        response_200 = RefreshAzureRegionsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = RefreshAzureRegionsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = RefreshAzureRegionsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = RefreshAzureRegionsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = RefreshAzureRegionsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RefreshAzureRegionsResponse200 | RefreshAzureRegionsResponse400 | RefreshAzureRegionsResponse401 | RefreshAzureRegionsResponse403 | RefreshAzureRegionsResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[RefreshAzureRegionsResponse200 | RefreshAzureRegionsResponse400 | RefreshAzureRegionsResponse401 | RefreshAzureRegionsResponse403 | RefreshAzureRegionsResponse500]:
    """ Triggers a refresh of the available Azure Regions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RefreshAzureRegionsResponse200 | RefreshAzureRegionsResponse400 | RefreshAzureRegionsResponse401 | RefreshAzureRegionsResponse403 | RefreshAzureRegionsResponse500]
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

) -> RefreshAzureRegionsResponse200 | RefreshAzureRegionsResponse400 | RefreshAzureRegionsResponse401 | RefreshAzureRegionsResponse403 | RefreshAzureRegionsResponse500 | None:
    """ Triggers a refresh of the available Azure Regions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RefreshAzureRegionsResponse200 | RefreshAzureRegionsResponse400 | RefreshAzureRegionsResponse401 | RefreshAzureRegionsResponse403 | RefreshAzureRegionsResponse500
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[RefreshAzureRegionsResponse200 | RefreshAzureRegionsResponse400 | RefreshAzureRegionsResponse401 | RefreshAzureRegionsResponse403 | RefreshAzureRegionsResponse500]:
    """ Triggers a refresh of the available Azure Regions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RefreshAzureRegionsResponse200 | RefreshAzureRegionsResponse400 | RefreshAzureRegionsResponse401 | RefreshAzureRegionsResponse403 | RefreshAzureRegionsResponse500]
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

) -> RefreshAzureRegionsResponse200 | RefreshAzureRegionsResponse400 | RefreshAzureRegionsResponse401 | RefreshAzureRegionsResponse403 | RefreshAzureRegionsResponse500 | None:
    """ Triggers a refresh of the available Azure Regions.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RefreshAzureRegionsResponse200 | RefreshAzureRegionsResponse400 | RefreshAzureRegionsResponse401 | RefreshAzureRegionsResponse403 | RefreshAzureRegionsResponse500
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
