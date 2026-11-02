from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_compliance_control_response_200 import DeleteComplianceControlResponse200
from ...models.delete_compliance_control_response_401 import DeleteComplianceControlResponse401
from ...models.delete_compliance_control_response_403 import DeleteComplianceControlResponse403
from ...models.delete_compliance_control_response_404 import DeleteComplianceControlResponse404
from ...models.delete_compliance_control_response_500 import DeleteComplianceControlResponse500
from typing import cast



def _get_kwargs(
    id: int,
    control_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v4/compliance/program/{id}/control/{control_id}".format(id=quote(str(id), safe=""),control_id=quote(str(control_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteComplianceControlResponse200 | DeleteComplianceControlResponse401 | DeleteComplianceControlResponse403 | DeleteComplianceControlResponse404 | DeleteComplianceControlResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteComplianceControlResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = DeleteComplianceControlResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteComplianceControlResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteComplianceControlResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = DeleteComplianceControlResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteComplianceControlResponse200 | DeleteComplianceControlResponse401 | DeleteComplianceControlResponse403 | DeleteComplianceControlResponse404 | DeleteComplianceControlResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    control_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteComplianceControlResponse200 | DeleteComplianceControlResponse401 | DeleteComplianceControlResponse403 | DeleteComplianceControlResponse404 | DeleteComplianceControlResponse500]:
    """ Deletes the Compliance Control by ID and Compliance Program ID in the application.

    Args:
        id (int):
        control_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteComplianceControlResponse200 | DeleteComplianceControlResponse401 | DeleteComplianceControlResponse403 | DeleteComplianceControlResponse404 | DeleteComplianceControlResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
control_id=control_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    control_id: int,
    *,
    client: AuthenticatedClient,

) -> DeleteComplianceControlResponse200 | DeleteComplianceControlResponse401 | DeleteComplianceControlResponse403 | DeleteComplianceControlResponse404 | DeleteComplianceControlResponse500 | None:
    """ Deletes the Compliance Control by ID and Compliance Program ID in the application.

    Args:
        id (int):
        control_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteComplianceControlResponse200 | DeleteComplianceControlResponse401 | DeleteComplianceControlResponse403 | DeleteComplianceControlResponse404 | DeleteComplianceControlResponse500
     """


    return sync_detailed(
        id=id,
control_id=control_id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    control_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteComplianceControlResponse200 | DeleteComplianceControlResponse401 | DeleteComplianceControlResponse403 | DeleteComplianceControlResponse404 | DeleteComplianceControlResponse500]:
    """ Deletes the Compliance Control by ID and Compliance Program ID in the application.

    Args:
        id (int):
        control_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteComplianceControlResponse200 | DeleteComplianceControlResponse401 | DeleteComplianceControlResponse403 | DeleteComplianceControlResponse404 | DeleteComplianceControlResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
control_id=control_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    control_id: int,
    *,
    client: AuthenticatedClient,

) -> DeleteComplianceControlResponse200 | DeleteComplianceControlResponse401 | DeleteComplianceControlResponse403 | DeleteComplianceControlResponse404 | DeleteComplianceControlResponse500 | None:
    """ Deletes the Compliance Control by ID and Compliance Program ID in the application.

    Args:
        id (int):
        control_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteComplianceControlResponse200 | DeleteComplianceControlResponse401 | DeleteComplianceControlResponse403 | DeleteComplianceControlResponse404 | DeleteComplianceControlResponse500
     """


    return (await asyncio_detailed(
        id=id,
control_id=control_id,
client=client,

    )).parsed
