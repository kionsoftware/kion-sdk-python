from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_archive_account_check_finding_response_200 import DeleteArchiveAccountCheckFindingResponse200
from ...models.delete_archive_account_check_finding_response_401 import DeleteArchiveAccountCheckFindingResponse401
from ...models.delete_archive_account_check_finding_response_403 import DeleteArchiveAccountCheckFindingResponse403
from ...models.delete_archive_account_check_finding_response_404 import DeleteArchiveAccountCheckFindingResponse404
from ...models.delete_archive_account_check_finding_response_500 import DeleteArchiveAccountCheckFindingResponse500
from typing import cast



def _get_kwargs(
    id: int,
    check_id: int,
    finding_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/account/{id}/compliance/check/{check_id}/finding/{finding_id}/archive".format(id=quote(str(id), safe=""),check_id=quote(str(check_id), safe=""),finding_id=quote(str(finding_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteArchiveAccountCheckFindingResponse200 | DeleteArchiveAccountCheckFindingResponse401 | DeleteArchiveAccountCheckFindingResponse403 | DeleteArchiveAccountCheckFindingResponse404 | DeleteArchiveAccountCheckFindingResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteArchiveAccountCheckFindingResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DeleteArchiveAccountCheckFindingResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteArchiveAccountCheckFindingResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteArchiveAccountCheckFindingResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = DeleteArchiveAccountCheckFindingResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteArchiveAccountCheckFindingResponse200 | DeleteArchiveAccountCheckFindingResponse401 | DeleteArchiveAccountCheckFindingResponse403 | DeleteArchiveAccountCheckFindingResponse404 | DeleteArchiveAccountCheckFindingResponse500]:
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

) -> Response[DeleteArchiveAccountCheckFindingResponse200 | DeleteArchiveAccountCheckFindingResponse401 | DeleteArchiveAccountCheckFindingResponse403 | DeleteArchiveAccountCheckFindingResponse404 | DeleteArchiveAccountCheckFindingResponse500]:
    """ Archives a single finding for a given account, check and finding id.

    Args:
        id (int):
        check_id (int):
        finding_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteArchiveAccountCheckFindingResponse200 | DeleteArchiveAccountCheckFindingResponse401 | DeleteArchiveAccountCheckFindingResponse403 | DeleteArchiveAccountCheckFindingResponse404 | DeleteArchiveAccountCheckFindingResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
check_id=check_id,
finding_id=finding_id,

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

) -> DeleteArchiveAccountCheckFindingResponse200 | DeleteArchiveAccountCheckFindingResponse401 | DeleteArchiveAccountCheckFindingResponse403 | DeleteArchiveAccountCheckFindingResponse404 | DeleteArchiveAccountCheckFindingResponse500 | None:
    """ Archives a single finding for a given account, check and finding id.

    Args:
        id (int):
        check_id (int):
        finding_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteArchiveAccountCheckFindingResponse200 | DeleteArchiveAccountCheckFindingResponse401 | DeleteArchiveAccountCheckFindingResponse403 | DeleteArchiveAccountCheckFindingResponse404 | DeleteArchiveAccountCheckFindingResponse500
     """


    return sync_detailed(
        id=id,
check_id=check_id,
finding_id=finding_id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    check_id: int,
    finding_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteArchiveAccountCheckFindingResponse200 | DeleteArchiveAccountCheckFindingResponse401 | DeleteArchiveAccountCheckFindingResponse403 | DeleteArchiveAccountCheckFindingResponse404 | DeleteArchiveAccountCheckFindingResponse500]:
    """ Archives a single finding for a given account, check and finding id.

    Args:
        id (int):
        check_id (int):
        finding_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteArchiveAccountCheckFindingResponse200 | DeleteArchiveAccountCheckFindingResponse401 | DeleteArchiveAccountCheckFindingResponse403 | DeleteArchiveAccountCheckFindingResponse404 | DeleteArchiveAccountCheckFindingResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
check_id=check_id,
finding_id=finding_id,

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

) -> DeleteArchiveAccountCheckFindingResponse200 | DeleteArchiveAccountCheckFindingResponse401 | DeleteArchiveAccountCheckFindingResponse403 | DeleteArchiveAccountCheckFindingResponse404 | DeleteArchiveAccountCheckFindingResponse500 | None:
    """ Archives a single finding for a given account, check and finding id.

    Args:
        id (int):
        check_id (int):
        finding_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteArchiveAccountCheckFindingResponse200 | DeleteArchiveAccountCheckFindingResponse401 | DeleteArchiveAccountCheckFindingResponse403 | DeleteArchiveAccountCheckFindingResponse404 | DeleteArchiveAccountCheckFindingResponse500
     """


    return (await asyncio_detailed(
        id=id,
check_id=check_id,
finding_id=finding_id,
client=client,

    )).parsed
