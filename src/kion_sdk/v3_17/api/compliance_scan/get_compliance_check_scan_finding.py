from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_compliance_check_scan_finding_response_200 import GetComplianceCheckScanFindingResponse200
from ...models.get_compliance_check_scan_finding_response_401 import GetComplianceCheckScanFindingResponse401
from ...models.get_compliance_check_scan_finding_response_403 import GetComplianceCheckScanFindingResponse403
from ...models.get_compliance_check_scan_finding_response_404 import GetComplianceCheckScanFindingResponse404
from ...models.get_compliance_check_scan_finding_response_500 import GetComplianceCheckScanFindingResponse500
from typing import cast



def _get_kwargs(
    id: int,
    finding_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/compliance/check/{id}/finding/{finding_id}".format(id=quote(str(id), safe=""),finding_id=quote(str(finding_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetComplianceCheckScanFindingResponse200 | GetComplianceCheckScanFindingResponse401 | GetComplianceCheckScanFindingResponse403 | GetComplianceCheckScanFindingResponse404 | GetComplianceCheckScanFindingResponse500 | None:
    if response.status_code == 200:
        response_200 = GetComplianceCheckScanFindingResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetComplianceCheckScanFindingResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetComplianceCheckScanFindingResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetComplianceCheckScanFindingResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetComplianceCheckScanFindingResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetComplianceCheckScanFindingResponse200 | GetComplianceCheckScanFindingResponse401 | GetComplianceCheckScanFindingResponse403 | GetComplianceCheckScanFindingResponse404 | GetComplianceCheckScanFindingResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    finding_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetComplianceCheckScanFindingResponse200 | GetComplianceCheckScanFindingResponse401 | GetComplianceCheckScanFindingResponse403 | GetComplianceCheckScanFindingResponse404 | GetComplianceCheckScanFindingResponse500]:
    """ Finds a Compliance Check Scan Finding by ID in the application.

    Args:
        id (int):
        finding_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetComplianceCheckScanFindingResponse200 | GetComplianceCheckScanFindingResponse401 | GetComplianceCheckScanFindingResponse403 | GetComplianceCheckScanFindingResponse404 | GetComplianceCheckScanFindingResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
finding_id=finding_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    finding_id: int,
    *,
    client: AuthenticatedClient,

) -> GetComplianceCheckScanFindingResponse200 | GetComplianceCheckScanFindingResponse401 | GetComplianceCheckScanFindingResponse403 | GetComplianceCheckScanFindingResponse404 | GetComplianceCheckScanFindingResponse500 | None:
    """ Finds a Compliance Check Scan Finding by ID in the application.

    Args:
        id (int):
        finding_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetComplianceCheckScanFindingResponse200 | GetComplianceCheckScanFindingResponse401 | GetComplianceCheckScanFindingResponse403 | GetComplianceCheckScanFindingResponse404 | GetComplianceCheckScanFindingResponse500
     """


    return sync_detailed(
        id=id,
finding_id=finding_id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    finding_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetComplianceCheckScanFindingResponse200 | GetComplianceCheckScanFindingResponse401 | GetComplianceCheckScanFindingResponse403 | GetComplianceCheckScanFindingResponse404 | GetComplianceCheckScanFindingResponse500]:
    """ Finds a Compliance Check Scan Finding by ID in the application.

    Args:
        id (int):
        finding_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetComplianceCheckScanFindingResponse200 | GetComplianceCheckScanFindingResponse401 | GetComplianceCheckScanFindingResponse403 | GetComplianceCheckScanFindingResponse404 | GetComplianceCheckScanFindingResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
finding_id=finding_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    finding_id: int,
    *,
    client: AuthenticatedClient,

) -> GetComplianceCheckScanFindingResponse200 | GetComplianceCheckScanFindingResponse401 | GetComplianceCheckScanFindingResponse403 | GetComplianceCheckScanFindingResponse404 | GetComplianceCheckScanFindingResponse500 | None:
    """ Finds a Compliance Check Scan Finding by ID in the application.

    Args:
        id (int):
        finding_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetComplianceCheckScanFindingResponse200 | GetComplianceCheckScanFindingResponse401 | GetComplianceCheckScanFindingResponse403 | GetComplianceCheckScanFindingResponse404 | GetComplianceCheckScanFindingResponse500
     """


    return (await asyncio_detailed(
        id=id,
finding_id=finding_id,
client=client,

    )).parsed
