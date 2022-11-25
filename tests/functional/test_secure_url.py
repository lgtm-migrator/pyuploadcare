import pytest

from pyuploadcare import Uploadcare
from pyuploadcare.secure_url import AkamaiSecureUrlBuilder


known_secret = (
    "73636b61519adede42191efe1e73f02a67c7b692e3765f90c250c230be095211"
)


@pytest.mark.freeze_time("2021-10-12")
def test_generate_secure_url():
    secure_url_bulder = AkamaiSecureUrlBuilder(
        "cdn.yourdomain.com", known_secret
    )
    secure_url = secure_url_bulder.build(
        "52da3bfc-7cd8-4861-8b05-126fef7a6994"
    )
    assert secure_url == (
        "https://cdn.yourdomain.com/52da3bfc-7cd8-4861-8b05-126fef7a6994/?token="
        "exp=1633997100~"
        "acl=/52da3bfc-7cd8-4861-8b05-126fef7a6994/~"
        "hmac=81852547d9dbd9eefd24bee2cada6eab02244b9013533bc8511511923098df72"
    )


@pytest.mark.freeze_time("2021-10-12")
def test_generate_secure_url_with_transformation():
    secure_url_bulder = AkamaiSecureUrlBuilder(
        "cdn.yourdomain.com", known_secret
    )
    secure_url = secure_url_bulder.build(
        "52da3bfc-7cd8-4861-8b05-126fef7a6994/-/resize/640x/other/transformations/"
    )
    assert secure_url == (
        "https://cdn.yourdomain.com/52da3bfc-7cd8-4861-8b05-126fef7a6994/"
        "-/resize/640x/other/transformations/?token="
        "exp=1633997100~"
        "acl=/52da3bfc-7cd8-4861-8b05-126fef7a6994/-/resize/640x/other/transformations/~"
        "hmac=a3ae2b3e3adfcb5d41ca753598e19d17264ac87d2b0b828ccdac5136e63f2f1a"
    )


@pytest.mark.freeze_time("2021-10-12")
def test_client_generate_secure_url():
    secure_url_bulder = AkamaiSecureUrlBuilder(
        "cdn.yourdomain.com", known_secret
    )

    uploadcare = Uploadcare(
        public_key="public",
        secret_key="secret",
        secure_url_builder=secure_url_bulder,
    )
    secure_url = uploadcare.generate_secure_url(
        "52da3bfc-7cd8-4861-8b05-126fef7a6994"
    )
    assert secure_url == (
        "https://cdn.yourdomain.com/52da3bfc-7cd8-4861-8b05-126fef7a6994/?token="
        "exp=1633997100~"
        "acl=/52da3bfc-7cd8-4861-8b05-126fef7a6994/~"
        "hmac=81852547d9dbd9eefd24bee2cada6eab02244b9013533bc8511511923098df72"
    )
