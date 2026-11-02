from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.cloud_provider_enabled import CloudProviderEnabled
from ...models.patch_set_enabled_cloud_provider_response_200 import PatchSetEnabledCloudProviderResponse200
from ...models.patch_set_enabled_cloud_provider_response_400 import PatchSetEnabledCloudProviderResponse400
from ...models.patch_set_enabled_cloud_provider_response_401 import PatchSetEnabledCloudProviderResponse401
from ...models.patch_set_enabled_cloud_provider_response_403 import PatchSetEnabledCloudProviderResponse403
from ...models.patch_set_enabled_cloud_provider_response_404 import PatchSetEnabledCloudProviderResponse404
from ...models.patch_set_enabled_cloud_provider_response_422 import PatchSetEnabledCloudProviderResponse422
from ...models.patch_set_enabled_cloud_provider_response_500 import PatchSetEnabledCloudProviderResponse500
from typing import cast



def _get_kwargs(
    id: bool,
    *,
    body: CloudProviderEnabled,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/cloud-provider/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchSetEnabledCloudProviderResponse200 | PatchSetEnabledCloudProviderResponse400 | PatchSetEnabledCloudProviderResponse401 | PatchSetEnabledCloudProviderResponse403 | PatchSetEnabledCloudProviderResponse404 | PatchSetEnabledCloudProviderResponse422 | PatchSetEnabledCloudProviderResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchSetEnabledCloudProviderResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchSetEnabledCloudProviderResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchSetEnabledCloudProviderResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchSetEnabledCloudProviderResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PatchSetEnabledCloudProviderResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PatchSetEnabledCloudProviderResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchSetEnabledCloudProviderResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchSetEnabledCloudProviderResponse200 | PatchSetEnabledCloudProviderResponse400 | PatchSetEnabledCloudProviderResponse401 | PatchSetEnabledCloudProviderResponse403 | PatchSetEnabledCloudProviderResponse404 | PatchSetEnabledCloudProviderResponse422 | PatchSetEnabledCloudProviderResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: bool,
    *,
    client: AuthenticatedClient,
    body: CloudProviderEnabled,

) -> Response[PatchSetEnabledCloudProviderResponse200 | PatchSetEnabledCloudProviderResponse400 | PatchSetEnabledCloudProviderResponse401 | PatchSetEnabledCloudProviderResponse403 | PatchSetEnabledCloudProviderResponse404 | PatchSetEnabledCloudProviderResponse422 | PatchSetEnabledCloudProviderResponse500]:
    """ Sets the enabled status of a cloud provider.

     At time of writing CSP IDs are 1 (AWS), 2 (Azure), 3 (Google Cloud), and 4 (OCI).
    You can check the status of the CSPs and get their IDs using GET /v3/cloud-provider

    Args:
        id (bool):
        body (CloudProviderEnabled): CloudProviderEnabled .

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSetEnabledCloudProviderResponse200 | PatchSetEnabledCloudProviderResponse400 | PatchSetEnabledCloudProviderResponse401 | PatchSetEnabledCloudProviderResponse403 | PatchSetEnabledCloudProviderResponse404 | PatchSetEnabledCloudProviderResponse422 | PatchSetEnabledCloudProviderResponse500]
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
    id: bool,
    *,
    client: AuthenticatedClient,
    body: CloudProviderEnabled,

) -> PatchSetEnabledCloudProviderResponse200 | PatchSetEnabledCloudProviderResponse400 | PatchSetEnabledCloudProviderResponse401 | PatchSetEnabledCloudProviderResponse403 | PatchSetEnabledCloudProviderResponse404 | PatchSetEnabledCloudProviderResponse422 | PatchSetEnabledCloudProviderResponse500 | None:
    """ Sets the enabled status of a cloud provider.

     At time of writing CSP IDs are 1 (AWS), 2 (Azure), 3 (Google Cloud), and 4 (OCI).
    You can check the status of the CSPs and get their IDs using GET /v3/cloud-provider

    Args:
        id (bool):
        body (CloudProviderEnabled): CloudProviderEnabled .

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSetEnabledCloudProviderResponse200 | PatchSetEnabledCloudProviderResponse400 | PatchSetEnabledCloudProviderResponse401 | PatchSetEnabledCloudProviderResponse403 | PatchSetEnabledCloudProviderResponse404 | PatchSetEnabledCloudProviderResponse422 | PatchSetEnabledCloudProviderResponse500
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: bool,
    *,
    client: AuthenticatedClient,
    body: CloudProviderEnabled,

) -> Response[PatchSetEnabledCloudProviderResponse200 | PatchSetEnabledCloudProviderResponse400 | PatchSetEnabledCloudProviderResponse401 | PatchSetEnabledCloudProviderResponse403 | PatchSetEnabledCloudProviderResponse404 | PatchSetEnabledCloudProviderResponse422 | PatchSetEnabledCloudProviderResponse500]:
    """ Sets the enabled status of a cloud provider.

     At time of writing CSP IDs are 1 (AWS), 2 (Azure), 3 (Google Cloud), and 4 (OCI).
    You can check the status of the CSPs and get their IDs using GET /v3/cloud-provider

    Args:
        id (bool):
        body (CloudProviderEnabled): CloudProviderEnabled .

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchSetEnabledCloudProviderResponse200 | PatchSetEnabledCloudProviderResponse400 | PatchSetEnabledCloudProviderResponse401 | PatchSetEnabledCloudProviderResponse403 | PatchSetEnabledCloudProviderResponse404 | PatchSetEnabledCloudProviderResponse422 | PatchSetEnabledCloudProviderResponse500]
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
    id: bool,
    *,
    client: AuthenticatedClient,
    body: CloudProviderEnabled,

) -> PatchSetEnabledCloudProviderResponse200 | PatchSetEnabledCloudProviderResponse400 | PatchSetEnabledCloudProviderResponse401 | PatchSetEnabledCloudProviderResponse403 | PatchSetEnabledCloudProviderResponse404 | PatchSetEnabledCloudProviderResponse422 | PatchSetEnabledCloudProviderResponse500 | None:
    """ Sets the enabled status of a cloud provider.

     At time of writing CSP IDs are 1 (AWS), 2 (Azure), 3 (Google Cloud), and 4 (OCI).
    You can check the status of the CSPs and get their IDs using GET /v3/cloud-provider

    Args:
        id (bool):
        body (CloudProviderEnabled): CloudProviderEnabled .

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchSetEnabledCloudProviderResponse200 | PatchSetEnabledCloudProviderResponse400 | PatchSetEnabledCloudProviderResponse401 | PatchSetEnabledCloudProviderResponse403 | PatchSetEnabledCloudProviderResponse404 | PatchSetEnabledCloudProviderResponse422 | PatchSetEnabledCloudProviderResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
