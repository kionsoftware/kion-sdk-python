from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_compliance_check_suppressed_finding_response_200 import DeleteComplianceCheckSuppressedFindingResponse200
from ...models.delete_compliance_check_suppressed_finding_response_401 import DeleteComplianceCheckSuppressedFindingResponse401
from ...models.delete_compliance_check_suppressed_finding_response_403 import DeleteComplianceCheckSuppressedFindingResponse403
from ...models.delete_compliance_check_suppressed_finding_response_404 import DeleteComplianceCheckSuppressedFindingResponse404
from ...models.delete_compliance_check_suppressed_finding_response_500 import DeleteComplianceCheckSuppressedFindingResponse500
from typing import cast



def _get_kwargs(
    id: int,
    check_id: int,
    suppressed_finding_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/project/{id}/compliance/check/{check_id}/suppressed-finding/{suppressed_finding_id}/un-suppress".format(id=quote(str(id), safe=""),check_id=quote(str(check_id), safe=""),suppressed_finding_id=quote(str(suppressed_finding_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteComplianceCheckSuppressedFindingResponse200 | DeleteComplianceCheckSuppressedFindingResponse401 | DeleteComplianceCheckSuppressedFindingResponse403 | DeleteComplianceCheckSuppressedFindingResponse404 | DeleteComplianceCheckSuppressedFindingResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteComplianceCheckSuppressedFindingResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DeleteComplianceCheckSuppressedFindingResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteComplianceCheckSuppressedFindingResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteComplianceCheckSuppressedFindingResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = DeleteComplianceCheckSuppressedFindingResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteComplianceCheckSuppressedFindingResponse200 | DeleteComplianceCheckSuppressedFindingResponse401 | DeleteComplianceCheckSuppressedFindingResponse403 | DeleteComplianceCheckSuppressedFindingResponse404 | DeleteComplianceCheckSuppressedFindingResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    check_id: int,
    suppressed_finding_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteComplianceCheckSuppressedFindingResponse200 | DeleteComplianceCheckSuppressedFindingResponse401 | DeleteComplianceCheckSuppressedFindingResponse403 | DeleteComplianceCheckSuppressedFindingResponse404 | DeleteComplianceCheckSuppressedFindingResponse500]:
    """ UnSuppressFinding a Compliance Check Finding by ID in the application.

    Args:
        id (int):
        check_id (int):
        suppressed_finding_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteComplianceCheckSuppressedFindingResponse200 | DeleteComplianceCheckSuppressedFindingResponse401 | DeleteComplianceCheckSuppressedFindingResponse403 | DeleteComplianceCheckSuppressedFindingResponse404 | DeleteComplianceCheckSuppressedFindingResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
check_id=check_id,
suppressed_finding_id=suppressed_finding_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    check_id: int,
    suppressed_finding_id: int,
    *,
    client: AuthenticatedClient,

) -> DeleteComplianceCheckSuppressedFindingResponse200 | DeleteComplianceCheckSuppressedFindingResponse401 | DeleteComplianceCheckSuppressedFindingResponse403 | DeleteComplianceCheckSuppressedFindingResponse404 | DeleteComplianceCheckSuppressedFindingResponse500 | None:
    """ UnSuppressFinding a Compliance Check Finding by ID in the application.

    Args:
        id (int):
        check_id (int):
        suppressed_finding_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteComplianceCheckSuppressedFindingResponse200 | DeleteComplianceCheckSuppressedFindingResponse401 | DeleteComplianceCheckSuppressedFindingResponse403 | DeleteComplianceCheckSuppressedFindingResponse404 | DeleteComplianceCheckSuppressedFindingResponse500
     """


    return sync_detailed(
        id=id,
check_id=check_id,
suppressed_finding_id=suppressed_finding_id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    check_id: int,
    suppressed_finding_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteComplianceCheckSuppressedFindingResponse200 | DeleteComplianceCheckSuppressedFindingResponse401 | DeleteComplianceCheckSuppressedFindingResponse403 | DeleteComplianceCheckSuppressedFindingResponse404 | DeleteComplianceCheckSuppressedFindingResponse500]:
    """ UnSuppressFinding a Compliance Check Finding by ID in the application.

    Args:
        id (int):
        check_id (int):
        suppressed_finding_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteComplianceCheckSuppressedFindingResponse200 | DeleteComplianceCheckSuppressedFindingResponse401 | DeleteComplianceCheckSuppressedFindingResponse403 | DeleteComplianceCheckSuppressedFindingResponse404 | DeleteComplianceCheckSuppressedFindingResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
check_id=check_id,
suppressed_finding_id=suppressed_finding_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    check_id: int,
    suppressed_finding_id: int,
    *,
    client: AuthenticatedClient,

) -> DeleteComplianceCheckSuppressedFindingResponse200 | DeleteComplianceCheckSuppressedFindingResponse401 | DeleteComplianceCheckSuppressedFindingResponse403 | DeleteComplianceCheckSuppressedFindingResponse404 | DeleteComplianceCheckSuppressedFindingResponse500 | None:
    """ UnSuppressFinding a Compliance Check Finding by ID in the application.

    Args:
        id (int):
        check_id (int):
        suppressed_finding_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteComplianceCheckSuppressedFindingResponse200 | DeleteComplianceCheckSuppressedFindingResponse401 | DeleteComplianceCheckSuppressedFindingResponse403 | DeleteComplianceCheckSuppressedFindingResponse404 | DeleteComplianceCheckSuppressedFindingResponse500
     """


    return (await asyncio_detailed(
        id=id,
check_id=check_id,
suppressed_finding_id=suppressed_finding_id,
client=client,

    )).parsed
