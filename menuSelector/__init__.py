# Qapplication(QT5 GUI 프로그램) 실행을 위한 sys,
# 임의의 메뉴 선택을 위한 random 모듈 import
import sys, random
# GUI 화면을 띄우기 위한
# PyQt5.QtWidgets 내 모든 모듈 import
from PyQt5.QtWidgets import *
# UI 파일을 연결하기 위한 PyQt5 내 uic 모듈 import
from PyQt5 import uic
# 메뉴 제외 버튼 모듈 import
from menuSelector.exceptButton import menuExceptButtonFunction
# 메뉴 제외 체크박스 모듈 import
from menuSelector.exceptCheck import menuExceptCheckFunction
# 메뉴 초기화 버튼 모듈 import
from menuSelector.resetButton import menuResetFunction
# 메뉴 선택 버튼 모듈 import
from menuSelector.selectButton import menuSelectFunction

# UI 파일 연결
form_class = uic.loadUiType("menuSelector.ui")[0]

# 화면을 출력 할 WindowClass class 선언
# QMainWindow, form_class 부모 class 상속
class WindowClass(QMainWindow, form_class):
    # 메뉴 제외의 라벨을 위한 변수 menu 선언
    menu = ["한식 ", "중식 ", "일식 ", "양식 ", "분식 "]
    # 메뉴 제외를 위한 변수 menuIndex 선언
    menuIndex = [0, 1, 2, 3, 4]
    # 초기 메뉴 선택을 위한 변수 randomMenuIndex 선언
    randomMenuIndex = random.randint(0, 4)

    # 메뉴목록 데이터베이스 menuList 선언
    menuList = [
        ["불고기", "된장찌개", "김치찌개", "육개장", "비빔밥", "청국장", "김치볶음밥", "죽", "냉면", "국수", "갈비탕", "감자탕", "국밥", "매운탕", "부대찌개", "전골", "갈비찜", "수육", "족발", "제육볶음", "삼겹살", "명태찜", "전", "게장", "잡채", "찜닭"],
        ["짜장면", "짬뽕", "탕수육", "고추잡채", "깐풍기", "마파두부", "잡채밥", "중식볶음밥", "우육탕", "꿔바로우","동파육", "라조기", "팔보채", "난자완스", "칠리새우", "양장피"],
        ["돈까스", "라멘", "초밥", "돈부리", "우동", "야끼우동", "소바", "야끼소바", "오코노미야끼", "샤브샤브", "규카츠"],
        ["피자", "치킨", "스테이크", "햄버거", "토스트", "파스타", "필라프", "부리또"],
        ["떡볶이", "라면", "라볶이", "김밥", "타꼬야끼", "만두"]
    ]
    # menuList 백업 데이터베이스 menuList_backup 선언
    menuList_backup = [
        ["불고기", "된장찌개", "김치찌개", "육개장", "비빔밥", "청국장", "김치볶음밥", "죽", "냉면", "국수", "갈비탕", "감자탕", "국밥", "매운탕", "부대찌개", "전골", "갈비찜", "수육", "족발", "제육볶음", "삼겹살", "명태찜", "전", "게장", "잡채", "찜닭"],
        ["짜장면", "짬뽕", "탕수육", "고추잡채", "깐풍기", "마파두부", "잡채밥", "중식볶음밥", "우육탕", "꿔바로우","동파육", "라조기", "팔보채", "난자완스", "칠리새우", "양장피"],
        ["돈까스", "라멘", "초밥", "돈부리", "우동", "야끼우동", "소바", "야끼소바", "오코노미야끼", "샤브샤브", "규카츠"],
        ["피자", "치킨", "스테이크", "햄버거", "토스트", "파스타", "필라프", "부리또"],
        ["떡볶이", "라면", "라볶이", "김밥", "타꼬야끼", "만두"]
    ]

    # 생성자 함수 선언
    def __init__(self):
        # 부모의 생성자 함수 호출
        super().__init__()
        # 화면을 그리기 위한 setupUi 함수 호출
        self.setupUi(self)

        # 초기에 메뉴 제외버튼 비가시화
        self.menuExceptButton.setVisible(False)
        # 초기에 메뉴 리셋버튼 비가시화
        self.menuResetButton.setVisible(False)


        # 각 버튼 클릭되거나 체크박스
        # 변화가 있을 때 실행 될 함수 연결
        self.menuSelectButton.clicked.connect(lambda: menuSelectFunction(self))
        self.exceptKoreanMenu.stateChanged.connect(lambda: menuExceptCheckFunction(self))
        self.exceptChineseMenu.stateChanged.connect(lambda: menuExceptCheckFunction(self))
        self.exceptJapaneseMenu.stateChanged.connect(lambda: menuExceptCheckFunction(self))
        self.exceptWesternMenu.stateChanged.connect(lambda: menuExceptCheckFunction(self))
        self.exceptSnackMenu.stateChanged.connect(lambda: menuExceptCheckFunction(self))
        self.menuExceptButton.clicked.connect(lambda: menuExceptButtonFunction(self))
        self.menuResetButton.clicked.connect(lambda: menuResetFunction(self))

# 이 모듈이 메인일 때 실행
if __name__ == "__main__":

    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
