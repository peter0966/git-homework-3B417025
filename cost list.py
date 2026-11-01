expenses = []

while True:
    print("--- 消費紀錄統計系統 ---")
    print("1. 新增消費")
    print("2. 顯示消費明細")
    print("3. 顯示統計")
    print("4. 退出系統")
    print("-----------------------------")

    choice = input("請選擇功能: ")

    if choice == "1":
        item = input("請輸入消費項目: ")

        while True:
            price = input("請輸入消費金額: ")

            if price == "":
                print("金額不可為空，請重新輸入")

            else:
                dot_count = 0
                valid = True

                for char in price:

                    if char == ".":
                        dot_count += 1

                    elif char < "0" or char > "9":
                        valid = False

                if dot_count > 1:
                    valid = False

                if price[0] == "." or price[-1] == ".":
                    valid = False

                if valid == True:
                    price = float(price)

                    if price > 0:
                        break
                    else:
                        print("金額必須大於 0，請重新輸入")
                else:
                    print("金額格式錯誤，請重新輸入")

        new_expense = {
            "項目": item,
            "金額": price
        }

        expenses.append(new_expense)
        print("新增成功\n")

    elif choice == "2":
        if not expenses:
            print("目前沒有消費紀錄\n")

        else:
            print("--- 消費明細: ---")
            print(f"{'編號':>2}  {'項目':<12} {'金額':>6}")
            print("-----------------------------")
            index = 1

            for expense in expenses:
                print(f"{index:>4}  {expense['項目']:<12} {expense['金額']:>10.2f}")
                index += 1

            print()

    elif choice == "3":
        if not expenses:
            print("目前沒有消費紀錄\n")

        else:
            total = 0

            for expense in expenses:
                total += expense["金額"]

            count = len(expenses)
            average = total / count

            print("--- 消費統計: ---")
            print(f"消費筆數: {count}")
            print(f"總消費金額: {total:.2f}")
            print(f"平均消費金額: {average:.2f}")
            print("-----------------------------")
            if total < 300:
                print("消費不多")

            elif total < 500:
                print("注意控制消費")

            else:
                print("已達提醒門檻")

            print()

    elif choice == "4":
        print("系統已退出")
        break

    else:
        print("選項錯誤，請重新選擇\n")