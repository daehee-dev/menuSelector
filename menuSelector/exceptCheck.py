import copy
import random


def menuExceptCheckFunction(self):
    labelSetter = "제외하고 메뉴 선택"
    # 0:한식 1:중식 2:일식 3:양식 4:분식, 인덱스 초기화
    self.menuIndex = [0, 1, 2, 3, 4]
    # 메뉴 초기화
    self.menuList = copy.deepcopy(self.menuList_backup)
    self.menuSelectButton.setText("메뉴 추천")
    self.menuExceptButton.setVisible(False)

    # 제외 메뉴 인덱스 제거
    if self.exceptKoreanMenu.isChecked():
        labelSetter = self.menu[0] + labelSetter
        self.menuIndex.remove(0)

    if self.exceptChineseMenu.isChecked():
        labelSetter = self.menu[1] + labelSetter
        self.menuIndex.remove(1)
    if self.exceptJapaneseMenu.isChecked():
        labelSetter = self.menu[2] + labelSetter
        self.menuIndex.remove(2)

    if self.exceptWesternMenu.isChecked():
        labelSetter = self.menu[3] + labelSetter
        self.menuIndex.remove(3)

    if self.exceptSnackMenu.isChecked():
        labelSetter = self.menu[4] + labelSetter
        self.menuIndex.remove(4)

    # 인덱스가 없을 시 처리
    if not len(self.menuIndex):
        self.display.setText("추천할 메뉴가 없습니다")
        self.menuSelectButton.setEnabled(False)
        self.menuExceptButton.setEnabled(False)
    # 메뉴의 개수가 그대로라면
    elif len(self.menuIndex) == len(self.menu):
        self.display.setText("메뉴를 추천해 주세요")
    else:
        self.menuSelectButton.setEnabled(True)
        self.menuExceptButton.setEnabled(True)
        # 인덱스가 없을 시 버튼 1,2 비활성화, 그 외 활성화
        self.randomMenuIndex = random.sample(self.menuIndex, 1)
        self.display.setText(labelSetter)
