from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.patch_service_control_policy_response_200 import PatchServiceControlPolicyResponse200
from ...models.patch_service_control_policy_response_400 import PatchServiceControlPolicyResponse400
from ...models.patch_service_control_policy_response_401 import PatchServiceControlPolicyResponse401
from ...models.patch_service_control_policy_response_403 import PatchServiceControlPolicyResponse403
from ...models.patch_service_control_policy_response_404 import PatchServiceControlPolicyResponse404
from ...models.patch_service_control_policy_response_422 import PatchServiceControlPolicyResponse422
from ...models.patch_service_control_policy_response_500 import PatchServiceControlPolicyResponse500
from ...models.service_control_policy_update import ServiceControlPolicyUpdate
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: ServiceControlPolicyUpdate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/service-control-policy/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchServiceControlPolicyResponse200 | PatchServiceControlPolicyResponse400 | PatchServiceControlPolicyResponse401 | PatchServiceControlPolicyResponse403 | PatchServiceControlPolicyResponse404 | PatchServiceControlPolicyResponse422 | PatchServiceControlPolicyResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchServiceControlPolicyResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchServiceControlPolicyResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchServiceControlPolicyResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchServiceControlPolicyResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PatchServiceControlPolicyResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PatchServiceControlPolicyResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchServiceControlPolicyResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchServiceControlPolicyResponse200 | PatchServiceControlPolicyResponse400 | PatchServiceControlPolicyResponse401 | PatchServiceControlPolicyResponse403 | PatchServiceControlPolicyResponse404 | PatchServiceControlPolicyResponse422 | PatchServiceControlPolicyResponse500]:
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
    body: ServiceControlPolicyUpdate,

) -> Response[PatchServiceControlPolicyResponse200 | PatchServiceControlPolicyResponse400 | PatchServiceControlPolicyResponse401 | PatchServiceControlPolicyResponse403 | PatchServiceControlPolicyResponse404 | PatchServiceControlPolicyResponse422 | PatchServiceControlPolicyResponse500]:
    """ Updates an Service Control Policy by ID in the application.

    Args:
        id (int):
        body (ServiceControlPolicyUpdate): ServiceControlPolicyUpdate defines an Service Control
            policy update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServiceControlPolicyResponse200 | PatchServiceControlPolicyResponse400 | PatchServiceControlPolicyResponse401 | PatchServiceControlPolicyResponse403 | PatchServiceControlPolicyResponse404 | PatchServiceControlPolicyResponse422 | PatchServiceControlPolicyResponse500]
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
    body: ServiceControlPolicyUpdate,

) -> PatchServiceControlPolicyResponse200 | PatchServiceControlPolicyResponse400 | PatchServiceControlPolicyResponse401 | PatchServiceControlPolicyResponse403 | PatchServiceControlPolicyResponse404 | PatchServiceControlPolicyResponse422 | PatchServiceControlPolicyResponse500 | None:
    """ Updates an Service Control Policy by ID in the application.

    Args:
        id (int):
        body (ServiceControlPolicyUpdate): ServiceControlPolicyUpdate defines an Service Control
            policy update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServiceControlPolicyResponse200 | PatchServiceControlPolicyResponse400 | PatchServiceControlPolicyResponse401 | PatchServiceControlPolicyResponse403 | PatchServiceControlPolicyResponse404 | PatchServiceControlPolicyResponse422 | PatchServiceControlPolicyResponse500
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
    body: ServiceControlPolicyUpdate,

) -> Response[PatchServiceControlPolicyResponse200 | PatchServiceControlPolicyResponse400 | PatchServiceControlPolicyResponse401 | PatchServiceControlPolicyResponse403 | PatchServiceControlPolicyResponse404 | PatchServiceControlPolicyResponse422 | PatchServiceControlPolicyResponse500]:
    """ Updates an Service Control Policy by ID in the application.

    Args:
        id (int):
        body (ServiceControlPolicyUpdate): ServiceControlPolicyUpdate defines an Service Control
            policy update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchServiceControlPolicyResponse200 | PatchServiceControlPolicyResponse400 | PatchServiceControlPolicyResponse401 | PatchServiceControlPolicyResponse403 | PatchServiceControlPolicyResponse404 | PatchServiceControlPolicyResponse422 | PatchServiceControlPolicyResponse500]
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
    body: ServiceControlPolicyUpdate,

) -> PatchServiceControlPolicyResponse200 | PatchServiceControlPolicyResponse400 | PatchServiceControlPolicyResponse401 | PatchServiceControlPolicyResponse403 | PatchServiceControlPolicyResponse404 | PatchServiceControlPolicyResponse422 | PatchServiceControlPolicyResponse500 | None:
    """ Updates an Service Control Policy by ID in the application.

    Args:
        id (int):
        body (ServiceControlPolicyUpdate): ServiceControlPolicyUpdate defines an Service Control
            policy update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchServiceControlPolicyResponse200 | PatchServiceControlPolicyResponse400 | PatchServiceControlPolicyResponse401 | PatchServiceControlPolicyResponse403 | PatchServiceControlPolicyResponse404 | PatchServiceControlPolicyResponse422 | PatchServiceControlPolicyResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
