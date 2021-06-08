import psycopg2


def find(db, user, host, password, phones):
    try:
        connect_str = f"dbname='{db}' user='{user}' host='{host}' password='{password}'"
        conn = psycopg2.connect(connect_str)
        cursor = conn.cursor()
        cursor.execute("""SELECT phone1, description1, phone2, description2, phone3, description3 from \"user\"""")
        rows = cursor.fetchall()

        result = ""
        for row in range(len(rows)):
            one_str = ""
            filled = False
            for col in range(len(rows[row])):
                if col > 1 and clean_phone(rows[row][col - 1]) in phones:
                    continue
                if clean_phone(rows[row][col]) in phones:
                    one_str = one_str + "|" + clean_phone(rows[row][col]) + ", " + rows[row][col + 1] + "|"
                    filled = True
                else:
                    one_str = one_str + "|-, -|"
            if filled:
                result = result + one_str + "\r\n"

        cursor.close()
        conn.close()

        return result
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)


def clean_phone(raw_phone):
    if raw_phone is not None:
        raw_phone = raw_phone.replace("+7", "8")
        raw_phone = raw_phone.replace("НОЛЬ", "0")

    return raw_phone


if __name__ == "__main__":
    print(find(
        db="ultroizmuroma",
        user="postgres",
        host="localhost",
        password="",
        phones=["89107702801", "88002000600"]
    ))
