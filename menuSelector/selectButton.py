import random


def menuSelectFunction(self):
    self.menuSelectButton.setText("메뉴 재추천")
    self.randomMenuIndex = random.sample(self.menuIndex, 1)[0]
    self.selectedMenu = random.sample(self.menuList[self.randomMenuIndex], 1)[0]
    self.display.setText(self.selectedMenu)
    self.menuExceptButton.setVisible(True)
