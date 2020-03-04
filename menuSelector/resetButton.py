import copy


def menuResetFunction(self):
    # 메뉴목록 초기화
    self.menuList = copy.deepcopy(self.menuList_backup)
    self.menuIndex = [0, 1, 2, 3, 4]


    # 버튼 1 활성화, 버튼 3 비가시화
    self.menuSelectButton.setEnabled(True)
    self.menuResetButton.setVisible(False)

    # 체크박스 체크 해제
    self.exceptKoreanMenu.setChecked(False)
    self.exceptChineseMenu.setChecked(False)
    self.exceptJapaneseMenu.setChecked(False)
    self.exceptWesternMenu.setChecked(False)
    self.exceptSnackMenu.setChecked(False)

    # 체크박스 활성화
    self.exceptKoreanMenu.setEnabled(True)
    self.exceptChineseMenu.setEnabled(True)
    self.exceptJapaneseMenu.setEnabled(True)
    self.exceptWesternMenu.setEnabled(True)
    self.exceptSnackMenu.setEnabled(True)

    self.display.setText("메뉴가 초기화 되었습니다")
