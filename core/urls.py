from django.urls import path, include, re_path
from . import views, api_views

app_name = "core"
urlpatterns = [
    path("", views.ProductCreateView.as_view(), name="product_create_view"),
    re_path(
        r"^dashboard/(?P<token>[0-9a-f-]+)$",
        views.ProductSellerView.as_view(),
        name="product_info_seller",
    ),
    re_path(
        r"^dashboard/email_updates$",
        views.ProductEmailUpdatesView.as_view(),
        name="product_seller_email_updates",
    ),
    re_path(
        r"^product/(?P<uid>[0-9a-f-]+)/$",
        views.ProductPublicView.as_view(),
        name="product_info_buyer",
    ),
    re_path(
        r"^checkout/(?P<order_id>\w+)$",
        views.IntializePayment.as_view(),
        name="product_pay_buyer",
    ),
    re_path(
        r"^payment_processed/$",
        views.PaymentConfirmCallbackView.as_view(),
        name="payment_processed_buyer",
    ),
    re_path(
        r"^payment/(?P<order_id>\w+)/$",
        views.PaymentStatusView.as_view(),
        name="payment_info_buyer",
    ),
    re_path(
        r"^(?P<order_id>\w+)/download/$",
        views.DownloadFiles.as_view(),
        name="product_download_buyer",
    ),
    path(
        "update/payments",
        views.UpdatePaymentStatusCallback.as_view(),
        name="payment_status_update",
    ),

    ## API URLs Start ##

    path(
        "api/product",
        api_views.ProductCreateAPIView.as_view(),
        name="api_product_create_view",
    ),
    path(
        "api/email_updates",
        api_views.EmailUpdateAPIView.as_view(),
        name="api_product_seller_email_updates",
    ),
]
