from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_compliance_check_scan_group_index_response_200 import GetComplianceCheckScanGroupIndexResponse200
from ...models.get_compliance_check_scan_group_index_response_401 import GetComplianceCheckScanGroupIndexResponse401
from ...models.get_compliance_check_scan_group_index_response_403 import GetComplianceCheckScanGroupIndexResponse403
from ...models.get_compliance_check_scan_group_index_response_404 import GetComplianceCheckScanGroupIndexResponse404
from ...models.get_compliance_check_scan_group_index_response_500 import GetComplianceCheckScanGroupIndexResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/compliance/check/{id}/scan/group".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetComplianceCheckScanGroupIndexResponse200 | GetComplianceCheckScanGroupIndexResponse401 | GetComplianceCheckScanGroupIndexResponse403 | GetComplianceCheckScanGroupIndexResponse404 | GetComplianceCheckScanGroupIndexResponse500 | None:
    if response.status_code == 200:
        response_200 = GetComplianceCheckScanGroupIndexResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetComplianceCheckScanGroupIndexResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetComplianceCheckScanGroupIndexResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetComplianceCheckScanGroupIndexResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetComplianceCheckScanGroupIndexResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetComplianceCheckScanGroupIndexResponse200 | GetComplianceCheckScanGroupIndexResponse401 | GetComplianceCheckScanGroupIndexResponse403 | GetComplianceCheckScanGroupIndexResponse404 | GetComplianceCheckScanGroupIndexResponse500]:
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

) -> Response[GetComplianceCheckScanGroupIndexResponse200 | GetComplianceCheckScanGroupIndexResponse401 | GetComplianceCheckScanGroupIndexResponse403 | GetComplianceCheckScanGroupIndexResponse404 | GetComplianceCheckScanGroupIndexResponse500]:
    """ Finds all Compliance Check Scan Groups in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetComplianceCheckScanGroupIndexResponse200 | GetComplianceCheckScanGroupIndexResponse401 | GetComplianceCheckScanGroupIndexResponse403 | GetComplianceCheckScanGroupIndexResponse404 | GetComplianceCheckScanGroupIndexResponse500]
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

) -> GetComplianceCheckScanGroupIndexResponse200 | GetComplianceCheckScanGroupIndexResponse401 | GetComplianceCheckScanGroupIndexResponse403 | GetComplianceCheckScanGroupIndexResponse404 | GetComplianceCheckScanGroupIndexResponse500 | None:
    """ Finds all Compliance Check Scan Groups in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetComplianceCheckScanGroupIndexResponse200 | GetComplianceCheckScanGroupIndexResponse401 | GetComplianceCheckScanGroupIndexResponse403 | GetComplianceCheckScanGroupIndexResponse404 | GetComplianceCheckScanGroupIndexResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetComplianceCheckScanGroupIndexResponse200 | GetComplianceCheckScanGroupIndexResponse401 | GetComplianceCheckScanGroupIndexResponse403 | GetComplianceCheckScanGroupIndexResponse404 | GetComplianceCheckScanGroupIndexResponse500]:
    """ Finds all Compliance Check Scan Groups in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetComplianceCheckScanGroupIndexResponse200 | GetComplianceCheckScanGroupIndexResponse401 | GetComplianceCheckScanGroupIndexResponse403 | GetComplianceCheckScanGroupIndexResponse404 | GetComplianceCheckScanGroupIndexResponse500]
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

) -> GetComplianceCheckScanGroupIndexResponse200 | GetComplianceCheckScanGroupIndexResponse401 | GetComplianceCheckScanGroupIndexResponse403 | GetComplianceCheckScanGroupIndexResponse404 | GetComplianceCheckScanGroupIndexResponse500 | None:
    """ Finds all Compliance Check Scan Groups in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetComplianceCheckScanGroupIndexResponse200 | GetComplianceCheckScanGroupIndexResponse401 | GetComplianceCheckScanGroupIndexResponse403 | GetComplianceCheckScanGroupIndexResponse404 | GetComplianceCheckScanGroupIndexResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
