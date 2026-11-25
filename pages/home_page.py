from core.base_page import BasePage
from config.settings import BASE_URL


class HomePage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        # ==========================
        # 메인홈 영역
        # ==========================

        self.CATEGORY = page.get_by_text(
            "카테고리쇼핑티켓테마관입점/판매 신청",
            exact=True
        )

        # ==========================
        # 검색 영역
        # ==========================

        self.SEARCH_BOX = page.get_by_role(
            "textbox", name="쿠팡 상품 검색", exact=True
        )

        self.SEARCH_BUTTON = page.get_by_role(
            "button", name="검색", exact=True
        )

        # ==========================
        # GNB 이동 버튼
        # ==========================

        self.GNB_LEFT_BTN = page.locator(
            ".gnb-menu-btn"
        ).first

        # GNB 우측 이동 버튼
        self.GNB_RIGHT_BTN = page.locator(
            ".gnb-menu-btn.gnb-menu-btn-right"
        ).first

        # ==========================
        # GNB 메뉴 영역
        # ==========================

        self.GNB_COUPANG_PLAY = page.get_by_role(
            "link", name="쿠팡플레이 쿠팡플레이", exact=True
        )

        self.GNB_ROCKET_DELIVERY = page.get_by_role(
            "link", name="로켓배송 로켓배송", exact=True
        )

        self.GNB_ROCKET_FRESH = page.get_by_role(
            "link", name="로켓프레시 로켓프레시", exact=True
        )

        self.GNB_CHRISTMAS = page.get_by_role(
            "link", name="크리스마스 크리스마스", exact=True
        )

        self.GNB_REPURCHASE = page.get_by_role(
            "link", name="다시 구매 다시 구매", exact=True
        )

        self.GNB_COUPANG_BIZ = page.get_by_role(
            "link", name="쿠팡비즈 쿠팡비즈", exact=True
        )

        self.GNB_ROCKET_DIRECT = page.get_by_role(
            "link", name="로켓직구 로켓직구", exact=True
        )

        self.GNB_GOLD_BOX = page.get_by_role(
            "link", name="골드박스 골드박스", exact=True
        )

        self.GNB_NEW_PRODUCT = page.get_by_role(
            "link", name="이달의신상 이달의신상", exact=True
        )

        # 카테고리 하위 메뉴 영역
        self.CATEGORY_FASHION = page.get_by_text(
            "패션의류/잡화", exact=True
        )

        self.CATEGORY_BEAUTY = page.get_by_text(
            "뷰티", exact=True
        )

        self.CATEGORY_BABY = page.get_by_text(
            "출산/유아동", exact=True
        )

        self.CATEGORY_FOOD = page.get_by_text(
            "식품", exact=True
        )

        self.CATEGORY_KITCHEN = page.get_by_text(
            "주방용품", exact=True
        )

        self.CATEGORY_LIFE = page.get_by_text(
            "생활용품", exact=True
        )

        self.CATEGORY_INTERIOR = page.get_by_text(
            "홈인테리어", exact=True
        )

        self.CATEGORY_DIGITAL = page.get_by_text(
            "가전디지털", exact=True
        )

        self.CATEGORY_SPORTS = page.get_by_text(
            "스포츠/레저", exact=True
        )

    # ==========================
    # 메인홈 기능
    # ==========================

    def open_home(self):
        self.open(BASE_URL)

    def verify_home(self):
        self.verify_visible(self.SEARCH_BOX)
        self.verify_visible(self.SEARCH_BUTTON)
        self.verify_visible(self.CATEGORY)

    # ==========================
    # 검색 기능
    # ==========================

    def search(self, keyword):
        self.input_text(self.SEARCH_BOX, keyword)
        self.click(self.SEARCH_BUTTON)

    def search_by_enter(self, keyword):
        self.input_text(self.SEARCH_BOX, keyword)
        self.press(self.SEARCH_BOX, "Enter")

    # ==========================
    # 카테고리 기능
    # ==========================

    def hover_category(self):
        self.hover(self.CATEGORY)

    def click_category(self):
        self.click(self.CATEGORY)

    # ==========================
    # GNB 기능
    # ==========================

    def click_gnb_left(self):
        self.click(self.GNB_LEFT_BTN)

    def click_gnb_right(self):
        self.click(self.GNB_RIGHT_BTN)

