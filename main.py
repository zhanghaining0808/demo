import questionary

def main():
    bank_list = [f"{bank}银行" for bank in  ["农业","工商","建设","交通"]]
    now_select = questionary.select("choose your bank?",bank_list).ask()
    print(now_select)

if __name__ == "__main__":
    main()