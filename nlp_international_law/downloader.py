import re
import pathlib
from bs4 import BeautifulSoup
from pdfminer.high_level import extract_text

from nlp_international_law.unspider import UNSpider
from nlp_international_law.keywords import keywords
from nlp_international_law.un_document import UNDocument


def parse_un_page(page_html):

    soup = BeautifulSoup(page_html, "html.parser")
    title_spans = soup.find_all("span", id=re.compile("cfTitle"))
    subject_spans = soup.find_all("span", id=re.compile("cfSubjs"))

    paper_list = []

    for t, s in (title_spans, subject_spans):

        paper = {"title": t.get_text(),
                 "subject": s.get_text(),
                 "files": []
        }

        detail_id = t["id"].replace("cfTitle", "details1")
        detail_div = soup.find("div", id=detail_id)
        if detail_div is None:
            continue

        detail_docs = detail_div.find_all("a", attrs={"class": "odsDoc"})

        for d in detail_docs:

            doc = {"url": d["href"]}

            lan_div = d.find_previous("span", attrs={"class": "odsTitle"})
            doc["lan"] = lan_div.get_text()

            sr = re.search(r"[a-zA-Z]+", d["title"])
            if not(sr is None):
                doc["format"] = sr[0]
            else:
                doc["format"] = "unknown"

            paper["files"].append(doc)

        paper_list.append(paper)

    return paper_list


def download_document_and_title(
    start_date, end_date, keyword, page_count=25, output_dir="./data/"
):

    s = UNSpider(start_date, end_date)
    s.init_cookies()

    out_dir = pathlib.Path("{}/{}/".format(output_dir, keyword))
    out_dir.mkdir(parents=True, exist_ok=True)

    docs = []

    print("searching first page")
    fp = s.init_search(keyword)
    dds = parse_un_page(fp)
    docs += dds
    print("search first page got {} results".format(len(dds)))

    for i in range(2, page_count + 1):
        print("searching page {}".format(i))
        p = s.get_search_page(i)
        dds = parse_un_page(p)
        print("search page {} got {} results".format(i, len(dds)))
        docs += dds

        if len(dds) != 20:
            break

    for d in docs:

        for f in d["files"]:

            if f["lan"] == "ENGLISH":

                sr = re.search(r"/\w+.\w+\?", f["url"])
                if not(sr is None):
                    file_name = sr[0][1:-1]
                else:
                    file_name = "unkownfile.bin"

                save_file_path = output_dir / file_name

                print("downloading from {}".format(f["url"]))
                r = s.download(f["url"])
                if r.status_code != 200:
                    print("download failed")
                else:
                    with open(str(save_file_path), "bw") as fp:
                        print(f"Path: {save_file_path}")
                        fp.write(r.content)

                content = extract_text(
                    str(save_file_path.with_suffix(".pdf"))
                )

                doc = UNDocument(
                    path_pdf=save_file_path,
                    title=d["title"],
                    year=start_date[:4],
                    subjects=d["subject"],
                    content=content
                )
                doc.save(out_dir)


if __name__ == "__main__":
    for keyword in keywords:
        for year in range(1945, 2020):
            print("\n\n ######   {}: YEAR is {}  ###### \n\n".format(keyword, year))
            start_date = "{}-01-01".format(year)
            end_date = "{}-12-31".format(year)
            download_document_and_title(start_date, end_date, keyword)
