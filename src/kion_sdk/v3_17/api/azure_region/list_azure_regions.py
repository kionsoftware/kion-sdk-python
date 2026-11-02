from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.list_azure_regions_response_200 import ListAzureRegionsResponse200
from ...models.list_azure_regions_response_401 import ListAzureRegionsResponse401
from ...models.list_azure_regions_response_500 import ListAzureRegionsResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    include_deleted: bool | Unset = False,
    supported_only: bool | Unset = False,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["include-deleted"] = include_deleted

    params["supported-only"] = supported_only


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/azure-region",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ListAzureRegionsResponse200 | ListAzureRegionsResponse401 | ListAzureRegionsResponse500 | None:
    if response.status_code == 200:
        response_200 = ListAzureRegionsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = ListAzureRegionsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 500:
        response_500 = ListAzureRegionsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ListAzureRegionsResponse200 | ListAzureRegionsResponse401 | ListAzureRegionsResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    include_deleted: bool | Unset = False,
    supported_only: bool | Unset = False,

) -> Response[ListAzureRegionsResponse200 | ListAzureRegionsResponse401 | ListAzureRegionsResponse500]:
    """ Retrieves the list of all cached Azure Regions.

    Args:
        include_deleted (bool | Unset):  Default: False.
        supported_only (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAzureRegionsResponse200 | ListAzureRegionsResponse401 | ListAzureRegionsResponse500]
     """


    kwargs = _get_kwargs(
        include_deleted=include_deleted,
supported_only=supported_only,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    include_deleted: bool | Unset = False,
    supported_only: bool | Unset = False,

) -> ListAzureRegionsResponse200 | ListAzureRegionsResponse401 | ListAzureRegionsResponse500 | None:
    """ Retrieves the list of all cached Azure Regions.

    Args:
        include_deleted (bool | Unset):  Default: False.
        supported_only (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAzureRegionsResponse200 | ListAzureRegionsResponse401 | ListAzureRegionsResponse500
     """


    return sync_detailed(
        client=client,
include_deleted=include_deleted,
supported_only=supported_only,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include_deleted: bool | Unset = False,
    supported_only: bool | Unset = False,

) -> Response[ListAzureRegionsResponse200 | ListAzureRegionsResponse401 | ListAzureRegionsResponse500]:
    """ Retrieves the list of all cached Azure Regions.

    Args:
        include_deleted (bool | Unset):  Default: False.
        supported_only (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListAzureRegionsResponse200 | ListAzureRegionsResponse401 | ListAzureRegionsResponse500]
     """


    kwargs = _get_kwargs(
        include_deleted=include_deleted,
supported_only=supported_only,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    include_deleted: bool | Unset = False,
    supported_only: bool | Unset = False,

) -> ListAzureRegionsResponse200 | ListAzureRegionsResponse401 | ListAzureRegionsResponse500 | None:
    """ Retrieves the list of all cached Azure Regions.

    Args:
        include_deleted (bool | Unset):  Default: False.
        supported_only (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListAzureRegionsResponse200 | ListAzureRegionsResponse401 | ListAzureRegionsResponse500
     """


    return (await asyncio_detailed(
        client=client,
include_deleted=include_deleted,
supported_only=supported_only,

    )).parsed
