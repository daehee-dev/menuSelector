import random


def menuExceptButtonFunction(self):
    self.menuExceptButton.setText("선택된 메뉴 제외하고 재추천")
    self.menuList[self.randomMenuIndex].remove(self.selectedMenu)

    # 해당 인덱스의 배열이 비었을 경우 인덱스를 제거
    if self.menuList.count([]):
        self.menuIndex.remove(self.menuList.index([]))

        # 인덱스를 모두 소진하였을 경우 처리
        if len(self.menuIndex)==0:
            self.display.setText("더 이상 추천할 메뉴가 없습니다")
            # 버튼 1 비활성화, 버튼 2 자리에 버튼 3으로 대체
            self.menuSelectButton.setEnabled(False)
            self.menuSelectButton.setText("메뉴 추천")
            self.menuExceptButton.setVisible(False)
            self.menuResetButton.setVisible(True)
            # 각 체크박스 선택 불가능->이미 비어있는 인덱스에 대해서
            # 인덱스를 비우려고 할 수 있기 때문
            self.exceptKoreanMenu.setEnabled(False)
            self.exceptChineseMenu.setEnabled(False)
            self.exceptJapaneseMenu.setEnabled(False)
            self.exceptWesternMenu.setEnabled(False)
            self.exceptSnackMenu.setEnabled(False)
            return
        # 빈 배열을 없애버리면 인덱스 자체가 당겨지기 때문에
        # 빈 문자열로 인덱스를 채움.
        self.menuList[self.menuList.index([])]=""


    # 인덱스에서 하나를 선택
    self.randomMenuIndex=random.sample(self.menuIndex,1)[0]
    # 선택된 인덱스 중 다시 하나를 선택
    self.selectedMenu=random.sample(self.menuList[self.randomMenuIndex],1)[0]

    # 선택된 메뉴를 나타냄
    self.display.setText(self.selectedMenu)
