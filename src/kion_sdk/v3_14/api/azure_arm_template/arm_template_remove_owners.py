from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.arm_template_remove_owners_response_200 import ARMTemplateRemoveOwnersResponse200
from ...models.arm_template_remove_owners_response_400 import ARMTemplateRemoveOwnersResponse400
from ...models.arm_template_remove_owners_response_401 import ARMTemplateRemoveOwnersResponse401
from ...models.arm_template_remove_owners_response_403 import ARMTemplateRemoveOwnersResponse403
from ...models.arm_template_remove_owners_response_404 import ARMTemplateRemoveOwnersResponse404
from ...models.arm_template_remove_owners_response_422 import ARMTemplateRemoveOwnersResponse422
from ...models.arm_template_remove_owners_response_500 import ARMTemplateRemoveOwnersResponse500
from ...models.azure_arm_template_definition_owners import AzureARMTemplateDefinitionOwners
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: AzureARMTemplateDefinitionOwners,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/azure-arm-template/{id}/owner".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ARMTemplateRemoveOwnersResponse200 | ARMTemplateRemoveOwnersResponse400 | ARMTemplateRemoveOwnersResponse401 | ARMTemplateRemoveOwnersResponse403 | ARMTemplateRemoveOwnersResponse404 | ARMTemplateRemoveOwnersResponse422 | ARMTemplateRemoveOwnersResponse500 | None:
    if response.status_code == 200:
        response_200 = ARMTemplateRemoveOwnersResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ARMTemplateRemoveOwnersResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ARMTemplateRemoveOwnersResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ARMTemplateRemoveOwnersResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = ARMTemplateRemoveOwnersResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = ARMTemplateRemoveOwnersResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = ARMTemplateRemoveOwnersResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ARMTemplateRemoveOwnersResponse200 | ARMTemplateRemoveOwnersResponse400 | ARMTemplateRemoveOwnersResponse401 | ARMTemplateRemoveOwnersResponse403 | ARMTemplateRemoveOwnersResponse404 | ARMTemplateRemoveOwnersResponse422 | ARMTemplateRemoveOwnersResponse500]:
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
    body: AzureARMTemplateDefinitionOwners,

) -> Response[ARMTemplateRemoveOwnersResponse200 | ARMTemplateRemoveOwnersResponse400 | ARMTemplateRemoveOwnersResponse401 | ARMTemplateRemoveOwnersResponse403 | ARMTemplateRemoveOwnersResponse404 | ARMTemplateRemoveOwnersResponse422 | ARMTemplateRemoveOwnersResponse500]:
    """ Removes users and groups as owners of the Azure ARM template in the application.

    Args:
        id (int):
        body (AzureARMTemplateDefinitionOwners): AzureARMTemplateDefinitionOwners defines the
            owners of an ARM template.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ARMTemplateRemoveOwnersResponse200 | ARMTemplateRemoveOwnersResponse400 | ARMTemplateRemoveOwnersResponse401 | ARMTemplateRemoveOwnersResponse403 | ARMTemplateRemoveOwnersResponse404 | ARMTemplateRemoveOwnersResponse422 | ARMTemplateRemoveOwnersResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: AzureARMTemplateDefinitionOwners,

) -> ARMTemplateRemoveOwnersResponse200 | ARMTemplateRemoveOwnersResponse400 | ARMTemplateRemoveOwnersResponse401 | ARMTemplateRemoveOwnersResponse403 | ARMTemplateRemoveOwnersResponse404 | ARMTemplateRemoveOwnersResponse422 | ARMTemplateRemoveOwnersResponse500 | None:
    """ Removes users and groups as owners of the Azure ARM template in the application.

    Args:
        id (int):
        body (AzureARMTemplateDefinitionOwners): AzureARMTemplateDefinitionOwners defines the
            owners of an ARM template.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ARMTemplateRemoveOwnersResponse200 | ARMTemplateRemoveOwnersResponse400 | ARMTemplateRemoveOwnersResponse401 | ARMTemplateRemoveOwnersResponse403 | ARMTemplateRemoveOwnersResponse404 | ARMTemplateRemoveOwnersResponse422 | ARMTemplateRemoveOwnersResponse500
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: AzureARMTemplateDefinitionOwners,

) -> Response[ARMTemplateRemoveOwnersResponse200 | ARMTemplateRemoveOwnersResponse400 | ARMTemplateRemoveOwnersResponse401 | ARMTemplateRemoveOwnersResponse403 | ARMTemplateRemoveOwnersResponse404 | ARMTemplateRemoveOwnersResponse422 | ARMTemplateRemoveOwnersResponse500]:
    """ Removes users and groups as owners of the Azure ARM template in the application.

    Args:
        id (int):
        body (AzureARMTemplateDefinitionOwners): AzureARMTemplateDefinitionOwners defines the
            owners of an ARM template.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ARMTemplateRemoveOwnersResponse200 | ARMTemplateRemoveOwnersResponse400 | ARMTemplateRemoveOwnersResponse401 | ARMTemplateRemoveOwnersResponse403 | ARMTemplateRemoveOwnersResponse404 | ARMTemplateRemoveOwnersResponse422 | ARMTemplateRemoveOwnersResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: AzureARMTemplateDefinitionOwners,

) -> ARMTemplateRemoveOwnersResponse200 | ARMTemplateRemoveOwnersResponse400 | ARMTemplateRemoveOwnersResponse401 | ARMTemplateRemoveOwnersResponse403 | ARMTemplateRemoveOwnersResponse404 | ARMTemplateRemoveOwnersResponse422 | ARMTemplateRemoveOwnersResponse500 | None:
    """ Removes users and groups as owners of the Azure ARM template in the application.

    Args:
        id (int):
        body (AzureARMTemplateDefinitionOwners): AzureARMTemplateDefinitionOwners defines the
            owners of an ARM template.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ARMTemplateRemoveOwnersResponse200 | ARMTemplateRemoveOwnersResponse400 | ARMTemplateRemoveOwnersResponse401 | ARMTemplateRemoveOwnersResponse403 | ARMTemplateRemoveOwnersResponse404 | ARMTemplateRemoveOwnersResponse422 | ARMTemplateRemoveOwnersResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
