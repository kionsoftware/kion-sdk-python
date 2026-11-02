from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_compliance_check_scan_response_200 import GetComplianceCheckScanResponse200
from ...models.get_compliance_check_scan_response_401 import GetComplianceCheckScanResponse401
from ...models.get_compliance_check_scan_response_403 import GetComplianceCheckScanResponse403
from ...models.get_compliance_check_scan_response_404 import GetComplianceCheckScanResponse404
from ...models.get_compliance_check_scan_response_500 import GetComplianceCheckScanResponse500
from typing import cast



def _get_kwargs(
    id: int,
    scan_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/compliance/check/{id}/scan/{scan_id}".format(id=quote(str(id), safe=""),scan_id=quote(str(scan_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetComplianceCheckScanResponse200 | GetComplianceCheckScanResponse401 | GetComplianceCheckScanResponse403 | GetComplianceCheckScanResponse404 | GetComplianceCheckScanResponse500 | None:
    if response.status_code == 200:
        response_200 = GetComplianceCheckScanResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetComplianceCheckScanResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetComplianceCheckScanResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetComplianceCheckScanResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetComplianceCheckScanResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetComplianceCheckScanResponse200 | GetComplianceCheckScanResponse401 | GetComplianceCheckScanResponse403 | GetComplianceCheckScanResponse404 | GetComplianceCheckScanResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    scan_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetComplianceCheckScanResponse200 | GetComplianceCheckScanResponse401 | GetComplianceCheckScanResponse403 | GetComplianceCheckScanResponse404 | GetComplianceCheckScanResponse500]:
    """ Finds an Compliance Check Scan by ID in the application.

    Args:
        id (int):
        scan_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetComplianceCheckScanResponse200 | GetComplianceCheckScanResponse401 | GetComplianceCheckScanResponse403 | GetComplianceCheckScanResponse404 | GetComplianceCheckScanResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
scan_id=scan_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    scan_id: int,
    *,
    client: AuthenticatedClient,

) -> GetComplianceCheckScanResponse200 | GetComplianceCheckScanResponse401 | GetComplianceCheckScanResponse403 | GetComplianceCheckScanResponse404 | GetComplianceCheckScanResponse500 | None:
    """ Finds an Compliance Check Scan by ID in the application.

    Args:
        id (int):
        scan_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetComplianceCheckScanResponse200 | GetComplianceCheckScanResponse401 | GetComplianceCheckScanResponse403 | GetComplianceCheckScanResponse404 | GetComplianceCheckScanResponse500
     """


    return sync_detailed(
        id=id,
scan_id=scan_id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    scan_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetComplianceCheckScanResponse200 | GetComplianceCheckScanResponse401 | GetComplianceCheckScanResponse403 | GetComplianceCheckScanResponse404 | GetComplianceCheckScanResponse500]:
    """ Finds an Compliance Check Scan by ID in the application.

    Args:
        id (int):
        scan_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetComplianceCheckScanResponse200 | GetComplianceCheckScanResponse401 | GetComplianceCheckScanResponse403 | GetComplianceCheckScanResponse404 | GetComplianceCheckScanResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
scan_id=scan_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    scan_id: int,
    *,
    client: AuthenticatedClient,

) -> GetComplianceCheckScanResponse200 | GetComplianceCheckScanResponse401 | GetComplianceCheckScanResponse403 | GetComplianceCheckScanResponse404 | GetComplianceCheckScanResponse500 | None:
    """ Finds an Compliance Check Scan by ID in the application.

    Args:
        id (int):
        scan_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetComplianceCheckScanResponse200 | GetComplianceCheckScanResponse401 | GetComplianceCheckScanResponse403 | GetComplianceCheckScanResponse404 | GetComplianceCheckScanResponse500
     """


    return (await asyncio_detailed(
        id=id,
scan_id=scan_id,
client=client,

    )).parsed
