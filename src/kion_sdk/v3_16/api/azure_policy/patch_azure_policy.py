from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.azure_policy_definition_update import AzurePolicyDefinitionUpdate
from ...models.patch_azure_policy_response_200 import PatchAzurePolicyResponse200
from ...models.patch_azure_policy_response_400 import PatchAzurePolicyResponse400
from ...models.patch_azure_policy_response_401 import PatchAzurePolicyResponse401
from ...models.patch_azure_policy_response_403 import PatchAzurePolicyResponse403
from ...models.patch_azure_policy_response_404 import PatchAzurePolicyResponse404
from ...models.patch_azure_policy_response_422 import PatchAzurePolicyResponse422
from ...models.patch_azure_policy_response_500 import PatchAzurePolicyResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: AzurePolicyDefinitionUpdate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/azure-policy/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchAzurePolicyResponse200 | PatchAzurePolicyResponse400 | PatchAzurePolicyResponse401 | PatchAzurePolicyResponse403 | PatchAzurePolicyResponse404 | PatchAzurePolicyResponse422 | PatchAzurePolicyResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchAzurePolicyResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchAzurePolicyResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchAzurePolicyResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchAzurePolicyResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PatchAzurePolicyResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PatchAzurePolicyResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchAzurePolicyResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchAzurePolicyResponse200 | PatchAzurePolicyResponse400 | PatchAzurePolicyResponse401 | PatchAzurePolicyResponse403 | PatchAzurePolicyResponse404 | PatchAzurePolicyResponse422 | PatchAzurePolicyResponse500]:
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
    body: AzurePolicyDefinitionUpdate,

) -> Response[PatchAzurePolicyResponse200 | PatchAzurePolicyResponse400 | PatchAzurePolicyResponse401 | PatchAzurePolicyResponse403 | PatchAzurePolicyResponse404 | PatchAzurePolicyResponse422 | PatchAzurePolicyResponse500]:
    """ Updates an azure policy by ID in the application.

    Args:
        id (int):
        body (AzurePolicyDefinitionUpdate): AzurePolicyDefinitionUpdate represents an update Azure
            Policy Definition, complete with the policy itself and its parameters.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchAzurePolicyResponse200 | PatchAzurePolicyResponse400 | PatchAzurePolicyResponse401 | PatchAzurePolicyResponse403 | PatchAzurePolicyResponse404 | PatchAzurePolicyResponse422 | PatchAzurePolicyResponse500]
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
    body: AzurePolicyDefinitionUpdate,

) -> PatchAzurePolicyResponse200 | PatchAzurePolicyResponse400 | PatchAzurePolicyResponse401 | PatchAzurePolicyResponse403 | PatchAzurePolicyResponse404 | PatchAzurePolicyResponse422 | PatchAzurePolicyResponse500 | None:
    """ Updates an azure policy by ID in the application.

    Args:
        id (int):
        body (AzurePolicyDefinitionUpdate): AzurePolicyDefinitionUpdate represents an update Azure
            Policy Definition, complete with the policy itself and its parameters.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchAzurePolicyResponse200 | PatchAzurePolicyResponse400 | PatchAzurePolicyResponse401 | PatchAzurePolicyResponse403 | PatchAzurePolicyResponse404 | PatchAzurePolicyResponse422 | PatchAzurePolicyResponse500
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
    body: AzurePolicyDefinitionUpdate,

) -> Response[PatchAzurePolicyResponse200 | PatchAzurePolicyResponse400 | PatchAzurePolicyResponse401 | PatchAzurePolicyResponse403 | PatchAzurePolicyResponse404 | PatchAzurePolicyResponse422 | PatchAzurePolicyResponse500]:
    """ Updates an azure policy by ID in the application.

    Args:
        id (int):
        body (AzurePolicyDefinitionUpdate): AzurePolicyDefinitionUpdate represents an update Azure
            Policy Definition, complete with the policy itself and its parameters.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchAzurePolicyResponse200 | PatchAzurePolicyResponse400 | PatchAzurePolicyResponse401 | PatchAzurePolicyResponse403 | PatchAzurePolicyResponse404 | PatchAzurePolicyResponse422 | PatchAzurePolicyResponse500]
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
    body: AzurePolicyDefinitionUpdate,

) -> PatchAzurePolicyResponse200 | PatchAzurePolicyResponse400 | PatchAzurePolicyResponse401 | PatchAzurePolicyResponse403 | PatchAzurePolicyResponse404 | PatchAzurePolicyResponse422 | PatchAzurePolicyResponse500 | None:
    """ Updates an azure policy by ID in the application.

    Args:
        id (int):
        body (AzurePolicyDefinitionUpdate): AzurePolicyDefinitionUpdate represents an update Azure
            Policy Definition, complete with the policy itself and its parameters.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchAzurePolicyResponse200 | PatchAzurePolicyResponse400 | PatchAzurePolicyResponse401 | PatchAzurePolicyResponse403 | PatchAzurePolicyResponse404 | PatchAzurePolicyResponse422 | PatchAzurePolicyResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
