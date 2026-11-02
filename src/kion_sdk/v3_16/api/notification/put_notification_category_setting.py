from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.notification_setting import NotificationSetting
from ...models.put_notification_category_setting_response_200 import PutNotificationCategorySettingResponse200
from ...models.put_notification_category_setting_response_400 import PutNotificationCategorySettingResponse400
from ...models.put_notification_category_setting_response_403 import PutNotificationCategorySettingResponse403
from ...models.put_notification_category_setting_response_404 import PutNotificationCategorySettingResponse404
from ...models.put_notification_category_setting_response_422 import PutNotificationCategorySettingResponse422
from ...models.put_notification_category_setting_response_500 import PutNotificationCategorySettingResponse500
from typing import cast



def _get_kwargs(
    category_id: int,
    notification_type: str,
    *,
    body: NotificationSetting,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v3/notification/setting/category/{category_id}/{notification_type}".format(category_id=quote(str(category_id), safe=""),notification_type=quote(str(notification_type), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PutNotificationCategorySettingResponse200 | PutNotificationCategorySettingResponse400 | PutNotificationCategorySettingResponse403 | PutNotificationCategorySettingResponse404 | PutNotificationCategorySettingResponse422 | PutNotificationCategorySettingResponse500 | None:
    if response.status_code == 200:
        response_200 = PutNotificationCategorySettingResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PutNotificationCategorySettingResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 403:
        response_403 = PutNotificationCategorySettingResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = PutNotificationCategorySettingResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PutNotificationCategorySettingResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PutNotificationCategorySettingResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PutNotificationCategorySettingResponse200 | PutNotificationCategorySettingResponse400 | PutNotificationCategorySettingResponse403 | PutNotificationCategorySettingResponse404 | PutNotificationCategorySettingResponse422 | PutNotificationCategorySettingResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    category_id: int,
    notification_type: str,
    *,
    client: AuthenticatedClient,
    body: NotificationSetting,

) -> Response[PutNotificationCategorySettingResponse200 | PutNotificationCategorySettingResponse400 | PutNotificationCategorySettingResponse403 | PutNotificationCategorySettingResponse404 | PutNotificationCategorySettingResponse422 | PutNotificationCategorySettingResponse500]:
    """ Updates the global notification setting for a given notification category to a given value.

    Args:
        category_id (int):
        notification_type (str):
        body (NotificationSetting): NotificationSetting represents the updated value of a
            notification category setting.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutNotificationCategorySettingResponse200 | PutNotificationCategorySettingResponse400 | PutNotificationCategorySettingResponse403 | PutNotificationCategorySettingResponse404 | PutNotificationCategorySettingResponse422 | PutNotificationCategorySettingResponse500]
     """


    kwargs = _get_kwargs(
        category_id=category_id,
notification_type=notification_type,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    category_id: int,
    notification_type: str,
    *,
    client: AuthenticatedClient,
    body: NotificationSetting,

) -> PutNotificationCategorySettingResponse200 | PutNotificationCategorySettingResponse400 | PutNotificationCategorySettingResponse403 | PutNotificationCategorySettingResponse404 | PutNotificationCategorySettingResponse422 | PutNotificationCategorySettingResponse500 | None:
    """ Updates the global notification setting for a given notification category to a given value.

    Args:
        category_id (int):
        notification_type (str):
        body (NotificationSetting): NotificationSetting represents the updated value of a
            notification category setting.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutNotificationCategorySettingResponse200 | PutNotificationCategorySettingResponse400 | PutNotificationCategorySettingResponse403 | PutNotificationCategorySettingResponse404 | PutNotificationCategorySettingResponse422 | PutNotificationCategorySettingResponse500
     """


    return sync_detailed(
        category_id=category_id,
notification_type=notification_type,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    category_id: int,
    notification_type: str,
    *,
    client: AuthenticatedClient,
    body: NotificationSetting,

) -> Response[PutNotificationCategorySettingResponse200 | PutNotificationCategorySettingResponse400 | PutNotificationCategorySettingResponse403 | PutNotificationCategorySettingResponse404 | PutNotificationCategorySettingResponse422 | PutNotificationCategorySettingResponse500]:
    """ Updates the global notification setting for a given notification category to a given value.

    Args:
        category_id (int):
        notification_type (str):
        body (NotificationSetting): NotificationSetting represents the updated value of a
            notification category setting.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutNotificationCategorySettingResponse200 | PutNotificationCategorySettingResponse400 | PutNotificationCategorySettingResponse403 | PutNotificationCategorySettingResponse404 | PutNotificationCategorySettingResponse422 | PutNotificationCategorySettingResponse500]
     """


    kwargs = _get_kwargs(
        category_id=category_id,
notification_type=notification_type,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    category_id: int,
    notification_type: str,
    *,
    client: AuthenticatedClient,
    body: NotificationSetting,

) -> PutNotificationCategorySettingResponse200 | PutNotificationCategorySettingResponse400 | PutNotificationCategorySettingResponse403 | PutNotificationCategorySettingResponse404 | PutNotificationCategorySettingResponse422 | PutNotificationCategorySettingResponse500 | None:
    """ Updates the global notification setting for a given notification category to a given value.

    Args:
        category_id (int):
        notification_type (str):
        body (NotificationSetting): NotificationSetting represents the updated value of a
            notification category setting.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutNotificationCategorySettingResponse200 | PutNotificationCategorySettingResponse400 | PutNotificationCategorySettingResponse403 | PutNotificationCategorySettingResponse404 | PutNotificationCategorySettingResponse422 | PutNotificationCategorySettingResponse500
     """


    return (await asyncio_detailed(
        category_id=category_id,
notification_type=notification_type,
client=client,
body=body,

    )).parsed
