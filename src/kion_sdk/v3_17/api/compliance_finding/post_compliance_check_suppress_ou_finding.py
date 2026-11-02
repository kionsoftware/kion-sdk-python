from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.compliance_check_suppressed_finding_create import ComplianceCheckSuppressedFindingCreate
from ...models.post_compliance_check_suppress_ou_finding_response_200 import PostComplianceCheckSuppressOUFindingResponse200
from ...models.post_compliance_check_suppress_ou_finding_response_400 import PostComplianceCheckSuppressOUFindingResponse400
from ...models.post_compliance_check_suppress_ou_finding_response_401 import PostComplianceCheckSuppressOUFindingResponse401
from ...models.post_compliance_check_suppress_ou_finding_response_403 import PostComplianceCheckSuppressOUFindingResponse403
from ...models.post_compliance_check_suppress_ou_finding_response_404 import PostComplianceCheckSuppressOUFindingResponse404
from ...models.post_compliance_check_suppress_ou_finding_response_422 import PostComplianceCheckSuppressOUFindingResponse422
from ...models.post_compliance_check_suppress_ou_finding_response_500 import PostComplianceCheckSuppressOUFindingResponse500
from typing import cast



def _get_kwargs(
    id: int,
    standard_id: int,
    check_id: int,
    finding_id: int,
    *,
    body: ComplianceCheckSuppressedFindingCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/ou/{id}/compliance/standard/{standard_id}/check/{check_id}/finding/{finding_id}/suppress".format(id=quote(str(id), safe=""),standard_id=quote(str(standard_id), safe=""),check_id=quote(str(check_id), safe=""),finding_id=quote(str(finding_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostComplianceCheckSuppressOUFindingResponse200 | PostComplianceCheckSuppressOUFindingResponse400 | PostComplianceCheckSuppressOUFindingResponse401 | PostComplianceCheckSuppressOUFindingResponse403 | PostComplianceCheckSuppressOUFindingResponse404 | PostComplianceCheckSuppressOUFindingResponse422 | PostComplianceCheckSuppressOUFindingResponse500 | None:
    if response.status_code == 200:
        response_200 = PostComplianceCheckSuppressOUFindingResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PostComplianceCheckSuppressOUFindingResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostComplianceCheckSuppressOUFindingResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostComplianceCheckSuppressOUFindingResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PostComplianceCheckSuppressOUFindingResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PostComplianceCheckSuppressOUFindingResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostComplianceCheckSuppressOUFindingResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostComplianceCheckSuppressOUFindingResponse200 | PostComplianceCheckSuppressOUFindingResponse400 | PostComplianceCheckSuppressOUFindingResponse401 | PostComplianceCheckSuppressOUFindingResponse403 | PostComplianceCheckSuppressOUFindingResponse404 | PostComplianceCheckSuppressOUFindingResponse422 | PostComplianceCheckSuppressOUFindingResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    standard_id: int,
    check_id: int,
    finding_id: int,
    *,
    client: AuthenticatedClient,
    body: ComplianceCheckSuppressedFindingCreate,

) -> Response[PostComplianceCheckSuppressOUFindingResponse200 | PostComplianceCheckSuppressOUFindingResponse400 | PostComplianceCheckSuppressOUFindingResponse401 | PostComplianceCheckSuppressOUFindingResponse403 | PostComplianceCheckSuppressOUFindingResponse404 | PostComplianceCheckSuppressOUFindingResponse422 | PostComplianceCheckSuppressOUFindingResponse500]:
    """ Suppresses a Compliance Check Finding by ID in the application within OU ID, Standard ID and Check
    ID scope.

    Args:
        id (int):
        standard_id (int):
        check_id (int):
        finding_id (int):
        body (ComplianceCheckSuppressedFindingCreate): ComplianceCheckSuppressedFindingCreate
            defines a Compliance Check Suppressed Finding Create.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostComplianceCheckSuppressOUFindingResponse200 | PostComplianceCheckSuppressOUFindingResponse400 | PostComplianceCheckSuppressOUFindingResponse401 | PostComplianceCheckSuppressOUFindingResponse403 | PostComplianceCheckSuppressOUFindingResponse404 | PostComplianceCheckSuppressOUFindingResponse422 | PostComplianceCheckSuppressOUFindingResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
standard_id=standard_id,
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
    standard_id: int,
    check_id: int,
    finding_id: int,
    *,
    client: AuthenticatedClient,
    body: ComplianceCheckSuppressedFindingCreate,

) -> PostComplianceCheckSuppressOUFindingResponse200 | PostComplianceCheckSuppressOUFindingResponse400 | PostComplianceCheckSuppressOUFindingResponse401 | PostComplianceCheckSuppressOUFindingResponse403 | PostComplianceCheckSuppressOUFindingResponse404 | PostComplianceCheckSuppressOUFindingResponse422 | PostComplianceCheckSuppressOUFindingResponse500 | None:
    """ Suppresses a Compliance Check Finding by ID in the application within OU ID, Standard ID and Check
    ID scope.

    Args:
        id (int):
        standard_id (int):
        check_id (int):
        finding_id (int):
        body (ComplianceCheckSuppressedFindingCreate): ComplianceCheckSuppressedFindingCreate
            defines a Compliance Check Suppressed Finding Create.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostComplianceCheckSuppressOUFindingResponse200 | PostComplianceCheckSuppressOUFindingResponse400 | PostComplianceCheckSuppressOUFindingResponse401 | PostComplianceCheckSuppressOUFindingResponse403 | PostComplianceCheckSuppressOUFindingResponse404 | PostComplianceCheckSuppressOUFindingResponse422 | PostComplianceCheckSuppressOUFindingResponse500
     """


    return sync_detailed(
        id=id,
standard_id=standard_id,
check_id=check_id,
finding_id=finding_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: int,
    standard_id: int,
    check_id: int,
    finding_id: int,
    *,
    client: AuthenticatedClient,
    body: ComplianceCheckSuppressedFindingCreate,

) -> Response[PostComplianceCheckSuppressOUFindingResponse200 | PostComplianceCheckSuppressOUFindingResponse400 | PostComplianceCheckSuppressOUFindingResponse401 | PostComplianceCheckSuppressOUFindingResponse403 | PostComplianceCheckSuppressOUFindingResponse404 | PostComplianceCheckSuppressOUFindingResponse422 | PostComplianceCheckSuppressOUFindingResponse500]:
    """ Suppresses a Compliance Check Finding by ID in the application within OU ID, Standard ID and Check
    ID scope.

    Args:
        id (int):
        standard_id (int):
        check_id (int):
        finding_id (int):
        body (ComplianceCheckSuppressedFindingCreate): ComplianceCheckSuppressedFindingCreate
            defines a Compliance Check Suppressed Finding Create.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostComplianceCheckSuppressOUFindingResponse200 | PostComplianceCheckSuppressOUFindingResponse400 | PostComplianceCheckSuppressOUFindingResponse401 | PostComplianceCheckSuppressOUFindingResponse403 | PostComplianceCheckSuppressOUFindingResponse404 | PostComplianceCheckSuppressOUFindingResponse422 | PostComplianceCheckSuppressOUFindingResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
standard_id=standard_id,
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
    standard_id: int,
    check_id: int,
    finding_id: int,
    *,
    client: AuthenticatedClient,
    body: ComplianceCheckSuppressedFindingCreate,

) -> PostComplianceCheckSuppressOUFindingResponse200 | PostComplianceCheckSuppressOUFindingResponse400 | PostComplianceCheckSuppressOUFindingResponse401 | PostComplianceCheckSuppressOUFindingResponse403 | PostComplianceCheckSuppressOUFindingResponse404 | PostComplianceCheckSuppressOUFindingResponse422 | PostComplianceCheckSuppressOUFindingResponse500 | None:
    """ Suppresses a Compliance Check Finding by ID in the application within OU ID, Standard ID and Check
    ID scope.

    Args:
        id (int):
        standard_id (int):
        check_id (int):
        finding_id (int):
        body (ComplianceCheckSuppressedFindingCreate): ComplianceCheckSuppressedFindingCreate
            defines a Compliance Check Suppressed Finding Create.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostComplianceCheckSuppressOUFindingResponse200 | PostComplianceCheckSuppressOUFindingResponse400 | PostComplianceCheckSuppressOUFindingResponse401 | PostComplianceCheckSuppressOUFindingResponse403 | PostComplianceCheckSuppressOUFindingResponse404 | PostComplianceCheckSuppressOUFindingResponse422 | PostComplianceCheckSuppressOUFindingResponse500
     """


    return (await asyncio_detailed(
        id=id,
standard_id=standard_id,
check_id=check_id,
finding_id=finding_id,
client=client,
body=body,

    )).parsed
