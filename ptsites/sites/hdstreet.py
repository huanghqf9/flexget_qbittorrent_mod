from ..schema.site_base import SiteBase
from ..schema.nexusphp import NexusPHP

# auto_sign_in
URL = 'https://hdstreet.club/bakatest.php'
SUCCEED_REGEX = '连续\\d+天签到,获得\\d+点魔力值|今天已经签过到了\\(已连续\\d+天签到\\)'
WRONG_REGEX = '回答错误,失去 1 魔力值,这道题还会再考一次'


class MainClass(NexusPHP):
    @staticmethod
    def build_sign_in(entry, config):
        SiteBase.build_sign_in_entry(entry, config, URL, SUCCEED_REGEX, wrong_regex=WRONG_REGEX)

    def sign_in(self, entry, config):
        self.sign_in_by_question(entry, config)

    def build_selector(self):
        selector = super(MainClass, self).build_selector()
        selector['details']['hr'] = None
        return selector
