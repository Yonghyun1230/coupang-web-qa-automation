# Coupang Web QA Automation Framework

## 1. Project Overview

쿠팡 웹 서비스를 대상으로 Python, Playwright, Pytest 기반의 웹 UI 자동화 프레임워크를 설계하고 구축한 개인 QA 포트폴리오 프로젝트입니다.

기존 Appium 기반 모바일 QA 자동화 실무 경험을 바탕으로 웹 UI 자동화 영역까지 기술 역량을 확장하고자 진행하였습니다.

Page Object Model(POM) 설계 패턴을 적용하여 테스트 로직과 객체 관리 영역을 분리하고, 공통 제어 모듈을 구현하여 코드의 재사용성, 확장성 및 유지보수성을 고려하였습니다.

## 2. Tech Stack

| Category | Technology |
|---|---|
| Language | Python 3.12.10 |
| Automation Tool | Playwright |
| Test Framework | Pytest |
| Design Pattern | Page Object Model (POM) |
| Reporting | Pytest HTML |
| Browser | Chromium |
| IDE | PyCharm |
| Version Control | Git / GitHub |
| OS | Windows |

## 3. Key Features

- Page Object Model 기반 자동화 프레임워크 설계
- 공통 객체 탐색 및 제어 모듈 구현
- Role, CSS Selector 기반 Locator 관리
- Click, Hover, Scroll, Input 등 사용자 인터랙션 자동화
- Assertion 기반 테스트 결과 자동 판정
- 정규표현식을 활용한 텍스트 및 URL 검증
- 데이터 기반 입력값 검증
- TC ID 기반 테스트 스크립트 관리
- Pytest Fixture 기반 테스트 환경 관리
- HTML 테스트 결과 리포트 자동 생성

## 4. Framework Architecture

| Layer | Description |
|---|---|
| Test Runner | 전체 테스트 실행 및 결과 리포트 생성 |
| Test Script Layer | TC별 테스트 절차 및 예상 결과 검증 |
| Page Object Layer | 페이지별 Locator 및 기능 관리 |
| Core Layer | 공통 객체 탐색, 제어 및 검증 기능 |
| Playwright Engine | 브라우저 제어 및 웹 UI 자동화 |
| Target Application | Coupang Web Service |

각 계층의 역할을 분리하여 테스트 스크립트 간 중복 코드를 최소화하고, UI 변경 발생 시 유지보수 범위를 줄이도록 설계하였습니다.

## 5. Project Structure

```
coupang_automation/
├── config/
│   └── settings.py
├── core/
│   └── base_page.py
├── pages/
│   ├── home_page.py
│   └── search_page.py
├── tests/
│   ├── test_home.py
│   └── test_search.py
├── docs/
├── reports/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── run.py
├── .gitignore
└── README.md
```

| Directory / File | Description |
|---|---|
| config | 테스트 환경 및 공통 설정 관리 |
| core | 공통 자동화 제어 모듈 |
| pages | 페이지별 Locator 및 기능 정의 |
| tests | 테스트케이스 기반 자동화 스크립트 |
| docs | 포트폴리오 및 테스트 관련 문서 |
| reports | 자동화 테스트 수행 결과 |
| conftest.py | Fixture 및 테스트 환경 관리 |
| pytest.ini | Pytest 실행 설정 |
| run.py | 통합 테스트 실행 모듈 |
| requirements.txt | 프로젝트 라이브러리 의존성 관리 |

## 6. Test Coverage

| TC ID | Test Scenario |
|---|---|
| TC 0001 | 메인홈 주요 UI 정상 노출 검증 |
| TC 0002 | GNB 메뉴 정상 노출 검증 |
| TC 0003 | GNB 좌우 이동 및 원상복귀 검증 |
| TC 0004 | 쿠팡플레이 페이지 랜딩 검증 |
| TC 0005 | 새로고침 후 메인홈 UI 정상 노출 검증 |
| TC 0006 | 카테고리 Hover 시 하위 메뉴 노출 검증 |
| TC 0007 | 한글, 영문, 숫자, 특수문자 입력 검증 |
| TC 0008 | 상품 검색 및 검색 결과 검증 |

## 7. Test Execution Result

**Execution Date: 2026.11.26**

| Metric | Result |
|---|---|
| Total Test Cases | 8 |
| Passed | 5 |
| Failed | 3 |
| Skipped | 0 |
| Pass Rate | 62.5% |
| Execution Time | 72 seconds |

### Failure Analysis

일부 자동화 테스트 수행 과정에서 Access Denied 현상이 발생하였습니다.

쿠팡 측 보안 정책에 의해 자동화 브라우저의 접근이 제한되어 테스트가 실패한 것으로 추정됩니다.

다만 정확한 차단 정책 및 개별 테스트의 실패 원인은 확인되지 않았으므로, 서비스 자체의 기능 결함과 구분하여 테스트 환경 제약사항으로 관리하였습니다.

## 8. Troubleshooting

### 8.1 Locator 자료형 불일치

기존 공통 객체 탐색 모듈에서 문자열 기반 Selector와 Playwright Locator 객체 간 자료형 불일치 문제가 발생하였습니다.

isinstance()를 활용한 자료형 분기 처리를 적용하여 두 가지 객체 탐색 방식을 모두 지원하도록 개선하였습니다.

### 8.2 Pytest 테스트 탐색 오류

테스트 파일 명명 규칙 및 모듈 Import 경로 문제로 인해 테스트 스크립트가 정상적으로 탐색되지 않는 문제가 발생하였습니다.

Pytest의 테스트 탐색 규칙에 맞게 파일명을 수정하고 모듈 경로를 정리하여 해결하였습니다.

### 8.3 외부 서비스 접근 제한

자동화 브라우저를 통한 서비스 접근 과정에서 Access Denied 현상이 발생하였습니다.

해당 현상을 서비스 기능 결함으로 단정하지 않고 테스트 환경 제약사항으로 분류하였습니다.

## 9. Learning & Experience

기존 실무에서는 Appium과 Python을 활용한 모바일 UI 자동화 업무를 수행하였으며, XPath 기반 Locator를 주로 사용하였습니다.

이번 프로젝트에서는 Playwright의 Role 기반 Locator, CSS Selector, Inspector 및 브라우저 제어 방식을 새롭게 학습하였습니다.

모바일 자동화와 웹 자동화는 사용하는 도구와 객체 탐색 방식에 차이가 있었지만, 테스트 절차 설계, 객체 제어, 예상 결과 검증 등 자동화의 핵심 원리는 유사하였습니다.

기존 실무 경험을 바탕으로 새로운 자동화 도구에도 빠르게 적응할 수 있음을 확인하였으며, 특정 자동화 도구에 국한되지 않는 QA 자동화 역량을 확보하고자 하였습니다.

## 10. Installation & Execution

### Clone Repository

```bash
git clone https://github.com/Yonghyun1230/coupang-web-qa-automation.git
cd coupang-web-qa-automation
```

### Create Virtual Environment

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
python -m pip install -r requirements.txt
python -m playwright install chromium
```

### Run All Tests

```bash
python run.py
```

### Run Specific Test

```bash
python -c "import pytest; raise SystemExit(pytest.main(['-k', 'test_home_0001', '-v', '-s', '--headed']))"
```

### Generate HTML Report

```bash
python -c "import pytest; raise SystemExit(pytest.main(['tests', '-v', '--headed', '--html=reports/report.html', '--self-contained-html']))"
```

테스트 수행 완료 후 reports 디렉터리에서 HTML 결과 리포트를 확인할 수 있습니다.

## 11. Future Improvements

- [ ] 테스트케이스 및 자동화 검증 범위 확대
- [ ] 테스트 실패 시 스크린샷 자동 수집 및 리포트 첨부
- [ ] Logging 모듈을 활용한 수행 이력 관리
- [ ] 테스트 데이터 외부 파일 분리
- [ ] TC 명세서와 자동화 결과 연동
- [ ] Smoke / Regression 테스트 실행 환경 분리
- [ ] Cross Browser Testing
- [ ] Jenkins CI/CD 연동
- [ ] GitHub Actions 연동

## 12. Portfolio

- [QA Automation Portfolio (PDF)](docs/Coupang_QA_Portfolio_v2.pdf)

## 12. Disclaimer

본 프로젝트는 개인 학습 및 QA 자동화 역량 증명을 목적으로 제작되었으며, 쿠팡의 공식 프로젝트가 아닙니다.

외부 서비스의 보안 정책 및 접근 제한을 존중하며, 테스트 결과는 수행 환경 및 서비스 상태에 따라 달라질 수 있습니다.
