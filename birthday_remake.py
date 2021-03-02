import datetime
dt_now = datetime.datetime.now()

#利用者の生年を入力してyearに代入
def input_year():
    year = input("あなたの生まれた年（西暦）を入力してください:")
    year_age = dt_now.year - int(year)

    return year_age

#利用者の生月を入力してmonthに代入
def input_month():
    month = input("あなたの生まれた月を入力してください:")

    return int(month)

#日付入力
def input_day():
    day = input("あなたの生まれた日を入力してください:")

    return int(day)

#日付から年齢判定
def enzan_day():
    kakutei_day = input_day()

    if kakutei_day <= dt_now.day :
            age_d = input_year()
            return age_d

    elif kakutei_day > dt_now.day :
            age_d = input_year() - 1
            return age_d

#代入された月日から年齢を判定
def enzan_month():
    kakutei_month = input_month()

    if kakutei_month < dt_now.month :
        age = input_year()
        return age

    elif kakutei_month > dt_now.month:
        age = input_year() - 1
        return age
    
    elif kakutei_month == dt_now.month:
        age = enzan_day()
        return age

#特定した年齢をコンソールに出力
def age():
    print("あなたの年齢は" + str(enzan_month()) + "歳です")

age()
