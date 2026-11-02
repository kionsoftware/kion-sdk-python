from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_compliance_standard_check_schedule_scan_response_200 import PostComplianceStandardCheckScheduleScanResponse200
from ...models.post_compliance_standard_check_schedule_scan_response_401 import PostComplianceStandardCheckScheduleScanResponse401
from ...models.post_compliance_standard_check_schedule_scan_response_403 import PostComplianceStandardCheckScheduleScanResponse403
from ...models.post_compliance_standard_check_schedule_scan_response_404 import PostComplianceStandardCheckScheduleScanResponse404
from ...models.post_compliance_standard_check_schedule_scan_response_500 import PostComplianceStandardCheckScheduleScanResponse500
from typing import cast



def _get_kwargs(
    id: int,
    check_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/compliance/standard/{id}/check/{check_id}/schedule-scan".format(id=quote(str(id), safe=""),check_id=quote(str(check_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostComplianceStandardCheckScheduleScanResponse200 | PostComplianceStandardCheckScheduleScanResponse401 | PostComplianceStandardCheckScheduleScanResponse403 | PostComplianceStandardCheckScheduleScanResponse404 | PostComplianceStandardCheckScheduleScanResponse500 | None:
    if response.status_code == 200:
        response_200 = PostComplianceStandardCheckScheduleScanResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = PostComplianceStandardCheckScheduleScanResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostComplianceStandardCheckScheduleScanResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PostComplianceStandardCheckScheduleScanResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = PostComplianceStandardCheckScheduleScanResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostComplianceStandardCheckScheduleScanResponse200 | PostComplianceStandardCheckScheduleScanResponse401 | PostComplianceStandardCheckScheduleScanResponse403 | PostComplianceStandardCheckScheduleScanResponse404 | PostComplianceStandardCheckScheduleScanResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    check_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[PostComplianceStandardCheckScheduleScanResponse200 | PostComplianceStandardCheckScheduleScanResponse401 | PostComplianceStandardCheckScheduleScanResponse403 | PostComplianceStandardCheckScheduleScanResponse404 | PostComplianceStandardCheckScheduleScanResponse500]:
    """ Schedules a scan on the check for a given standard.

    Args:
        id (int):
        check_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostComplianceStandardCheckScheduleScanResponse200 | PostComplianceStandardCheckScheduleScanResponse401 | PostComplianceStandardCheckScheduleScanResponse403 | PostComplianceStandardCheckScheduleScanResponse404 | PostComplianceStandardCheckScheduleScanResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
check_id=check_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    check_id: int,
    *,
    client: AuthenticatedClient,

) -> PostComplianceStandardCheckScheduleScanResponse200 | PostComplianceStandardCheckScheduleScanResponse401 | PostComplianceStandardCheckScheduleScanResponse403 | PostComplianceStandardCheckScheduleScanResponse404 | PostComplianceStandardCheckScheduleScanResponse500 | None:
    """ Schedules a scan on the check for a given standard.

    Args:
        id (int):
        check_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostComplianceStandardCheckScheduleScanResponse200 | PostComplianceStandardCheckScheduleScanResponse401 | PostComplianceStandardCheckScheduleScanResponse403 | PostComplianceStandardCheckScheduleScanResponse404 | PostComplianceStandardCheckScheduleScanResponse500
     """


    return sync_detailed(
        id=id,
check_id=check_id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    check_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[PostComplianceStandardCheckScheduleScanResponse200 | PostComplianceStandardCheckScheduleScanResponse401 | PostComplianceStandardCheckScheduleScanResponse403 | PostComplianceStandardCheckScheduleScanResponse404 | PostComplianceStandardCheckScheduleScanResponse500]:
    """ Schedules a scan on the check for a given standard.

    Args:
        id (int):
        check_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostComplianceStandardCheckScheduleScanResponse200 | PostComplianceStandardCheckScheduleScanResponse401 | PostComplianceStandardCheckScheduleScanResponse403 | PostComplianceStandardCheckScheduleScanResponse404 | PostComplianceStandardCheckScheduleScanResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
check_id=check_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    check_id: int,
    *,
    client: AuthenticatedClient,

) -> PostComplianceStandardCheckScheduleScanResponse200 | PostComplianceStandardCheckScheduleScanResponse401 | PostComplianceStandardCheckScheduleScanResponse403 | PostComplianceStandardCheckScheduleScanResponse404 | PostComplianceStandardCheckScheduleScanResponse500 | None:
    """ Schedules a scan on the check for a given standard.

    Args:
        id (int):
        check_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostComplianceStandardCheckScheduleScanResponse200 | PostComplianceStandardCheckScheduleScanResponse401 | PostComplianceStandardCheckScheduleScanResponse403 | PostComplianceStandardCheckScheduleScanResponse404 | PostComplianceStandardCheckScheduleScanResponse500
     """


    return (await asyncio_detailed(
        id=id,
check_id=check_id,
client=client,

    )).parsed
