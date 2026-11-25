import pytest
import re

from pages.home_page import HomePage
from playwright.sync_api import expect

class TestHome:

    @pytest.mark.smoke
    def test_home_0001(self, page):
        """TC 001 - 메인홈 정상 노출 확인"""

        home = HomePage(page)

        # Step 1. 쿠팡 메인홈 접속
        home.open_home()

        page.wait_for_timeout(2000)

        # Expected Result
        home.verify_visible(home.SEARCH_BOX)

    @pytest.mark.smoke
    def test_home_0002(self, page):
        """TC 0002 - 메인홈 GNB 영역 노출 확인"""

        home = HomePage(page)

        # Step 1. 쿠팡 메인홈 접속
        home.open_home()

        page.wait_for_timeout(2000)

        # Step 2. GNB 영역 확인
        home.verify_visible(home.GNB_COUPANG_PLAY)
        home.verify_visible(home.GNB_ROCKET_DELIVERY)
        home.verify_visible(home.GNB_ROCKET_FRESH)
        home.verify_visible(home.GNB_CHRISTMAS)
        home.verify_visible(home.GNB_REPURCHASE)
        home.verify_visible(home.GNB_COUPANG_BIZ)
        home.verify_visible(home.GNB_ROCKET_DIRECT)
        home.verify_visible(home.GNB_GOLD_BOX)

    @pytest.mark.smoke
    def test_home_0003(self, page):
        """TC 0003 - GNB 좌우 이동 및 원상복귀 확인"""

        home = HomePage(page)

        # Step 1. 쿠팡 메인홈 접속
        home.open_home()
        page.wait_for_timeout(2000)

        # Step 2. 초기 GNB 메뉴 노출 확인
        home.verify_visible(home.GNB_COUPANG_PLAY)
        home.verify_visible(home.GNB_RIGHT_BTN)

        # Step 3. GNB 우측 이동 버튼 클릭
        home.click_gnb_right()
        page.wait_for_timeout(2000)

        # Step 4. 이달의신상 객체 노출 확인
        home.verify_visible(home.GNB_NEW_PRODUCT)

        # Step 5. GNB 좌측 이동 버튼 노출 확인
        home.verify_visible(home.GNB_LEFT_BTN)

        # Step 6. GNB 좌측 이동 버튼 클릭
        home.click_gnb_left()
        page.wait_for_timeout(2000)

        # Step 7. 초기 GNB 메뉴 원상복귀 확인
        home.verify_visible(home.GNB_COUPANG_PLAY)
        home.verify_visible(home.GNB_ROCKET_DELIVERY)
        home.verify_visible(home.GNB_ROCKET_FRESH)
        home.verify_visible(home.GNB_RIGHT_BTN)

        page.wait_for_timeout(2000)

    @pytest.mark.smoke
    def test_home_0004(self, page):
        """TC 0004 - GNB 쿠팡플레이 페이지 랜딩 확인"""

        home = HomePage(page)

        # Step 1. 쿠팡 메인홈 접속
        home.open_home()
        page.wait_for_timeout(2000)

        # Step 2. 쿠팡플레이 객체 노출 확인
        home.verify_visible(home.GNB_COUPANG_PLAY)

        # Step 3. 쿠팡플레이 클릭 및 새 탭 감지
        with page.expect_popup() as popup_info:
            home.click(home.GNB_COUPANG_PLAY)

        popup = popup_info.value

        # Step 4. 랜딩 페이지 로딩 대기
        popup.wait_for_load_state("domcontentloaded")

        # Step 5. 쿠팡플레이 랜딩 URL 검증
        expect(popup).to_have_url(
            re.compile(r"^https://(?:www\.)?coupangplay\.com(?:/|$)"),
            timeout=15000
        )

        print(f"[PASS] 랜딩 URL: {popup.url}")

        popup.wait_for_timeout(3000)

        # Step 6. 새 탭 종료
        popup.close()

        # Step 7. 기존 쿠팡 메인홈 유지 확인
        home.verify_visible(home.GNB_COUPANG_PLAY)

    @pytest.mark.smoke
    def test_home_0005(self, page):
        """TC 0005 - 메인홈 새로고침 후 객체 정상 노출 확인"""

        home = HomePage(page)

        # Step 1. 쿠팡 메인홈 접속
        home.open_home()
        page.wait_for_timeout(2000)

        # Step 2. 새로고침 전 주요 객체 노출 확인
        home.verify_visible(home.CATEGORY)
        home.verify_visible(home.SEARCH_BOX)
        home.verify_visible(home.SEARCH_BUTTON)
        home.verify_visible(home.GNB_COUPANG_PLAY)

        # Step 3. 메인홈 새로고침
        home.refresh()
        page.wait_for_timeout(2000)

        # Step 4. 새로고침 후 주요 객체 정상 노출 확인
        home.verify_visible(home.CATEGORY)
        home.verify_visible(home.SEARCH_BOX)
        home.verify_visible(home.SEARCH_BUTTON)
        home.verify_visible(home.GNB_COUPANG_PLAY)

        page.wait_for_timeout(2000)

    @pytest.mark.smoke
    def test_home_0006(self, page):
        """TC 0006 - 카테고리 Hover 시 하위 메뉴 정상 노출 확인"""

        home = HomePage(page)

        # Step 1. 쿠팡 메인홈 접속
        home.open_home()
        page.wait_for_timeout(2000)

        # Step 2. 카테고리 버튼 노출 확인
        home.verify_visible(home.CATEGORY)

        # Step 3. 카테고리 버튼 Hover (현재 쿠팡 자동화 브라우저로 진입상태에서는 카테고리 호버시 카테고리 목록이 노출안되고있음)
        home.hover_category()
        page.wait_for_timeout(2000)

        # Step 4. 하위 카테고리 항목 정상 노출 확인
        home.verify_visible(home.CATEGORY_FASHION)
        home.verify_visible(home.CATEGORY_BEAUTY)
        home.verify_visible(home.CATEGORY_BABY)
        home.verify_visible(home.CATEGORY_FOOD)

    @pytest.mark.smoke
    def test_home_0007(self, page):
        """TC 0007 - 검색창 한글 및 영문 입력 확인"""

        home = HomePage(page)

        # Step 1. 메인홈 접속
        home.open_home()
        page.wait_for_timeout(2000)

        # Step 2. 검색창 클릭
        home.click(home.SEARCH_BOX)

        # Step 3. 테스트 데이터 정의
        keywords = ["키보드", "abc", "123", "!@#"]

        # Step 4. 문자열 입력 및 검증
        for keyword in keywords:
            home.input_text(home.SEARCH_BOX, keyword)
            page.wait_for_timeout(2000)

            expect(home.SEARCH_BOX).to_have_value(keyword)

            print(f"[PASS] 검색어 입력 확인: {keyword}")

    @pytest.mark.smoke
    def test_home_0008(self, page):
        """TC 0008 - 키보드 검색 및 검색 결과 노출 확인"""

        home = HomePage(page)

        # Step 1. 메인홈 접속
        home.open_home()
        page.wait_for_timeout(2000)

        # Step 2. 검색창 클릭 및 검색어 입력
        home.click(home.SEARCH_BOX)
        home.input_text(home.SEARCH_BOX, "키보드")

        # Step 3. 입력값 검증
        expect(home.SEARCH_BOX).to_have_value("키보드")

        # Step 4. 검색 버튼 클릭
        home.click(home.SEARCH_BUTTON)
        page.wait_for_timeout(2000)

        # Step 5. 검색 결과 페이지 랜딩 확인
        expect(page).to_have_url(
            re.compile(r"/search")
        )

        # Step 6. 검색 결과 텍스트 OR 조건 검증
        result = page.get_by_text(
            re.compile(r"에이수스|앱코")
        ).filter(visible=True)

        expect(result.first).to_be_visible(timeout=10000)

        print("[PASS] 에이수스 또는 앱코 검색 결과 정상 노출")

