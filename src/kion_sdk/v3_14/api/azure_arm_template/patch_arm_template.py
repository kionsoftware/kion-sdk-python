from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.azure_arm_template_definition_update import AzureARMTemplateDefinitionUpdate
from ...models.patch_arm_template_response_200 import PatchARMTemplateResponse200
from ...models.patch_arm_template_response_400 import PatchARMTemplateResponse400
from ...models.patch_arm_template_response_401 import PatchARMTemplateResponse401
from ...models.patch_arm_template_response_403 import PatchARMTemplateResponse403
from ...models.patch_arm_template_response_404 import PatchARMTemplateResponse404
from ...models.patch_arm_template_response_422 import PatchARMTemplateResponse422
from ...models.patch_arm_template_response_500 import PatchARMTemplateResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: AzureARMTemplateDefinitionUpdate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/azure-arm-template/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchARMTemplateResponse200 | PatchARMTemplateResponse400 | PatchARMTemplateResponse401 | PatchARMTemplateResponse403 | PatchARMTemplateResponse404 | PatchARMTemplateResponse422 | PatchARMTemplateResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchARMTemplateResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchARMTemplateResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchARMTemplateResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchARMTemplateResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PatchARMTemplateResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PatchARMTemplateResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchARMTemplateResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchARMTemplateResponse200 | PatchARMTemplateResponse400 | PatchARMTemplateResponse401 | PatchARMTemplateResponse403 | PatchARMTemplateResponse404 | PatchARMTemplateResponse422 | PatchARMTemplateResponse500]:
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
    body: AzureARMTemplateDefinitionUpdate,

) -> Response[PatchARMTemplateResponse200 | PatchARMTemplateResponse400 | PatchARMTemplateResponse401 | PatchARMTemplateResponse403 | PatchARMTemplateResponse404 | PatchARMTemplateResponse422 | PatchARMTemplateResponse500]:
    """ Updates an Azure ARM template in the application.

    Args:
        id (int):
        body (AzureARMTemplateDefinitionUpdate): AzureARMTemplateDefinitionUpdate defines an Azure
            ARM template definition update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchARMTemplateResponse200 | PatchARMTemplateResponse400 | PatchARMTemplateResponse401 | PatchARMTemplateResponse403 | PatchARMTemplateResponse404 | PatchARMTemplateResponse422 | PatchARMTemplateResponse500]
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
    body: AzureARMTemplateDefinitionUpdate,

) -> PatchARMTemplateResponse200 | PatchARMTemplateResponse400 | PatchARMTemplateResponse401 | PatchARMTemplateResponse403 | PatchARMTemplateResponse404 | PatchARMTemplateResponse422 | PatchARMTemplateResponse500 | None:
    """ Updates an Azure ARM template in the application.

    Args:
        id (int):
        body (AzureARMTemplateDefinitionUpdate): AzureARMTemplateDefinitionUpdate defines an Azure
            ARM template definition update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchARMTemplateResponse200 | PatchARMTemplateResponse400 | PatchARMTemplateResponse401 | PatchARMTemplateResponse403 | PatchARMTemplateResponse404 | PatchARMTemplateResponse422 | PatchARMTemplateResponse500
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
    body: AzureARMTemplateDefinitionUpdate,

) -> Response[PatchARMTemplateResponse200 | PatchARMTemplateResponse400 | PatchARMTemplateResponse401 | PatchARMTemplateResponse403 | PatchARMTemplateResponse404 | PatchARMTemplateResponse422 | PatchARMTemplateResponse500]:
    """ Updates an Azure ARM template in the application.

    Args:
        id (int):
        body (AzureARMTemplateDefinitionUpdate): AzureARMTemplateDefinitionUpdate defines an Azure
            ARM template definition update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchARMTemplateResponse200 | PatchARMTemplateResponse400 | PatchARMTemplateResponse401 | PatchARMTemplateResponse403 | PatchARMTemplateResponse404 | PatchARMTemplateResponse422 | PatchARMTemplateResponse500]
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
    body: AzureARMTemplateDefinitionUpdate,

) -> PatchARMTemplateResponse200 | PatchARMTemplateResponse400 | PatchARMTemplateResponse401 | PatchARMTemplateResponse403 | PatchARMTemplateResponse404 | PatchARMTemplateResponse422 | PatchARMTemplateResponse500 | None:
    """ Updates an Azure ARM template in the application.

    Args:
        id (int):
        body (AzureARMTemplateDefinitionUpdate): AzureARMTemplateDefinitionUpdate defines an Azure
            ARM template definition update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchARMTemplateResponse200 | PatchARMTemplateResponse400 | PatchARMTemplateResponse401 | PatchARMTemplateResponse403 | PatchARMTemplateResponse404 | PatchARMTemplateResponse422 | PatchARMTemplateResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
