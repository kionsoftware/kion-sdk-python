from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_archive_account_standard_findings_response_200 import DeleteArchiveAccountStandardFindingsResponse200
from ...models.delete_archive_account_standard_findings_response_401 import DeleteArchiveAccountStandardFindingsResponse401
from ...models.delete_archive_account_standard_findings_response_403 import DeleteArchiveAccountStandardFindingsResponse403
from ...models.delete_archive_account_standard_findings_response_404 import DeleteArchiveAccountStandardFindingsResponse404
from ...models.delete_archive_account_standard_findings_response_500 import DeleteArchiveAccountStandardFindingsResponse500
from typing import cast



def _get_kwargs(
    id: int,
    standard_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/account/{id}/compliance/standard/{standard_id}/archive".format(id=quote(str(id), safe=""),standard_id=quote(str(standard_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteArchiveAccountStandardFindingsResponse200 | DeleteArchiveAccountStandardFindingsResponse401 | DeleteArchiveAccountStandardFindingsResponse403 | DeleteArchiveAccountStandardFindingsResponse404 | DeleteArchiveAccountStandardFindingsResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteArchiveAccountStandardFindingsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DeleteArchiveAccountStandardFindingsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteArchiveAccountStandardFindingsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteArchiveAccountStandardFindingsResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = DeleteArchiveAccountStandardFindingsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteArchiveAccountStandardFindingsResponse200 | DeleteArchiveAccountStandardFindingsResponse401 | DeleteArchiveAccountStandardFindingsResponse403 | DeleteArchiveAccountStandardFindingsResponse404 | DeleteArchiveAccountStandardFindingsResponse500]:
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

) -> Response[DeleteArchiveAccountStandardFindingsResponse200 | DeleteArchiveAccountStandardFindingsResponse401 | DeleteArchiveAccountStandardFindingsResponse403 | DeleteArchiveAccountStandardFindingsResponse404 | DeleteArchiveAccountStandardFindingsResponse500]:
    """ Archives all findings given account and standard id.

    Args:
        id (int):
        standard_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteArchiveAccountStandardFindingsResponse200 | DeleteArchiveAccountStandardFindingsResponse401 | DeleteArchiveAccountStandardFindingsResponse403 | DeleteArchiveAccountStandardFindingsResponse404 | DeleteArchiveAccountStandardFindingsResponse500]
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

) -> DeleteArchiveAccountStandardFindingsResponse200 | DeleteArchiveAccountStandardFindingsResponse401 | DeleteArchiveAccountStandardFindingsResponse403 | DeleteArchiveAccountStandardFindingsResponse404 | DeleteArchiveAccountStandardFindingsResponse500 | None:
    """ Archives all findings given account and standard id.

    Args:
        id (int):
        standard_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteArchiveAccountStandardFindingsResponse200 | DeleteArchiveAccountStandardFindingsResponse401 | DeleteArchiveAccountStandardFindingsResponse403 | DeleteArchiveAccountStandardFindingsResponse404 | DeleteArchiveAccountStandardFindingsResponse500
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

) -> Response[DeleteArchiveAccountStandardFindingsResponse200 | DeleteArchiveAccountStandardFindingsResponse401 | DeleteArchiveAccountStandardFindingsResponse403 | DeleteArchiveAccountStandardFindingsResponse404 | DeleteArchiveAccountStandardFindingsResponse500]:
    """ Archives all findings given account and standard id.

    Args:
        id (int):
        standard_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteArchiveAccountStandardFindingsResponse200 | DeleteArchiveAccountStandardFindingsResponse401 | DeleteArchiveAccountStandardFindingsResponse403 | DeleteArchiveAccountStandardFindingsResponse404 | DeleteArchiveAccountStandardFindingsResponse500]
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

) -> DeleteArchiveAccountStandardFindingsResponse200 | DeleteArchiveAccountStandardFindingsResponse401 | DeleteArchiveAccountStandardFindingsResponse403 | DeleteArchiveAccountStandardFindingsResponse404 | DeleteArchiveAccountStandardFindingsResponse500 | None:
    """ Archives all findings given account and standard id.

    Args:
        id (int):
        standard_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteArchiveAccountStandardFindingsResponse200 | DeleteArchiveAccountStandardFindingsResponse401 | DeleteArchiveAccountStandardFindingsResponse403 | DeleteArchiveAccountStandardFindingsResponse404 | DeleteArchiveAccountStandardFindingsResponse500
     """


    return (await asyncio_detailed(
        id=id,
standard_id=standard_id,
client=client,

    )).parsed
