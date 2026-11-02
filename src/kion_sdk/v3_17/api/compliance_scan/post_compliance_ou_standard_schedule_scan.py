from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_compliance_ou_standard_schedule_scan_response_200 import PostComplianceOUStandardScheduleScanResponse200
from ...models.post_compliance_ou_standard_schedule_scan_response_401 import PostComplianceOUStandardScheduleScanResponse401
from ...models.post_compliance_ou_standard_schedule_scan_response_403 import PostComplianceOUStandardScheduleScanResponse403
from ...models.post_compliance_ou_standard_schedule_scan_response_404 import PostComplianceOUStandardScheduleScanResponse404
from ...models.post_compliance_ou_standard_schedule_scan_response_500 import PostComplianceOUStandardScheduleScanResponse500
from typing import cast



def _get_kwargs(
    id: int,
    standard_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/ou/{id}/compliance/standard/{standard_id}/schedule-scan".format(id=quote(str(id), safe=""),standard_id=quote(str(standard_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostComplianceOUStandardScheduleScanResponse200 | PostComplianceOUStandardScheduleScanResponse401 | PostComplianceOUStandardScheduleScanResponse403 | PostComplianceOUStandardScheduleScanResponse404 | PostComplianceOUStandardScheduleScanResponse500 | None:
    if response.status_code == 200:
        response_200 = PostComplianceOUStandardScheduleScanResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = PostComplianceOUStandardScheduleScanResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostComplianceOUStandardScheduleScanResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PostComplianceOUStandardScheduleScanResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = PostComplianceOUStandardScheduleScanResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostComplianceOUStandardScheduleScanResponse200 | PostComplianceOUStandardScheduleScanResponse401 | PostComplianceOUStandardScheduleScanResponse403 | PostComplianceOUStandardScheduleScanResponse404 | PostComplianceOUStandardScheduleScanResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    standard_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[PostComplianceOUStandardScheduleScanResponse200 | PostComplianceOUStandardScheduleScanResponse401 | PostComplianceOUStandardScheduleScanResponse403 | PostComplianceOUStandardScheduleScanResponse404 | PostComplianceOUStandardScheduleScanResponse500]:
    """ Schedules a scan on the standard that is applied to a OU.

    Args:
        id (int):
        standard_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostComplianceOUStandardScheduleScanResponse200 | PostComplianceOUStandardScheduleScanResponse401 | PostComplianceOUStandardScheduleScanResponse403 | PostComplianceOUStandardScheduleScanResponse404 | PostComplianceOUStandardScheduleScanResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
standard_id=standard_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    standard_id: int,
    *,
    client: AuthenticatedClient,

) -> PostComplianceOUStandardScheduleScanResponse200 | PostComplianceOUStandardScheduleScanResponse401 | PostComplianceOUStandardScheduleScanResponse403 | PostComplianceOUStandardScheduleScanResponse404 | PostComplianceOUStandardScheduleScanResponse500 | None:
    """ Schedules a scan on the standard that is applied to a OU.

    Args:
        id (int):
        standard_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostComplianceOUStandardScheduleScanResponse200 | PostComplianceOUStandardScheduleScanResponse401 | PostComplianceOUStandardScheduleScanResponse403 | PostComplianceOUStandardScheduleScanResponse404 | PostComplianceOUStandardScheduleScanResponse500
     """


    return sync_detailed(
        id=id,
standard_id=standard_id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    standard_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[PostComplianceOUStandardScheduleScanResponse200 | PostComplianceOUStandardScheduleScanResponse401 | PostComplianceOUStandardScheduleScanResponse403 | PostComplianceOUStandardScheduleScanResponse404 | PostComplianceOUStandardScheduleScanResponse500]:
    """ Schedules a scan on the standard that is applied to a OU.

    Args:
        id (int):
        standard_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostComplianceOUStandardScheduleScanResponse200 | PostComplianceOUStandardScheduleScanResponse401 | PostComplianceOUStandardScheduleScanResponse403 | PostComplianceOUStandardScheduleScanResponse404 | PostComplianceOUStandardScheduleScanResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
standard_id=standard_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    standard_id: int,
    *,
    client: AuthenticatedClient,

) -> PostComplianceOUStandardScheduleScanResponse200 | PostComplianceOUStandardScheduleScanResponse401 | PostComplianceOUStandardScheduleScanResponse403 | PostComplianceOUStandardScheduleScanResponse404 | PostComplianceOUStandardScheduleScanResponse500 | None:
    """ Schedules a scan on the standard that is applied to a OU.

    Args:
        id (int):
        standard_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostComplianceOUStandardScheduleScanResponse200 | PostComplianceOUStandardScheduleScanResponse401 | PostComplianceOUStandardScheduleScanResponse403 | PostComplianceOUStandardScheduleScanResponse404 | PostComplianceOUStandardScheduleScanResponse500
     """


    return (await asyncio_detailed(
        id=id,
standard_id=standard_id,
client=client,

    )).parsed
