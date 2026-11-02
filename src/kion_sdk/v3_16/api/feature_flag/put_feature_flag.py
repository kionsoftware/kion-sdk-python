from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.feature_flag_update import FeatureFlagUpdate
from ...models.put_feature_flag_response_200 import PutFeatureFlagResponse200
from ...models.put_feature_flag_response_400 import PutFeatureFlagResponse400
from ...models.put_feature_flag_response_401 import PutFeatureFlagResponse401
from ...models.put_feature_flag_response_403 import PutFeatureFlagResponse403
from ...models.put_feature_flag_response_404 import PutFeatureFlagResponse404
from ...models.put_feature_flag_response_422 import PutFeatureFlagResponse422
from ...models.put_feature_flag_response_500 import PutFeatureFlagResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    flag: str,
    *,
    body: FeatureFlagUpdate,
    exclude_nested: bool | Unset = False,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["excludeNested"] = exclude_nested


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v3/feature-flag/{flag}".format(flag=quote(str(flag), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PutFeatureFlagResponse200 | PutFeatureFlagResponse400 | PutFeatureFlagResponse401 | PutFeatureFlagResponse403 | PutFeatureFlagResponse404 | PutFeatureFlagResponse422 | PutFeatureFlagResponse500 | None:
    if response.status_code == 200:
        response_200 = PutFeatureFlagResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PutFeatureFlagResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PutFeatureFlagResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PutFeatureFlagResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PutFeatureFlagResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PutFeatureFlagResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PutFeatureFlagResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PutFeatureFlagResponse200 | PutFeatureFlagResponse400 | PutFeatureFlagResponse401 | PutFeatureFlagResponse403 | PutFeatureFlagResponse404 | PutFeatureFlagResponse422 | PutFeatureFlagResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    flag: str,
    *,
    client: AuthenticatedClient,
    body: FeatureFlagUpdate,
    exclude_nested: bool | Unset = False,

) -> Response[PutFeatureFlagResponse200 | PutFeatureFlagResponse400 | PutFeatureFlagResponse401 | PutFeatureFlagResponse403 | PutFeatureFlagResponse404 | PutFeatureFlagResponse422 | PutFeatureFlagResponse500]:
    """ Updates a feature flag to be enabled or disabled

    Args:
        flag (str):
        exclude_nested (bool | Unset):  Default: False.
        body (FeatureFlagUpdate): FeatureFlagUpdate is the model for updating an existing feature
            flag

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutFeatureFlagResponse200 | PutFeatureFlagResponse400 | PutFeatureFlagResponse401 | PutFeatureFlagResponse403 | PutFeatureFlagResponse404 | PutFeatureFlagResponse422 | PutFeatureFlagResponse500]
     """


    kwargs = _get_kwargs(
        flag=flag,
body=body,
exclude_nested=exclude_nested,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    flag: str,
    *,
    client: AuthenticatedClient,
    body: FeatureFlagUpdate,
    exclude_nested: bool | Unset = False,

) -> PutFeatureFlagResponse200 | PutFeatureFlagResponse400 | PutFeatureFlagResponse401 | PutFeatureFlagResponse403 | PutFeatureFlagResponse404 | PutFeatureFlagResponse422 | PutFeatureFlagResponse500 | None:
    """ Updates a feature flag to be enabled or disabled

    Args:
        flag (str):
        exclude_nested (bool | Unset):  Default: False.
        body (FeatureFlagUpdate): FeatureFlagUpdate is the model for updating an existing feature
            flag

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutFeatureFlagResponse200 | PutFeatureFlagResponse400 | PutFeatureFlagResponse401 | PutFeatureFlagResponse403 | PutFeatureFlagResponse404 | PutFeatureFlagResponse422 | PutFeatureFlagResponse500
     """


    return sync_detailed(
        flag=flag,
client=client,
body=body,
exclude_nested=exclude_nested,

    ).parsed

async def asyncio_detailed(
    flag: str,
    *,
    client: AuthenticatedClient,
    body: FeatureFlagUpdate,
    exclude_nested: bool | Unset = False,

) -> Response[PutFeatureFlagResponse200 | PutFeatureFlagResponse400 | PutFeatureFlagResponse401 | PutFeatureFlagResponse403 | PutFeatureFlagResponse404 | PutFeatureFlagResponse422 | PutFeatureFlagResponse500]:
    """ Updates a feature flag to be enabled or disabled

    Args:
        flag (str):
        exclude_nested (bool | Unset):  Default: False.
        body (FeatureFlagUpdate): FeatureFlagUpdate is the model for updating an existing feature
            flag

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutFeatureFlagResponse200 | PutFeatureFlagResponse400 | PutFeatureFlagResponse401 | PutFeatureFlagResponse403 | PutFeatureFlagResponse404 | PutFeatureFlagResponse422 | PutFeatureFlagResponse500]
     """


    kwargs = _get_kwargs(
        flag=flag,
body=body,
exclude_nested=exclude_nested,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    flag: str,
    *,
    client: AuthenticatedClient,
    body: FeatureFlagUpdate,
    exclude_nested: bool | Unset = False,

) -> PutFeatureFlagResponse200 | PutFeatureFlagResponse400 | PutFeatureFlagResponse401 | PutFeatureFlagResponse403 | PutFeatureFlagResponse404 | PutFeatureFlagResponse422 | PutFeatureFlagResponse500 | None:
    """ Updates a feature flag to be enabled or disabled

    Args:
        flag (str):
        exclude_nested (bool | Unset):  Default: False.
        body (FeatureFlagUpdate): FeatureFlagUpdate is the model for updating an existing feature
            flag

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutFeatureFlagResponse200 | PutFeatureFlagResponse400 | PutFeatureFlagResponse401 | PutFeatureFlagResponse403 | PutFeatureFlagResponse404 | PutFeatureFlagResponse422 | PutFeatureFlagResponse500
     """


    return (await asyncio_detailed(
        flag=flag,
client=client,
body=body,
exclude_nested=exclude_nested,

    )).parsed
