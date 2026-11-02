from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.compliance_check_scan_create_object import ComplianceCheckScanCreateObject
from ...models.post_compliance_check_scan_array_object_response_201 import PostComplianceCheckScanArrayObjectResponse201
from ...models.post_compliance_check_scan_array_object_response_400 import PostComplianceCheckScanArrayObjectResponse400
from ...models.post_compliance_check_scan_array_object_response_401 import PostComplianceCheckScanArrayObjectResponse401
from ...models.post_compliance_check_scan_array_object_response_403 import PostComplianceCheckScanArrayObjectResponse403
from ...models.post_compliance_check_scan_array_object_response_422 import PostComplianceCheckScanArrayObjectResponse422
from ...models.post_compliance_check_scan_array_object_response_500 import PostComplianceCheckScanArrayObjectResponse500
from typing import cast



def _get_kwargs(
    *,
    body: list[ComplianceCheckScanCreateObject],

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/compliance/check/scan/bulk-create",
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)



    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostComplianceCheckScanArrayObjectResponse201 | PostComplianceCheckScanArrayObjectResponse400 | PostComplianceCheckScanArrayObjectResponse401 | PostComplianceCheckScanArrayObjectResponse403 | PostComplianceCheckScanArrayObjectResponse422 | PostComplianceCheckScanArrayObjectResponse500 | None:
    if response.status_code == 201:
        response_201 = PostComplianceCheckScanArrayObjectResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostComplianceCheckScanArrayObjectResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostComplianceCheckScanArrayObjectResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostComplianceCheckScanArrayObjectResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostComplianceCheckScanArrayObjectResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostComplianceCheckScanArrayObjectResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostComplianceCheckScanArrayObjectResponse201 | PostComplianceCheckScanArrayObjectResponse400 | PostComplianceCheckScanArrayObjectResponse401 | PostComplianceCheckScanArrayObjectResponse403 | PostComplianceCheckScanArrayObjectResponse422 | PostComplianceCheckScanArrayObjectResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: list[ComplianceCheckScanCreateObject],

) -> Response[PostComplianceCheckScanArrayObjectResponse201 | PostComplianceCheckScanArrayObjectResponse400 | PostComplianceCheckScanArrayObjectResponse401 | PostComplianceCheckScanArrayObjectResponse403 | PostComplianceCheckScanArrayObjectResponse422 | PostComplianceCheckScanArrayObjectResponse500]:
    """ Creates a List of Object Compliance Check Scan with Findings.

    Args:
        body (list[ComplianceCheckScanCreateObject]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostComplianceCheckScanArrayObjectResponse201 | PostComplianceCheckScanArrayObjectResponse400 | PostComplianceCheckScanArrayObjectResponse401 | PostComplianceCheckScanArrayObjectResponse403 | PostComplianceCheckScanArrayObjectResponse422 | PostComplianceCheckScanArrayObjectResponse500]
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
    body: list[ComplianceCheckScanCreateObject],

) -> PostComplianceCheckScanArrayObjectResponse201 | PostComplianceCheckScanArrayObjectResponse400 | PostComplianceCheckScanArrayObjectResponse401 | PostComplianceCheckScanArrayObjectResponse403 | PostComplianceCheckScanArrayObjectResponse422 | PostComplianceCheckScanArrayObjectResponse500 | None:
    """ Creates a List of Object Compliance Check Scan with Findings.

    Args:
        body (list[ComplianceCheckScanCreateObject]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostComplianceCheckScanArrayObjectResponse201 | PostComplianceCheckScanArrayObjectResponse400 | PostComplianceCheckScanArrayObjectResponse401 | PostComplianceCheckScanArrayObjectResponse403 | PostComplianceCheckScanArrayObjectResponse422 | PostComplianceCheckScanArrayObjectResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: list[ComplianceCheckScanCreateObject],

) -> Response[PostComplianceCheckScanArrayObjectResponse201 | PostComplianceCheckScanArrayObjectResponse400 | PostComplianceCheckScanArrayObjectResponse401 | PostComplianceCheckScanArrayObjectResponse403 | PostComplianceCheckScanArrayObjectResponse422 | PostComplianceCheckScanArrayObjectResponse500]:
    """ Creates a List of Object Compliance Check Scan with Findings.

    Args:
        body (list[ComplianceCheckScanCreateObject]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostComplianceCheckScanArrayObjectResponse201 | PostComplianceCheckScanArrayObjectResponse400 | PostComplianceCheckScanArrayObjectResponse401 | PostComplianceCheckScanArrayObjectResponse403 | PostComplianceCheckScanArrayObjectResponse422 | PostComplianceCheckScanArrayObjectResponse500]
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
    body: list[ComplianceCheckScanCreateObject],

) -> PostComplianceCheckScanArrayObjectResponse201 | PostComplianceCheckScanArrayObjectResponse400 | PostComplianceCheckScanArrayObjectResponse401 | PostComplianceCheckScanArrayObjectResponse403 | PostComplianceCheckScanArrayObjectResponse422 | PostComplianceCheckScanArrayObjectResponse500 | None:
    """ Creates a List of Object Compliance Check Scan with Findings.

    Args:
        body (list[ComplianceCheckScanCreateObject]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostComplianceCheckScanArrayObjectResponse201 | PostComplianceCheckScanArrayObjectResponse400 | PostComplianceCheckScanArrayObjectResponse401 | PostComplianceCheckScanArrayObjectResponse403 | PostComplianceCheckScanArrayObjectResponse422 | PostComplianceCheckScanArrayObjectResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
