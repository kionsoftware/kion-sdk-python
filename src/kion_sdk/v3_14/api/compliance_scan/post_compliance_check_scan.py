from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.compliance_check_scan_create import ComplianceCheckScanCreate
from ...models.post_compliance_check_scan_response_201 import PostComplianceCheckScanResponse201
from ...models.post_compliance_check_scan_response_400 import PostComplianceCheckScanResponse400
from ...models.post_compliance_check_scan_response_401 import PostComplianceCheckScanResponse401
from ...models.post_compliance_check_scan_response_403 import PostComplianceCheckScanResponse403
from ...models.post_compliance_check_scan_response_422 import PostComplianceCheckScanResponse422
from ...models.post_compliance_check_scan_response_500 import PostComplianceCheckScanResponse500
from typing import cast



def _get_kwargs(
    *,
    body: list[ComplianceCheckScanCreate],

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/compliance/check/scan/array",
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)



    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostComplianceCheckScanResponse201 | PostComplianceCheckScanResponse400 | PostComplianceCheckScanResponse401 | PostComplianceCheckScanResponse403 | PostComplianceCheckScanResponse422 | PostComplianceCheckScanResponse500 | None:
    if response.status_code == 201:
        response_201 = PostComplianceCheckScanResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostComplianceCheckScanResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostComplianceCheckScanResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostComplianceCheckScanResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostComplianceCheckScanResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostComplianceCheckScanResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostComplianceCheckScanResponse201 | PostComplianceCheckScanResponse400 | PostComplianceCheckScanResponse401 | PostComplianceCheckScanResponse403 | PostComplianceCheckScanResponse422 | PostComplianceCheckScanResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: list[ComplianceCheckScanCreate],

) -> Response[PostComplianceCheckScanResponse201 | PostComplianceCheckScanResponse400 | PostComplianceCheckScanResponse401 | PostComplianceCheckScanResponse403 | PostComplianceCheckScanResponse422 | PostComplianceCheckScanResponse500]:
    """ Creates an Array of Compliance Check Scan with findings.

    Args:
        body (list[ComplianceCheckScanCreate]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostComplianceCheckScanResponse201 | PostComplianceCheckScanResponse400 | PostComplianceCheckScanResponse401 | PostComplianceCheckScanResponse403 | PostComplianceCheckScanResponse422 | PostComplianceCheckScanResponse500]
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
    body: list[ComplianceCheckScanCreate],

) -> PostComplianceCheckScanResponse201 | PostComplianceCheckScanResponse400 | PostComplianceCheckScanResponse401 | PostComplianceCheckScanResponse403 | PostComplianceCheckScanResponse422 | PostComplianceCheckScanResponse500 | None:
    """ Creates an Array of Compliance Check Scan with findings.

    Args:
        body (list[ComplianceCheckScanCreate]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostComplianceCheckScanResponse201 | PostComplianceCheckScanResponse400 | PostComplianceCheckScanResponse401 | PostComplianceCheckScanResponse403 | PostComplianceCheckScanResponse422 | PostComplianceCheckScanResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: list[ComplianceCheckScanCreate],

) -> Response[PostComplianceCheckScanResponse201 | PostComplianceCheckScanResponse400 | PostComplianceCheckScanResponse401 | PostComplianceCheckScanResponse403 | PostComplianceCheckScanResponse422 | PostComplianceCheckScanResponse500]:
    """ Creates an Array of Compliance Check Scan with findings.

    Args:
        body (list[ComplianceCheckScanCreate]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostComplianceCheckScanResponse201 | PostComplianceCheckScanResponse400 | PostComplianceCheckScanResponse401 | PostComplianceCheckScanResponse403 | PostComplianceCheckScanResponse422 | PostComplianceCheckScanResponse500]
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
    body: list[ComplianceCheckScanCreate],

) -> PostComplianceCheckScanResponse201 | PostComplianceCheckScanResponse400 | PostComplianceCheckScanResponse401 | PostComplianceCheckScanResponse403 | PostComplianceCheckScanResponse422 | PostComplianceCheckScanResponse500 | None:
    """ Creates an Array of Compliance Check Scan with findings.

    Args:
        body (list[ComplianceCheckScanCreate]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostComplianceCheckScanResponse201 | PostComplianceCheckScanResponse400 | PostComplianceCheckScanResponse401 | PostComplianceCheckScanResponse403 | PostComplianceCheckScanResponse422 | PostComplianceCheckScanResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
