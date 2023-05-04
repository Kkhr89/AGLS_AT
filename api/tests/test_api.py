""" API Test suite """
import pytest
import time

from api.commands.commands import *


class TestAPI:

    @pytest.mark.parametrize('filename', ['Avatar.png',
                                          'Аватар.png',
                                          'อวาตาร์.png',
                                          '阿瓦托爾.png',
                                          'PNG_910kB.png',
                                          'PNG_1960kB.png'])
    def test_upload_avatar(self, filename):
        access_token = BaseMethods.return_auth_token()
        url_upload = BaseMethods.parse_from_api_urls("url_post_upload_and_set_avatar")
        response = BaseMethods.post_request_to_upload_file(f'testdata/avatars/{filename}',
                                                           'avatar',
                                                           url_upload,
                                                           access_token)
        BaseMethods.assert_status_code(response, 200)
        BaseMethods.assert_str_in_json(response, 'file')
        BaseMethods.assert_str_in_json_2nd_lvl(response, 'file', 'fileSize')
        time.sleep(1)
