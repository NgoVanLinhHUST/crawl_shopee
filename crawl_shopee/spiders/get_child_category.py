import scrapy
from scrapy_splash import SplashRequest
from bs4 import BeautifulSoup
import json

class GetChildCategorySpider(scrapy.Spider):
    name = "get_child_category"
    # allowed_domains = ["shopee.vn"]
    # start_urls = ["https://shopee.vn"]

    custom_headers = {
    'authority': 'shopee.vn',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'cookie': 'csrftoken=4DzG54tBXPFxFqRjRFLnfhvoPHy58EJn; _gcl_aw=GCL.1700150893.EAIaIQobChMIrdX3zvPIggMVfM5MAh1nLQIWEAAYASAAEgIo0vD_BwE; _gcl_au=1.1.392599059.1700150893; _med=cpc; SPC_T_IV=SnBhZ3RCdnc0c0RSQ2dsVw==; SPC_F=bukiQR2J7rJngiGX2PaH0CkA5xCXZKUA; REC_T_ID=57fe7838-849a-11ee-b364-5aa27d49e790; SPC_R_T_ID=YJ6MbAOydYg645wB2Vt4swESEIBff95EgKeyL7cl03u99TgJaXdRlTsHAjzWQpmUaZ4TdtRl+8S7abXrBrSvaru3Igw75RbqOe9880jTafC7cTtKU5KnwBO8PI9/jBXfmHSB0mRw/pc5VJ+R3Ydt/IvJ3uyyjrw7ncKqs0aMD9A=; SPC_R_T_IV=SnBhZ3RCdnc0c0RSQ2dsVw==; SPC_T_ID=YJ6MbAOydYg645wB2Vt4swESEIBff95EgKeyL7cl03u99TgJaXdRlTsHAjzWQpmUaZ4TdtRl+8S7abXrBrSvaru3Igw75RbqOe9880jTafC7cTtKU5KnwBO8PI9/jBXfmHSB0mRw/pc5VJ+R3Ydt/IvJ3uyyjrw7ncKqs0aMD9A=; _fbp=fb.1.1700150893876.1657694390; _hjSessionUser_868286=eyJpZCI6IjI1MDNiNmU3LTNiNmMtNWJiZS1hNjFhLWY2ZGUxMzM1OTMzNyIsImNyZWF0ZWQiOjE3MDAxNTA5MDA5MjgsImV4aXN0aW5nIjp0cnVlfQ==; SPC_SI=WUdTZQAAAAByd0RpTFZQN2FAIwAAAAAAWUZFVW9iaVI=; _gid=GA1.2.1748307311.1700240533; _QPWSDCXHZQA=e62bf0b7-11f9-4bbe-d2c9-63b2757d5bfe; REC7iLP4Q=cd2801c5-9728-40c3-9710-ff9588ec71b2; _hjAbsoluteSessionInProgress=0; _hjIncludedInSessionSample_868286=0; _hjSession_868286=eyJpZCI6ImY5YzkzYmNhLWMxMzUtNDJkNi05MWRlLTNkODc5NDJhNTNjYSIsImNyZWF0ZWQiOjE3MDAzMjAyOTg4NTAsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6dHJ1ZX0=; AMP_TOKEN=%24NOT_FOUND; SPC_SEC_SI=v1-cXV1UHRKSlVPMG1ZZFhOTfmv/W28oQrueqZWlnpMqcUh5GORC4Dzkqt8+IOVhmcqRFNL22V7rSvkAqpBHV99j/h7RhR+mT6H4vzRiF7R5rQ=; shopee_webUnique_ccd=psnW5cVZmrcgKuEpIRqcFQ%3D%3D%7CSLOErpanekVbZrcxK7XrgsAU9%2FD6RjHs%2BlwmVVt9tczWv%2FhRiVijMt16IJlUnoLlB3cWiHCbNL0%3D%7CiYdFMxoeUo%2BfAmYn%7C08%7C3; ds=a5e7da06e5748046cf57dbb2f46e0b5f; _ga=GA1.1.1186821245.1700150897; _dc_gtm_UA-61914164-6=1; _ga_M32T05RVZT=GS1.1.1700319376.4.1.1700325156.50.0.0; SPC_R_T_ID=YJ6MbAOydYg645wB2Vt4swESEIBff95EgKeyL7cl03u99TgJaXdRlTsHAjzWQpmUaZ4TdtRl+8S7abXrBrSvaru3Igw75RbqOe9880jTafC7cTtKU5KnwBO8PI9/jBXfmHSB0mRw/pc5VJ+R3Ydt/IvJ3uyyjrw7ncKqs0aMD9A=; SPC_R_T_IV=SnBhZ3RCdnc0c0RSQ2dsVw==; SPC_SEC_SI=v1-TGh6V2prSWVZSmdyZzliYkx29vPaPyPV/+nzzD1E0ZJ8wijdmUYBpdyNI7uGWyK2NdY92+/3Wf6NQmrd0ugw57F+e7ZZMM371N3SJc9yqqw=; SPC_SI=WUdTZQAAAAByd0RpTFZQN2FAIwAAAAAAWUZFVW9iaVI=; SPC_T_ID=YJ6MbAOydYg645wB2Vt4swESEIBff95EgKeyL7cl03u99TgJaXdRlTsHAjzWQpmUaZ4TdtRl+8S7abXrBrSvaru3Igw75RbqOe9880jTafC7cTtKU5KnwBO8PI9/jBXfmHSB0mRw/pc5VJ+R3Ydt/IvJ3uyyjrw7ncKqs0aMD9A=; SPC_T_IV=SnBhZ3RCdnc0c0RSQ2dsVw==',
    'if-none-match-': '55b03-158a0f98f80a09649f8dcfd2f8d263d4',
    'referer': 'https://shopee.vn/',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'x-api-source': 'pc',
    'x-requested-with': 'XMLHttpRequest',
    'x-sap-ri': '27e75865471ca69979696a3e01012a3c2814c022756171f1b979',
    'x-sap-sec': '3Asja8mS0xcHLxcHK/c5LxJHK/cHLxJHLxcELxcHYxMHLCFSLxcpLxcHwj1fTEmHLxcXLvcHBxMHLy0qc/HrxsZBxFEJ7Eq5lgfLtjLAK/JgKMktaKq/iD5tFPrDJxYnzByB0z2PDANaIMoYEZcw+UO8lCiFKg8ZWNnPVGnroh8OzUMZB/e4kXQcnfzUYuJC/neTFGmN6lassSxkWvYr60VvdEoVrSu8pPCLJY2S9DKoX8NcIfatC8gFfPcgRCTrEhHtIyrl0frt+ZFwIDX/OR2tys6d37eSxgbf2ZN9WwnwSjbhnI1WVlBZE5vUGZTMsKRSx5xU6fJrOI7T2BD3TyeAhnvHxuLU1pucKWAsSTgLXV88v7AED/eARqVxlFYk0cW+4VtXHbkROcjerx13SMNkqp97FWaKG+Wa/DvfDaa6GCTYZmbOHZafVyDkjl1Ie1je1CjtVC9G+okXEeJ5LxcHObJzPHgyPHJHLxcHqjqfTEmHLxcNLxcH/xcHLaTvHT8AqD4SBJhCB522JFe3p2ZB2xcHLbJxc6OUQoJaLxcHLxmH0xc5LxJH2xcHLxmHLxcNLxcH/xcHLb/nNpBZemZ1iuxVOjiIBgbBfJOM2xcHLb/qPoeCQb3ZLxcHLC==',
    'x-shopee-language': 'vi'
    }
    def get_url(self, name, itemid, shopid):
        name = name.replace(" ", "-").replace(",", "").replace("/","-")
        url = f"shopee.vn/{name}-i.{shopid}.{itemid}"
        return url
    

    def start_requests(self):
        yield scrapy.Request(url = f"https://shopee.vn/api/v4/pages/get_category_tree", callback=self.parse, headers=self.custom_headers)
    
    def parse(self, response):
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        text_content = soup.get_text()
        data_api = json.loads(text_content)
        # handle field
        parent_catids_of_childs = [child["parent_catid"] for entry in data_api["data"]["category_list"] for child in entry.get("children", [])]
        cat_ids = [child["catid"] for entry in data_api["data"]["category_list"] for child in entry.get("children", [])]
        display_names = [child["display_name"] for entry in data_api["data"]["category_list"] for child in entry.get("children", [])]    
        parent_catids = [entry["catid"] for entry in data_api["data"]["category_list"]]
        display_parent_names = [entry["display_name"] for entry in data_api["data"]["category_list"]]
        lst_output = []
        lst_cate_output = []
        for parent_catid, display_parent_name in zip(parent_catids, display_parent_names):   
            output = {'parent_catid':parent_catid,'display_parent_name':display_parent_name  }
            lst_output.append(output)
            cate_output = {'parent_catids_of_child': '', 'cat_id': parent_catid, 'display_name': display_parent_names,'display_parent_name':display_parent_name }
            # lst_cate_output.append(cate_output)

        for parent_catids_of_child, cat_id, display_name in zip(parent_catids_of_childs, cat_ids, display_names):
            output_child = {'parent_catids_of_child': parent_catids_of_child, 'cat_id': cat_id, 'display_name': display_name}
            # Find the matching entry in lst_output
            matching_entry = next((entry for entry in lst_output if entry['parent_catid'] == parent_catids_of_child), None)
            # If a matching entry is found, update output_child with the display_parent_name
            if matching_entry:
                output_child['display_parent_name'] = matching_entry['display_parent_name']
            else:
                output_child['display_parent_name'] = None  # Set to None if no match is found
            lst_cate_output.append(output_child)
            # yield output_child
        # print(lst_cate_output)
        lst_offsets = [0, 60, 120, 180, 240, 300, 360, 420, 480]
        for lst_offset in lst_offsets:
            for entry in lst_cate_output:
                parent_catids_of_child = entry["parent_catids_of_child"]
                catid = entry["cat_id"]
                display_name = entry["display_name"]
                display_parent_name = entry["display_parent_name"]
                print(f"https://shopee.vn/api/v4/recommend/recommend?bundle=category_landing_page&cat_level=1&catid={catid}&limit=60&offset={lst_offset}")
                yield scrapy.Request(url = f"https://shopee.vn/api/v4/recommend/recommend?bundle=category_landing_page&cat_level=1&catid={catid}&limit=60&offset={lst_offset}", callback=self.parse_info, headers=self.custom_headers, cb_kwargs={'display_name':display_name, 'display_parent_name':display_parent_name})

    def parse_info(self, response, display_name, display_parent_name):
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        text_content = soup.get_text()
        data_api = json.loads(text_content)
        # print(data)
        itemids = [
            item["itemid"]
            for section in data_api["data"]["sections"]
            for item in section["data"]["item"]
        ]
        shopids = [
            item["shopid"]
            for section in data_api["data"]["sections"]
            for item in section["data"]["item"]
        ]
        nameprods = [
            item["name"]
            for section in data_api["data"]["sections"]
            for item in section["data"]["item"]
        ]
        prices = [
            item["price"]
            for section in data_api["data"]["sections"]
            for item in section["data"]["item"]
        ]
        historicalSolds = [
            item["historical_sold"]
            for section in data_api["data"]["sections"]
            for item in section["data"]["item"]
        ]

        ratingStars = [
            item["item_rating"]["rating_star"]
            for section in data_api["data"]["sections"]
            for item in section["data"]["item"]
        ]
        for itemid, shopid, nameprod, price, historicalSold, ratingStar in zip(itemids, shopids, nameprods, prices, historicalSolds, ratingStars):
            price = price / 100000 # clean giá 
            url = self.get_url(nameprod, itemid, shopid)
            output = {'display_parent_name':display_parent_name,
                      'display_name':display_name,
                      'name': nameprod,
                      'url':url,
                      'ratingStar':ratingStar,
                      'price': price,
                      'revenue': historicalSold*price}
            yield output


