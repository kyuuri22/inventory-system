import json


class InventoryManager:
    def __init__(self):
        self.inventory = self._load()

    def _load(self):
        try:
            with open("inventory.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    # 共通: 在庫一覧を表示する
    def _show_inventory(self):
        print('現在の在庫')
        for item, data in self.inventory.items():
            print(f'{item}:{data["stock"]}')

    # 共通: 数値を入力させる（0以下はエラー）
    def _input_number(self, prompt):
        num_input = input(prompt)
        try:
            num = int(num_input)
            if num <= 0:
                print('1以上の数を入力してください')
                return None
            return num
        except ValueError:
            print('数字を入力してください')
            return None

    # 共通: 変更後に自動保存する
    def _save(self):
        with open("inventory.json", "w", encoding="utf-8") as f:
            json.dump(self.inventory, f, ensure_ascii=False, indent=4)

    # 1. 商品登録
    def register_item(self):
        item_name = input('商品名を入力してください:').strip()

        if item_name == '':
            print('商品名を入力してください')
        elif item_name in self.inventory:
            print('その商品は既に登録されています')
        else:
            self.inventory[item_name] = {'stock': 0}
            print(f'{item_name}を登録しました')
            self._save()

    # 2. 入庫
    def stock_in(self):
        if not self.inventory:
            print("商品が登録されていません")
            return

        self._show_inventory()
        item = input('入庫する商品を入力してください:').strip()

        if item not in self.inventory:
            print('商品が登録されていません')
            return

        num = self._input_number('入庫数を入力してください:')
        if num is not None:
            self.inventory[item]['stock'] += num
            print(f'現在の在庫は {self.inventory[item]["stock"]} 個')
            self._save()

    # 3. 出庫
    def stock_out(self):
        if not self.inventory:
            print("商品が登録されていません")
            return

        self._show_inventory()
        item = input('出庫する商品を入力してください:').strip()

        if item not in self.inventory:
            print('商品が登録されていません')
            return

        num = self._input_number('出庫数を入力してください:')
        if num is not None:
            if self.inventory[item]['stock'] >= num:
                self.inventory[item]['stock'] -= num
                print(f'現在の{item}の在庫は {self.inventory[item]["stock"]} 個')
                if self.inventory[item]['stock'] == 0:
                    print('在庫がゼロになりました!')
                self._save()
            else:
                print('在庫が足りません')

    # 4. 一覧表示
    def display_inventory(self):
        print('===在庫一覧===')
        if not self.inventory:
            print('在庫が登録されていません')
        else:
            for item, data in self.inventory.items():
                print(f'{item} : {data["stock"]}')

    # Web用: 商品削除
    def delete_item_web(self, item_name):
        if item_name not in self.inventory:
            return False, '商品が登録されていません'
        del self.inventory[item_name]
        self._save()
        return True, f'{item_name}を削除しました'

    # Web用: 入庫
    def stock_in_web(self, item, qty):
        if item not in self.inventory:
            return False, '商品が登録されていません'
        if qty <= 0:
            return False, '1以上の数を入力してください'
        self.inventory[item]['stock'] += qty
        self._save()
        return True, f'{item}を{qty}個入庫しました（現在: {self.inventory[item]["stock"]}個）'

    # Web用: 出庫
    def stock_out_web(self, item, qty):
        if item not in self.inventory:
            return False, '商品が登録されていません'
        if qty <= 0:
            return False, '1以上の数を入力してください'
        if self.inventory[item]['stock'] < qty:
            return False, f'在庫が足りません（現在: {self.inventory[item]["stock"]}個）'
        self.inventory[item]['stock'] -= qty
        self._save()
        return True, f'{item}を{qty}個出庫しました（現在: {self.inventory[item]["stock"]}個）'

    # Web用: 商品登録
    def register_item_web(self, item_name):
        item_name = item_name.strip()
        if item_name == '':
            return False, '商品名を入力してください'
        if item_name in self.inventory:
            return False, 'その商品は既に登録されています'
        self.inventory[item_name] = {'stock': 0}
        self._save()
        return True, f'{item_name}を登録しました'

    # 5. 商品削除
    def delete_item(self):
        if not self.inventory:
            print("商品が登録されていません")
            return

        self._show_inventory()
        item_name = input('削除する商品名を入力してください:').strip()

        if item_name not in self.inventory:
            print('商品が登録されていません')
            return

        confirm = input(f'"{item_name}"を削除しますか？ (y/n):').strip()
        if confirm == 'y':
            del self.inventory[item_name]
            print(f'{item_name}を削除しました')
            self._save()
        else:
            print('削除をキャンセルしました')

    # 6. 終了
    def exit(self):
        print("終了します。")

    # メインループ
    def run(self):
        while True:
            print('\n1.商品登録')
            print('2.入庫')
            print('3.出庫')
            print('4.一覧表示')
            print('5.商品削除')
            print('6.終了')

            choice = input('番号を選んでください:')

            if choice == '1':
                self.register_item()
            elif choice == '2':
                self.stock_in()
            elif choice == '3':
                self.stock_out()
            elif choice == '4':
                self.display_inventory()
            elif choice == '5':
                self.delete_item()
            elif choice == '6':
                self.exit()
                break
            else:
                print('無効な選択です。')


if __name__ == '__main__':
    app = InventoryManager()
    app.run()
