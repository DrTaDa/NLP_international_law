import requests
from requests_toolbelt import MultipartEncoder
from urllib.parse import urlencode
from bs4 import BeautifulSoup


class UNSpider:

    HOME_URL = "https://documents.un.org/prod/ods.nsf/home.xsp"
    INIT_SEARCH_URL = "https://documents.un.org/prod/ods.nsf/home.xsp"
    SEARCH_URL = "https://documents.un.org/prod/ods.nsf/xpSearchResultsE.xsp"
    ORIGIN_URL = "https://documents.un.org"
    HOST_URL = "documents.un.org"

    def __init__(self, start_date, end_date):

        self.start_date = start_date
        self.end_date = end_date

        self.view_id = None

        self.session = requests.session()

        self.url_post = self.SEARCH_URL + "?$$ajaxid=view%3A_id1%3A_id2%3" \
                                          "AcbMain%3AmainPanel"

        self.session.headers["user-agent"] = "Mozilla/5.0 (Macintosh; Intel " \
                                             "Mac OS X 10_15_4) AppleWebKit/" \
                                             "537.36 (KHTML, like Gecko) Chr" \
                                             "ome/81.0.4044.138 Safari/537.36"
        self.session.headers["Accept"] = "text/html,application/xhtml+xml,app" \
                                         "lication/xml;q=0.9,image/webp,image" \
                                         "/apng,*/*;q=0.8,application/signed-" \
                                         "exchange;v=b3;q=0.9"
        self.session.headers["Accept-Encoding"] = "gzip, deflate, br"
        self.session.headers["Accept-Language"] = "zh-CN,zh;q=0.9,en;q=0.8"
        self.session.headers["Referer"] = self.INIT_SEARCH_URL
        self.session.headers["Host"] = self.HOST_URL
        self.session.headers["Origin"] = self.ORIGIN_URL
        self.session.headers["Sec-Fetch-Dest"] = "document"
        self.session.headers["Sec-Fetch-Mode"] = "navigate"
        self.session.headers["Sec-Fetch-Site"] = "same-origin"
        self.session.headers["Sec-Fetch-User"] = "?1"
        self.session.headers["Upgrade-Insecure-Requests"] = "1"
        self.session.headers["Cache-Control"] = "max-age=0"
        self.session.headers["Sec-Fetch-Dest"] = "empty"
        self.session.headers["Sec-Fetch-Mode"] = "cors"
        self.session.headers["Sec-Fetch-Site"] = "same-origin"
        self.session.headers["X-Requested-With"] = "XMLHttpRequest"

        self.download_headers = {
            "Host": "documents-dds-ny.un.org",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
        }

        self.form_fields = {
            "view:_id1:_id2:txtSymbol": "",
            "view:_id1:_id2:rgTrunc": "R",
            "view:_id1:_id2:txtWrds": "",
            "view:_id1:_id2:txtSubj": "",
            "view:_id1:_id2:dtPubDateFrom": self.start_date,
            "view:_id1:_id2:dtPubDateTo": self.end_date,
            "view:_id1:_id2:dtRelDateFrom": "",
            "view:_id1:_id2:dtRelDateTo": "",
            "view:_id1:_id2:txtJobNo": "",
            "view:_id1:_id2:txtSess": "",
            "view:_id1:_id2:txtAgItem": "",
            "view:_id1:_id2:cbType": "FP",
            "view:_id1:_id2:cbSort": "R",
            "view:_id1:_id2:hdnSubj": "",
            "$$xspsubmitid": "view:_id1:_id2:_id130",
            "$$xspexecid": "",
            "$$xspsubmitvalue": "",
            "$$xspsubmitscroll": "0|469",
            "view:_id1": "view:_id1",
        }

    def init_cookies(self):

        r = self.session.get(self.HOME_URL, verify=False)

        if r.status_code != 200:
            print("status_code != 200: coudn't reach home page !")
            return

        soup = BeautifulSoup(r.content, "html.parser")
        view_id_input = soup.find_all("input", attrs={"name": "$$viewid"})
        self.view_id = view_id_input[0].attrs["value"]

        print("first viewid: " + self.view_id)

    def init_search(self, keyword):

        self.form_fields["$$viewid"] = self.view_id
        self.form_fields["view:_id1:_id2:txtFTSrch"] = keyword

        m = MultipartEncoder(fields=self.form_fields)

        r = self.session.post(
            self.INIT_SEARCH_URL,
            data=m,
            headers={"Content-Type": m.content_type},
            verify=False,
        )
        print(r.status_code)

        if r.status_code == 200:
            print("init search success")
            soup = BeautifulSoup(r.content, "html.parser")
            view_id_input = soup.find_all("input", attrs={"name": "$$viewid"})
            self.view_id = view_id_input[0].attrs["value"]
            self.form_fields["$$viewid"] = self.view_id
            print("new viewid: " + self.view_id)

        return str(r.content, encoding="utf-8")

    def get_search_page(self, page_no):

        self.form_fields["$$xspsubmitid"] = "view:_id1:_id2:cbMain:_id135:" \
                                            "pager1__Group__lnk__{}" \
                                            "".format(page_no - 1)
        self.form_fields["$$xspexecid"] = "view:_id1:_id2:cbMain:_id135:pager1"
        self.form_fields["$$xspsubmitscroll"] = "0|334"
        self.form_fields["view:_id1:_id2:cbLang"] = ""

        data = urlencode(self.form_fields)
        data = data.replace("%21", "!")

        r = self.session.post(
            url=self.url_post,
            data=data,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            verify=False,
        )

        if r.status_code == 200:
            print("search page success")
        else:
            print("search page failed, status code {}".format(r.status_code))

        return str(r.content, encoding="utf-8")

    def download(self, doc_link):

        return self.session.get(
            doc_link, headers=self.download_headers, verify=False
        )
