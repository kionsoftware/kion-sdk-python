from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.ami_update import AMIUpdate
from ...models.patch_ami_response_200 import PatchAMIResponse200
from ...models.patch_ami_response_400 import PatchAMIResponse400
from ...models.patch_ami_response_401 import PatchAMIResponse401
from ...models.patch_ami_response_403 import PatchAMIResponse403
from ...models.patch_ami_response_404 import PatchAMIResponse404
from ...models.patch_ami_response_422 import PatchAMIResponse422
from ...models.patch_ami_response_500 import PatchAMIResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: AMIUpdate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/ami/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchAMIResponse200 | PatchAMIResponse400 | PatchAMIResponse401 | PatchAMIResponse403 | PatchAMIResponse404 | PatchAMIResponse422 | PatchAMIResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchAMIResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchAMIResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PatchAMIResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PatchAMIResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PatchAMIResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PatchAMIResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchAMIResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchAMIResponse200 | PatchAMIResponse400 | PatchAMIResponse401 | PatchAMIResponse403 | PatchAMIResponse404 | PatchAMIResponse422 | PatchAMIResponse500]:
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
    body: AMIUpdate,

) -> Response[PatchAMIResponse200 | PatchAMIResponse400 | PatchAMIResponse401 | PatchAMIResponse403 | PatchAMIResponse404 | PatchAMIResponse422 | PatchAMIResponse500]:
    """ Updates an AMI in the application.

     AMIs exist in AWS accounts that are attached to a project.

    Args:
        id (int):
        body (AMIUpdate): AMIUpdate defines an AMI update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchAMIResponse200 | PatchAMIResponse400 | PatchAMIResponse401 | PatchAMIResponse403 | PatchAMIResponse404 | PatchAMIResponse422 | PatchAMIResponse500]
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
    body: AMIUpdate,

) -> PatchAMIResponse200 | PatchAMIResponse400 | PatchAMIResponse401 | PatchAMIResponse403 | PatchAMIResponse404 | PatchAMIResponse422 | PatchAMIResponse500 | None:
    """ Updates an AMI in the application.

     AMIs exist in AWS accounts that are attached to a project.

    Args:
        id (int):
        body (AMIUpdate): AMIUpdate defines an AMI update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchAMIResponse200 | PatchAMIResponse400 | PatchAMIResponse401 | PatchAMIResponse403 | PatchAMIResponse404 | PatchAMIResponse422 | PatchAMIResponse500
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
    body: AMIUpdate,

) -> Response[PatchAMIResponse200 | PatchAMIResponse400 | PatchAMIResponse401 | PatchAMIResponse403 | PatchAMIResponse404 | PatchAMIResponse422 | PatchAMIResponse500]:
    """ Updates an AMI in the application.

     AMIs exist in AWS accounts that are attached to a project.

    Args:
        id (int):
        body (AMIUpdate): AMIUpdate defines an AMI update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchAMIResponse200 | PatchAMIResponse400 | PatchAMIResponse401 | PatchAMIResponse403 | PatchAMIResponse404 | PatchAMIResponse422 | PatchAMIResponse500]
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
    body: AMIUpdate,

) -> PatchAMIResponse200 | PatchAMIResponse400 | PatchAMIResponse401 | PatchAMIResponse403 | PatchAMIResponse404 | PatchAMIResponse422 | PatchAMIResponse500 | None:
    """ Updates an AMI in the application.

     AMIs exist in AWS accounts that are attached to a project.

    Args:
        id (int):
        body (AMIUpdate): AMIUpdate defines an AMI update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchAMIResponse200 | PatchAMIResponse400 | PatchAMIResponse401 | PatchAMIResponse403 | PatchAMIResponse404 | PatchAMIResponse422 | PatchAMIResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
