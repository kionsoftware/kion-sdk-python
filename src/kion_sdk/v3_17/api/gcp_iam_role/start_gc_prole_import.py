from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.gcp_trigger_role_import import GCPTriggerRoleImport
from ...models.start_gc_prole_import_response_202 import StartGCProleImportResponse202
from ...models.start_gc_prole_import_response_401 import StartGCProleImportResponse401
from ...models.start_gc_prole_import_response_500 import StartGCProleImportResponse500
from typing import cast



def _get_kwargs(
    *,
    body: GCPTriggerRoleImport,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/gcp-iam-role/trigger-import",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> StartGCProleImportResponse202 | StartGCProleImportResponse401 | StartGCProleImportResponse500 | None:
    if response.status_code == 202:
        response_202 = StartGCProleImportResponse202.from_dict(response.json())



        return response_202

    if response.status_code == 401:
        response_401 = StartGCProleImportResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 500:
        response_500 = StartGCProleImportResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[StartGCProleImportResponse202 | StartGCProleImportResponse401 | StartGCProleImportResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: GCPTriggerRoleImport,

) -> Response[StartGCProleImportResponse202 | StartGCProleImportResponse401 | StartGCProleImportResponse500]:
    """ Triggers an import of provider-defined or custom roles from Google Cloud.

    Args:
        body (GCPTriggerRoleImport): GCPTriggerRoleImport is the request body for triggering gcp
            roles imports

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StartGCProleImportResponse202 | StartGCProleImportResponse401 | StartGCProleImportResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: GCPTriggerRoleImport,

) -> StartGCProleImportResponse202 | StartGCProleImportResponse401 | StartGCProleImportResponse500 | None:
    """ Triggers an import of provider-defined or custom roles from Google Cloud.

    Args:
        body (GCPTriggerRoleImport): GCPTriggerRoleImport is the request body for triggering gcp
            roles imports

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StartGCProleImportResponse202 | StartGCProleImportResponse401 | StartGCProleImportResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: GCPTriggerRoleImport,

) -> Response[StartGCProleImportResponse202 | StartGCProleImportResponse401 | StartGCProleImportResponse500]:
    """ Triggers an import of provider-defined or custom roles from Google Cloud.

    Args:
        body (GCPTriggerRoleImport): GCPTriggerRoleImport is the request body for triggering gcp
            roles imports

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StartGCProleImportResponse202 | StartGCProleImportResponse401 | StartGCProleImportResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: GCPTriggerRoleImport,

) -> StartGCProleImportResponse202 | StartGCProleImportResponse401 | StartGCProleImportResponse500 | None:
    """ Triggers an import of provider-defined or custom roles from Google Cloud.

    Args:
        body (GCPTriggerRoleImport): GCPTriggerRoleImport is the request body for triggering gcp
            roles imports

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StartGCProleImportResponse202 | StartGCProleImportResponse401 | StartGCProleImportResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
