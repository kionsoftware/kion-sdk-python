from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_compliance_check_archive_all_project_check_findings_response_200 import DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse200
from ...models.delete_compliance_check_archive_all_project_check_findings_response_401 import DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse401
from ...models.delete_compliance_check_archive_all_project_check_findings_response_403 import DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse403
from ...models.delete_compliance_check_archive_all_project_check_findings_response_404 import DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse404
from ...models.delete_compliance_check_archive_all_project_check_findings_response_500 import DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse500
from typing import cast



def _get_kwargs(
    id: int,
    check_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/project/{id}/compliance/check/{check_id}/archive".format(id=quote(str(id), safe=""),check_id=quote(str(check_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse200 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse401 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse403 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse404 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse200 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse401 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse403 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse404 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse500]:
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

) -> Response[DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse200 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse401 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse403 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse404 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse500]:
    """ Archives all compliance check findings for a given project and check id.

    Args:
        id (int):
        check_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse200 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse401 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse403 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse404 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse500]
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

) -> DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse200 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse401 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse403 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse404 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse500 | None:
    """ Archives all compliance check findings for a given project and check id.

    Args:
        id (int):
        check_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse200 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse401 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse403 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse404 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse500
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

) -> Response[DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse200 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse401 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse403 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse404 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse500]:
    """ Archives all compliance check findings for a given project and check id.

    Args:
        id (int):
        check_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse200 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse401 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse403 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse404 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse500]
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

) -> DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse200 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse401 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse403 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse404 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse500 | None:
    """ Archives all compliance check findings for a given project and check id.

    Args:
        id (int):
        check_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse200 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse401 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse403 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse404 | DeleteComplianceCheckArchiveAllProjectCheckFindingsResponse500
     """


    return (await asyncio_detailed(
        id=id,
check_id=check_id,
client=client,

    )).parsed
