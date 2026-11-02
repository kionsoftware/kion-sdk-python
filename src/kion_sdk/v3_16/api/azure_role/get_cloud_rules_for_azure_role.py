from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_cloud_rules_for_azure_role_response_200 import GetCloudRulesForAzureRoleResponse200
from ...models.get_cloud_rules_for_azure_role_response_401 import GetCloudRulesForAzureRoleResponse401
from ...models.get_cloud_rules_for_azure_role_response_403 import GetCloudRulesForAzureRoleResponse403
from ...models.get_cloud_rules_for_azure_role_response_404 import GetCloudRulesForAzureRoleResponse404
from ...models.get_cloud_rules_for_azure_role_response_500 import GetCloudRulesForAzureRoleResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/azure-role/{id}/cloud-rule".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetCloudRulesForAzureRoleResponse200 | GetCloudRulesForAzureRoleResponse401 | GetCloudRulesForAzureRoleResponse403 | GetCloudRulesForAzureRoleResponse404 | GetCloudRulesForAzureRoleResponse500 | None:
    if response.status_code == 200:
        response_200 = GetCloudRulesForAzureRoleResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetCloudRulesForAzureRoleResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetCloudRulesForAzureRoleResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetCloudRulesForAzureRoleResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetCloudRulesForAzureRoleResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetCloudRulesForAzureRoleResponse200 | GetCloudRulesForAzureRoleResponse401 | GetCloudRulesForAzureRoleResponse403 | GetCloudRulesForAzureRoleResponse404 | GetCloudRulesForAzureRoleResponse500]:
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

) -> Response[GetCloudRulesForAzureRoleResponse200 | GetCloudRulesForAzureRoleResponse401 | GetCloudRulesForAzureRoleResponse403 | GetCloudRulesForAzureRoleResponse404 | GetCloudRulesForAzureRoleResponse500]:
    """ Returns a list of Cloud Rules that are attached to an Azure Role.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCloudRulesForAzureRoleResponse200 | GetCloudRulesForAzureRoleResponse401 | GetCloudRulesForAzureRoleResponse403 | GetCloudRulesForAzureRoleResponse404 | GetCloudRulesForAzureRoleResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,

) -> GetCloudRulesForAzureRoleResponse200 | GetCloudRulesForAzureRoleResponse401 | GetCloudRulesForAzureRoleResponse403 | GetCloudRulesForAzureRoleResponse404 | GetCloudRulesForAzureRoleResponse500 | None:
    """ Returns a list of Cloud Rules that are attached to an Azure Role.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCloudRulesForAzureRoleResponse200 | GetCloudRulesForAzureRoleResponse401 | GetCloudRulesForAzureRoleResponse403 | GetCloudRulesForAzureRoleResponse404 | GetCloudRulesForAzureRoleResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetCloudRulesForAzureRoleResponse200 | GetCloudRulesForAzureRoleResponse401 | GetCloudRulesForAzureRoleResponse403 | GetCloudRulesForAzureRoleResponse404 | GetCloudRulesForAzureRoleResponse500]:
    """ Returns a list of Cloud Rules that are attached to an Azure Role.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCloudRulesForAzureRoleResponse200 | GetCloudRulesForAzureRoleResponse401 | GetCloudRulesForAzureRoleResponse403 | GetCloudRulesForAzureRoleResponse404 | GetCloudRulesForAzureRoleResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,

) -> GetCloudRulesForAzureRoleResponse200 | GetCloudRulesForAzureRoleResponse401 | GetCloudRulesForAzureRoleResponse403 | GetCloudRulesForAzureRoleResponse404 | GetCloudRulesForAzureRoleResponse500 | None:
    """ Returns a list of Cloud Rules that are attached to an Azure Role.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCloudRulesForAzureRoleResponse200 | GetCloudRulesForAzureRoleResponse401 | GetCloudRulesForAzureRoleResponse403 | GetCloudRulesForAzureRoleResponse404 | GetCloudRulesForAzureRoleResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
