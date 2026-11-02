from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_compliance_cloud_rule_standard_schedule_scan_response_200 import PostComplianceCloudRuleStandardScheduleScanResponse200
from ...models.post_compliance_cloud_rule_standard_schedule_scan_response_401 import PostComplianceCloudRuleStandardScheduleScanResponse401
from ...models.post_compliance_cloud_rule_standard_schedule_scan_response_403 import PostComplianceCloudRuleStandardScheduleScanResponse403
from ...models.post_compliance_cloud_rule_standard_schedule_scan_response_404 import PostComplianceCloudRuleStandardScheduleScanResponse404
from ...models.post_compliance_cloud_rule_standard_schedule_scan_response_500 import PostComplianceCloudRuleStandardScheduleScanResponse500
from typing import cast



def _get_kwargs(
    id: int,
    standard_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/cloud-rule/{id}/compliance/standard/{standard_id}/schedule-scan".format(id=quote(str(id), safe=""),standard_id=quote(str(standard_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostComplianceCloudRuleStandardScheduleScanResponse200 | PostComplianceCloudRuleStandardScheduleScanResponse401 | PostComplianceCloudRuleStandardScheduleScanResponse403 | PostComplianceCloudRuleStandardScheduleScanResponse404 | PostComplianceCloudRuleStandardScheduleScanResponse500 | None:
    if response.status_code == 200:
        response_200 = PostComplianceCloudRuleStandardScheduleScanResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = PostComplianceCloudRuleStandardScheduleScanResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostComplianceCloudRuleStandardScheduleScanResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PostComplianceCloudRuleStandardScheduleScanResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = PostComplianceCloudRuleStandardScheduleScanResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostComplianceCloudRuleStandardScheduleScanResponse200 | PostComplianceCloudRuleStandardScheduleScanResponse401 | PostComplianceCloudRuleStandardScheduleScanResponse403 | PostComplianceCloudRuleStandardScheduleScanResponse404 | PostComplianceCloudRuleStandardScheduleScanResponse500]:
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

) -> Response[PostComplianceCloudRuleStandardScheduleScanResponse200 | PostComplianceCloudRuleStandardScheduleScanResponse401 | PostComplianceCloudRuleStandardScheduleScanResponse403 | PostComplianceCloudRuleStandardScheduleScanResponse404 | PostComplianceCloudRuleStandardScheduleScanResponse500]:
    """ Schedules a scan on the standard that is applied to a project on a cloud rule level.

    Args:
        id (int):
        standard_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostComplianceCloudRuleStandardScheduleScanResponse200 | PostComplianceCloudRuleStandardScheduleScanResponse401 | PostComplianceCloudRuleStandardScheduleScanResponse403 | PostComplianceCloudRuleStandardScheduleScanResponse404 | PostComplianceCloudRuleStandardScheduleScanResponse500]
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

) -> PostComplianceCloudRuleStandardScheduleScanResponse200 | PostComplianceCloudRuleStandardScheduleScanResponse401 | PostComplianceCloudRuleStandardScheduleScanResponse403 | PostComplianceCloudRuleStandardScheduleScanResponse404 | PostComplianceCloudRuleStandardScheduleScanResponse500 | None:
    """ Schedules a scan on the standard that is applied to a project on a cloud rule level.

    Args:
        id (int):
        standard_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostComplianceCloudRuleStandardScheduleScanResponse200 | PostComplianceCloudRuleStandardScheduleScanResponse401 | PostComplianceCloudRuleStandardScheduleScanResponse403 | PostComplianceCloudRuleStandardScheduleScanResponse404 | PostComplianceCloudRuleStandardScheduleScanResponse500
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

) -> Response[PostComplianceCloudRuleStandardScheduleScanResponse200 | PostComplianceCloudRuleStandardScheduleScanResponse401 | PostComplianceCloudRuleStandardScheduleScanResponse403 | PostComplianceCloudRuleStandardScheduleScanResponse404 | PostComplianceCloudRuleStandardScheduleScanResponse500]:
    """ Schedules a scan on the standard that is applied to a project on a cloud rule level.

    Args:
        id (int):
        standard_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostComplianceCloudRuleStandardScheduleScanResponse200 | PostComplianceCloudRuleStandardScheduleScanResponse401 | PostComplianceCloudRuleStandardScheduleScanResponse403 | PostComplianceCloudRuleStandardScheduleScanResponse404 | PostComplianceCloudRuleStandardScheduleScanResponse500]
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

) -> PostComplianceCloudRuleStandardScheduleScanResponse200 | PostComplianceCloudRuleStandardScheduleScanResponse401 | PostComplianceCloudRuleStandardScheduleScanResponse403 | PostComplianceCloudRuleStandardScheduleScanResponse404 | PostComplianceCloudRuleStandardScheduleScanResponse500 | None:
    """ Schedules a scan on the standard that is applied to a project on a cloud rule level.

    Args:
        id (int):
        standard_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostComplianceCloudRuleStandardScheduleScanResponse200 | PostComplianceCloudRuleStandardScheduleScanResponse401 | PostComplianceCloudRuleStandardScheduleScanResponse403 | PostComplianceCloudRuleStandardScheduleScanResponse404 | PostComplianceCloudRuleStandardScheduleScanResponse500
     """


    return (await asyncio_detailed(
        id=id,
standard_id=standard_id,
client=client,

    )).parsed
