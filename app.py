from counter import Counter

if __name__ == "__main__":
    start_num = int(input("初期値は? > "))
    step = int(input("幅は? > "))
    counter = Counter(start_num, step)

    command = input("Command? > ")

    while command != "q":
        if command == "i":
            print("加算します")
            counter.increase()
            print(counter.value)
        else:
            print("そんなコマンド知らないよ")

        command = input("Command? > ")
    print("Bye!")
