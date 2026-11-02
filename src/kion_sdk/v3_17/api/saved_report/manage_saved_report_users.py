from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.manage_saved_report_users_response_200 import ManageSavedReportUsersResponse200
from ...models.manage_saved_report_users_response_400 import ManageSavedReportUsersResponse400
from ...models.manage_saved_report_users_response_401 import ManageSavedReportUsersResponse401
from ...models.manage_saved_report_users_response_403 import ManageSavedReportUsersResponse403
from ...models.manage_saved_report_users_response_422 import ManageSavedReportUsersResponse422
from ...models.manage_saved_report_users_response_500 import ManageSavedReportUsersResponse500
from ...models.saved_report_sharing import SavedReportSharing
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: SavedReportSharing | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/saved-report/{id}/users".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ManageSavedReportUsersResponse200 | ManageSavedReportUsersResponse400 | ManageSavedReportUsersResponse401 | ManageSavedReportUsersResponse403 | ManageSavedReportUsersResponse422 | ManageSavedReportUsersResponse500 | None:
    if response.status_code == 200:
        response_200 = ManageSavedReportUsersResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ManageSavedReportUsersResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ManageSavedReportUsersResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = ManageSavedReportUsersResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = ManageSavedReportUsersResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = ManageSavedReportUsersResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ManageSavedReportUsersResponse200 | ManageSavedReportUsersResponse400 | ManageSavedReportUsersResponse401 | ManageSavedReportUsersResponse403 | ManageSavedReportUsersResponse422 | ManageSavedReportUsersResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: SavedReportSharing | Unset = UNSET,

) -> Response[ManageSavedReportUsersResponse200 | ManageSavedReportUsersResponse400 | ManageSavedReportUsersResponse401 | ManageSavedReportUsersResponse403 | ManageSavedReportUsersResponse422 | ManageSavedReportUsersResponse500]:
    """ Updates the assigned users for a saved report by saved report ID.

     This includes excluded users and user groups for global reports and lists of included users and user
    groups for non-global reports.

    Args:
        id (int):
        body (SavedReportSharing | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ManageSavedReportUsersResponse200 | ManageSavedReportUsersResponse400 | ManageSavedReportUsersResponse401 | ManageSavedReportUsersResponse403 | ManageSavedReportUsersResponse422 | ManageSavedReportUsersResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: SavedReportSharing | Unset = UNSET,

) -> ManageSavedReportUsersResponse200 | ManageSavedReportUsersResponse400 | ManageSavedReportUsersResponse401 | ManageSavedReportUsersResponse403 | ManageSavedReportUsersResponse422 | ManageSavedReportUsersResponse500 | None:
    """ Updates the assigned users for a saved report by saved report ID.

     This includes excluded users and user groups for global reports and lists of included users and user
    groups for non-global reports.

    Args:
        id (int):
        body (SavedReportSharing | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ManageSavedReportUsersResponse200 | ManageSavedReportUsersResponse400 | ManageSavedReportUsersResponse401 | ManageSavedReportUsersResponse403 | ManageSavedReportUsersResponse422 | ManageSavedReportUsersResponse500
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: SavedReportSharing | Unset = UNSET,

) -> Response[ManageSavedReportUsersResponse200 | ManageSavedReportUsersResponse400 | ManageSavedReportUsersResponse401 | ManageSavedReportUsersResponse403 | ManageSavedReportUsersResponse422 | ManageSavedReportUsersResponse500]:
    """ Updates the assigned users for a saved report by saved report ID.

     This includes excluded users and user groups for global reports and lists of included users and user
    groups for non-global reports.

    Args:
        id (int):
        body (SavedReportSharing | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ManageSavedReportUsersResponse200 | ManageSavedReportUsersResponse400 | ManageSavedReportUsersResponse401 | ManageSavedReportUsersResponse403 | ManageSavedReportUsersResponse422 | ManageSavedReportUsersResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: SavedReportSharing | Unset = UNSET,

) -> ManageSavedReportUsersResponse200 | ManageSavedReportUsersResponse400 | ManageSavedReportUsersResponse401 | ManageSavedReportUsersResponse403 | ManageSavedReportUsersResponse422 | ManageSavedReportUsersResponse500 | None:
    """ Updates the assigned users for a saved report by saved report ID.

     This includes excluded users and user groups for global reports and lists of included users and user
    groups for non-global reports.

    Args:
        id (int):
        body (SavedReportSharing | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ManageSavedReportUsersResponse200 | ManageSavedReportUsersResponse400 | ManageSavedReportUsersResponse401 | ManageSavedReportUsersResponse403 | ManageSavedReportUsersResponse422 | ManageSavedReportUsersResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
