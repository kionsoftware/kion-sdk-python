from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_compliance_check_archive_all_project_standard_findings_response_200 import DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse200
from ...models.delete_compliance_check_archive_all_project_standard_findings_response_401 import DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse401
from ...models.delete_compliance_check_archive_all_project_standard_findings_response_403 import DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse403
from ...models.delete_compliance_check_archive_all_project_standard_findings_response_404 import DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse404
from ...models.delete_compliance_check_archive_all_project_standard_findings_response_500 import DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse500
from typing import cast



def _get_kwargs(
    id: int,
    standard_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/project/{id}/compliance/standard/{standard_id}/archive".format(id=quote(str(id), safe=""),standard_id=quote(str(standard_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse200 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse401 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse403 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse404 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse200 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse401 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse403 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse404 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse500]:
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

) -> Response[DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse200 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse401 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse403 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse404 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse500]:
    """ Archives all compliance check findings for a given project, standard, and check id.

    Args:
        id (int):
        standard_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse200 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse401 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse403 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse404 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse500]
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

) -> DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse200 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse401 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse403 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse404 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse500 | None:
    """ Archives all compliance check findings for a given project, standard, and check id.

    Args:
        id (int):
        standard_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse200 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse401 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse403 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse404 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse500
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

) -> Response[DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse200 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse401 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse403 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse404 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse500]:
    """ Archives all compliance check findings for a given project, standard, and check id.

    Args:
        id (int):
        standard_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse200 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse401 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse403 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse404 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse500]
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

) -> DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse200 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse401 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse403 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse404 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse500 | None:
    """ Archives all compliance check findings for a given project, standard, and check id.

    Args:
        id (int):
        standard_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse200 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse401 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse403 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse404 | DeleteComplianceCheckArchiveAllProjectStandardFindingsResponse500
     """


    return (await asyncio_detailed(
        id=id,
standard_id=standard_id,
client=client,

    )).parsed
