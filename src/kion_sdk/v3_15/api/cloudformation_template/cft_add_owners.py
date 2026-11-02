from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.cft_add_owners_response_200 import CftAddOwnersResponse200
from ...models.cft_add_owners_response_400 import CftAddOwnersResponse400
from ...models.cft_add_owners_response_401 import CftAddOwnersResponse401
from ...models.cft_add_owners_response_403 import CftAddOwnersResponse403
from ...models.cft_add_owners_response_404 import CftAddOwnersResponse404
from ...models.cft_add_owners_response_422 import CftAddOwnersResponse422
from ...models.cft_add_owners_response_500 import CftAddOwnersResponse500
from ...models.cft_owners import CFTOwners
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: CFTOwners,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/cft/{id}/owner".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CftAddOwnersResponse200 | CftAddOwnersResponse400 | CftAddOwnersResponse401 | CftAddOwnersResponse403 | CftAddOwnersResponse404 | CftAddOwnersResponse422 | CftAddOwnersResponse500 | None:
    if response.status_code == 200:
        response_200 = CftAddOwnersResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = CftAddOwnersResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = CftAddOwnersResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = CftAddOwnersResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = CftAddOwnersResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = CftAddOwnersResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = CftAddOwnersResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CftAddOwnersResponse200 | CftAddOwnersResponse400 | CftAddOwnersResponse401 | CftAddOwnersResponse403 | CftAddOwnersResponse404 | CftAddOwnersResponse422 | CftAddOwnersResponse500]:
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
    body: CFTOwners,

) -> Response[CftAddOwnersResponse200 | CftAddOwnersResponse400 | CftAddOwnersResponse401 | CftAddOwnersResponse403 | CftAddOwnersResponse404 | CftAddOwnersResponse422 | CftAddOwnersResponse500]:
    """ Adds users and groups as owners of the CloudFormation template in the application.

    Args:
        id (int):
        body (CFTOwners): CFTOwners defines the owners of a CloudFormation template.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CftAddOwnersResponse200 | CftAddOwnersResponse400 | CftAddOwnersResponse401 | CftAddOwnersResponse403 | CftAddOwnersResponse404 | CftAddOwnersResponse422 | CftAddOwnersResponse500]
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
    body: CFTOwners,

) -> CftAddOwnersResponse200 | CftAddOwnersResponse400 | CftAddOwnersResponse401 | CftAddOwnersResponse403 | CftAddOwnersResponse404 | CftAddOwnersResponse422 | CftAddOwnersResponse500 | None:
    """ Adds users and groups as owners of the CloudFormation template in the application.

    Args:
        id (int):
        body (CFTOwners): CFTOwners defines the owners of a CloudFormation template.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CftAddOwnersResponse200 | CftAddOwnersResponse400 | CftAddOwnersResponse401 | CftAddOwnersResponse403 | CftAddOwnersResponse404 | CftAddOwnersResponse422 | CftAddOwnersResponse500
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
    body: CFTOwners,

) -> Response[CftAddOwnersResponse200 | CftAddOwnersResponse400 | CftAddOwnersResponse401 | CftAddOwnersResponse403 | CftAddOwnersResponse404 | CftAddOwnersResponse422 | CftAddOwnersResponse500]:
    """ Adds users and groups as owners of the CloudFormation template in the application.

    Args:
        id (int):
        body (CFTOwners): CFTOwners defines the owners of a CloudFormation template.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CftAddOwnersResponse200 | CftAddOwnersResponse400 | CftAddOwnersResponse401 | CftAddOwnersResponse403 | CftAddOwnersResponse404 | CftAddOwnersResponse422 | CftAddOwnersResponse500]
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
    body: CFTOwners,

) -> CftAddOwnersResponse200 | CftAddOwnersResponse400 | CftAddOwnersResponse401 | CftAddOwnersResponse403 | CftAddOwnersResponse404 | CftAddOwnersResponse422 | CftAddOwnersResponse500 | None:
    """ Adds users and groups as owners of the CloudFormation template in the application.

    Args:
        id (int):
        body (CFTOwners): CFTOwners defines the owners of a CloudFormation template.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CftAddOwnersResponse200 | CftAddOwnersResponse400 | CftAddOwnersResponse401 | CftAddOwnersResponse403 | CftAddOwnersResponse404 | CftAddOwnersResponse422 | CftAddOwnersResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
