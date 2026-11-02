from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.compliance_check_suppressed_finding_create import ComplianceCheckSuppressedFindingCreate
from ...models.post_compliance_check_suppress_all_standards_finding_response_200 import PostComplianceCheckSuppressAllStandardsFindingResponse200
from ...models.post_compliance_check_suppress_all_standards_finding_response_400 import PostComplianceCheckSuppressAllStandardsFindingResponse400
from ...models.post_compliance_check_suppress_all_standards_finding_response_401 import PostComplianceCheckSuppressAllStandardsFindingResponse401
from ...models.post_compliance_check_suppress_all_standards_finding_response_403 import PostComplianceCheckSuppressAllStandardsFindingResponse403
from ...models.post_compliance_check_suppress_all_standards_finding_response_404 import PostComplianceCheckSuppressAllStandardsFindingResponse404
from ...models.post_compliance_check_suppress_all_standards_finding_response_422 import PostComplianceCheckSuppressAllStandardsFindingResponse422
from ...models.post_compliance_check_suppress_all_standards_finding_response_500 import PostComplianceCheckSuppressAllStandardsFindingResponse500
from typing import cast



def _get_kwargs(
    id: int,
    check_id: int,
    finding_id: int,
    *,
    body: ComplianceCheckSuppressedFindingCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/project/{id}/compliance/check/{check_id}/finding/{finding_id}/suppress".format(id=quote(str(id), safe=""),check_id=quote(str(check_id), safe=""),finding_id=quote(str(finding_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostComplianceCheckSuppressAllStandardsFindingResponse200 | PostComplianceCheckSuppressAllStandardsFindingResponse400 | PostComplianceCheckSuppressAllStandardsFindingResponse401 | PostComplianceCheckSuppressAllStandardsFindingResponse403 | PostComplianceCheckSuppressAllStandardsFindingResponse404 | PostComplianceCheckSuppressAllStandardsFindingResponse422 | PostComplianceCheckSuppressAllStandardsFindingResponse500 | None:
    if response.status_code == 200:
        response_200 = PostComplianceCheckSuppressAllStandardsFindingResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PostComplianceCheckSuppressAllStandardsFindingResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostComplianceCheckSuppressAllStandardsFindingResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostComplianceCheckSuppressAllStandardsFindingResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PostComplianceCheckSuppressAllStandardsFindingResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PostComplianceCheckSuppressAllStandardsFindingResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostComplianceCheckSuppressAllStandardsFindingResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostComplianceCheckSuppressAllStandardsFindingResponse200 | PostComplianceCheckSuppressAllStandardsFindingResponse400 | PostComplianceCheckSuppressAllStandardsFindingResponse401 | PostComplianceCheckSuppressAllStandardsFindingResponse403 | PostComplianceCheckSuppressAllStandardsFindingResponse404 | PostComplianceCheckSuppressAllStandardsFindingResponse422 | PostComplianceCheckSuppressAllStandardsFindingResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    check_id: int,
    finding_id: int,
    *,
    client: AuthenticatedClient,
    body: ComplianceCheckSuppressedFindingCreate,

) -> Response[PostComplianceCheckSuppressAllStandardsFindingResponse200 | PostComplianceCheckSuppressAllStandardsFindingResponse400 | PostComplianceCheckSuppressAllStandardsFindingResponse401 | PostComplianceCheckSuppressAllStandardsFindingResponse403 | PostComplianceCheckSuppressAllStandardsFindingResponse404 | PostComplianceCheckSuppressAllStandardsFindingResponse422 | PostComplianceCheckSuppressAllStandardsFindingResponse500]:
    """ Suppresses a Compliance Check Finding by ID in the application.

    Args:
        id (int):
        check_id (int):
        finding_id (int):
        body (ComplianceCheckSuppressedFindingCreate): ComplianceCheckSuppressedFindingCreate
            defines a Compliance Check Suppressed Finding Create.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostComplianceCheckSuppressAllStandardsFindingResponse200 | PostComplianceCheckSuppressAllStandardsFindingResponse400 | PostComplianceCheckSuppressAllStandardsFindingResponse401 | PostComplianceCheckSuppressAllStandardsFindingResponse403 | PostComplianceCheckSuppressAllStandardsFindingResponse404 | PostComplianceCheckSuppressAllStandardsFindingResponse422 | PostComplianceCheckSuppressAllStandardsFindingResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
check_id=check_id,
finding_id=finding_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    check_id: int,
    finding_id: int,
    *,
    client: AuthenticatedClient,
    body: ComplianceCheckSuppressedFindingCreate,

) -> PostComplianceCheckSuppressAllStandardsFindingResponse200 | PostComplianceCheckSuppressAllStandardsFindingResponse400 | PostComplianceCheckSuppressAllStandardsFindingResponse401 | PostComplianceCheckSuppressAllStandardsFindingResponse403 | PostComplianceCheckSuppressAllStandardsFindingResponse404 | PostComplianceCheckSuppressAllStandardsFindingResponse422 | PostComplianceCheckSuppressAllStandardsFindingResponse500 | None:
    """ Suppresses a Compliance Check Finding by ID in the application.

    Args:
        id (int):
        check_id (int):
        finding_id (int):
        body (ComplianceCheckSuppressedFindingCreate): ComplianceCheckSuppressedFindingCreate
            defines a Compliance Check Suppressed Finding Create.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostComplianceCheckSuppressAllStandardsFindingResponse200 | PostComplianceCheckSuppressAllStandardsFindingResponse400 | PostComplianceCheckSuppressAllStandardsFindingResponse401 | PostComplianceCheckSuppressAllStandardsFindingResponse403 | PostComplianceCheckSuppressAllStandardsFindingResponse404 | PostComplianceCheckSuppressAllStandardsFindingResponse422 | PostComplianceCheckSuppressAllStandardsFindingResponse500
     """


    return sync_detailed(
        id=id,
check_id=check_id,
finding_id=finding_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: int,
    check_id: int,
    finding_id: int,
    *,
    client: AuthenticatedClient,
    body: ComplianceCheckSuppressedFindingCreate,

) -> Response[PostComplianceCheckSuppressAllStandardsFindingResponse200 | PostComplianceCheckSuppressAllStandardsFindingResponse400 | PostComplianceCheckSuppressAllStandardsFindingResponse401 | PostComplianceCheckSuppressAllStandardsFindingResponse403 | PostComplianceCheckSuppressAllStandardsFindingResponse404 | PostComplianceCheckSuppressAllStandardsFindingResponse422 | PostComplianceCheckSuppressAllStandardsFindingResponse500]:
    """ Suppresses a Compliance Check Finding by ID in the application.

    Args:
        id (int):
        check_id (int):
        finding_id (int):
        body (ComplianceCheckSuppressedFindingCreate): ComplianceCheckSuppressedFindingCreate
            defines a Compliance Check Suppressed Finding Create.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostComplianceCheckSuppressAllStandardsFindingResponse200 | PostComplianceCheckSuppressAllStandardsFindingResponse400 | PostComplianceCheckSuppressAllStandardsFindingResponse401 | PostComplianceCheckSuppressAllStandardsFindingResponse403 | PostComplianceCheckSuppressAllStandardsFindingResponse404 | PostComplianceCheckSuppressAllStandardsFindingResponse422 | PostComplianceCheckSuppressAllStandardsFindingResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
check_id=check_id,
finding_id=finding_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    check_id: int,
    finding_id: int,
    *,
    client: AuthenticatedClient,
    body: ComplianceCheckSuppressedFindingCreate,

) -> PostComplianceCheckSuppressAllStandardsFindingResponse200 | PostComplianceCheckSuppressAllStandardsFindingResponse400 | PostComplianceCheckSuppressAllStandardsFindingResponse401 | PostComplianceCheckSuppressAllStandardsFindingResponse403 | PostComplianceCheckSuppressAllStandardsFindingResponse404 | PostComplianceCheckSuppressAllStandardsFindingResponse422 | PostComplianceCheckSuppressAllStandardsFindingResponse500 | None:
    """ Suppresses a Compliance Check Finding by ID in the application.

    Args:
        id (int):
        check_id (int):
        finding_id (int):
        body (ComplianceCheckSuppressedFindingCreate): ComplianceCheckSuppressedFindingCreate
            defines a Compliance Check Suppressed Finding Create.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostComplianceCheckSuppressAllStandardsFindingResponse200 | PostComplianceCheckSuppressAllStandardsFindingResponse400 | PostComplianceCheckSuppressAllStandardsFindingResponse401 | PostComplianceCheckSuppressAllStandardsFindingResponse403 | PostComplianceCheckSuppressAllStandardsFindingResponse404 | PostComplianceCheckSuppressAllStandardsFindingResponse422 | PostComplianceCheckSuppressAllStandardsFindingResponse500
     """


    return (await asyncio_detailed(
        id=id,
check_id=check_id,
finding_id=finding_id,
client=client,
body=body,

    )).parsed
