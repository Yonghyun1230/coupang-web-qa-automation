import pytest
from pathlib import Path
from datetime import datetime


if __name__ == "__main__":

    Path("reports").mkdir(exist_ok=True)

    # 테스트 수행 시간
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # 리포트 파일 경로
    report_path = f"reports/report_{timestamp}.html"

    raise SystemExit(
        pytest.main([
            "tests",
            "-v",
            "-s",
            "--headed",
            "--html=reports/report.html",
            "--self-contained-html"
        ])
    )