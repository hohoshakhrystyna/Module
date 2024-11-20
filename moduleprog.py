import pandas as pd
import matplotlib.pyplot as plt
file_path = 'clients.csv'
try:
    orders_df = pd.read_csv(file_path, encoding='utf-8')
    print("Дані завантажені успішно.")
except FileNotFoundError:
    print("Файл не знайдено. Створюється порожній DataFrame.")
    orders_df = pd.DataFrame(columns=["Ім'я клієнта", "Номер замовлення", "Дата замовлення", "Сума замовлення", "Статус"])

def add_order():
    global orders_df
    print("\nДодати нове замовлення:")
    client_name = input("Введіть ім'я клієнта: ")
    order_number = int(input("Введіть номер замовлення: "))
    order_date = input("Введіть дату замовлення (YYYY-MM-DD): ")
    order_amount = float(input("Введіть суму замовлення: "))
    status = input("Введіть статус (Виконано/В процесі): ")
    new_order = {
        "Ім'я клієнта": client_name,
        "Номер замовлення": order_number,
        "Дата замовлення": order_date,
        "Сума замовлення": order_amount,
        "Статус": status
    }
    orders_df = pd.concat([orders_df, pd.DataFrame([new_order])], ignore_index=True)
    print("Замовлення додано.")

def edit_order():
    global orders_df
    print("\nРедагувати замовлення:")
    order_number = int(input("Введіть номер замовлення: "))
    if order_number in orders_df["Номер замовлення"].values:
        print("Введіть нові дані (натисніть Enter, щоб залишити без змін):")
        client_name = input("Ім'я клієнта: ")
        order_date = input("Дата замовлення (YYYY-MM-DD): ")
        order_amount = input("Сума замовлення: ")
        status = input("Статус (Виконано/В процесі): ")
        if client_name:
            orders_df.loc[orders_df["Номер замовлення"] == order_number, "Ім'я клієнта"] = client_name
        if order_date:
            orders_df.loc[orders_df["Номер замовлення"] == order_number, "Дата замовлення"] = order_date
        if order_amount:
            orders_df.loc[orders_df["Номер замовлення"] == order_number, "Сума замовлення"] = float(order_amount)
        if status:
            orders_df.loc[orders_df["Номер замовлення"] == order_number, "Статус"] = status
        print("Замовлення оновлено.")
    else:
        print("Замовлення з таким номером не знайдено.")

def delete_order():
    global orders_df
    print("\nВидалити замовлення:")
    order_number = int(input("Введіть номер замовлення: "))
    if order_number in orders_df["Номер замовлення"].values:
        orders_df = orders_df[orders_df["Номер замовлення"] != order_number]
        print("Замовлення видалено.")
    else:
        print("Замовлення з таким номером не знайдено.")

def show_orders():
    print("\nСписок всіх замовлень:")
    if orders_df.empty:
        print("Немає жодного замовлення.")
    else:
        print(orders_df)

def analyze_orders():
    print("\nАналіз замовлень:")
    total_orders = len(orders_df)
    total_amount = orders_df["Сума замовлення"].sum()
    print(f"Загальна кількість замовлень: {total_orders}")
    print(f"Сумарна вартість замовлень: {total_amount:.2f}")

def analyze_status():
    print("\nАналіз замовлень за статусом:")
    status_counts = orders_df["Статус"].value_counts()
    print(status_counts)

def find_max_order():
    print("\nЗамовлення з найбільшою сумою:")
    if not orders_df.empty:
        max_order = orders_df.loc[orders_df["Сума замовлення"].idxmax()]
        print(max_order)
    else:
        print("Немає замовлень.")

def save_to_csv():
    orders_df.to_csv(file_path, index=False, encoding='utf-8')
    print("Дані збережено у файл.")

def pie():
    print("\nПобудова кругової діаграми...")
    if not orders_df.empty:
        status_counts = orders_df["Статус"].value_counts()
        plt.figure(figsize=(6, 6))
        plt.pie(
            status_counts,
            labels=status_counts.index,
            autopct='%1.1f%%',
            colors=['#66c2a5', '#fc8d62'],
            startangle=140
        )
        plt.title("Частка виконаних і невиконаних замовлень")
        plt.show()
    else:
        print("Дані для побудови кругової діаграми відсутні.")

def histogram():
    print("\nПобудова гістограми кількості замовлень за датами...")
    if not orders_df.empty:
        orders_df['Дата замовлення'] = pd.to_datetime(orders_df['Дата замовлення'], errors='coerce')
        if orders_df['Дата замовлення'].isnull().any():
            print("Увага: є некоректні дати. Вони будуть пропущені.")
        orders_by_date = orders_df['Дата замовлення'].value_counts().sort_index()

        plt.figure(figsize=(10, 5))
        plt.bar(orders_by_date.index, orders_by_date.values, color='#8da0cb')
        plt.title("Кількість замовлень за датами")
        plt.xlabel("Дата")
        plt.ylabel("Кількість замовлень")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print("Дані для побудови гістограми відсутні.")

def menu():
    while True:
        print("\nМеню:")
        print("1. Всі замовлення")
        print("2. Додати замовлення")
        print("3. Редагувати замовлення")
        print("4. Видалити замовлення")
        print("5. Аналіз замовлень")
        print("6. Аналіз за статусом")
        print("7. Замовлення з найбільшою сумою")
        print("8. Кругова діаграма")
        print("9. Гістограма")
        print("10. Зберегти дані у файл")
        print("11. Вийти")
        choice = input("Виберіть номер: ")
        if choice == "1":
            show_orders()
        elif choice == "2":
            add_order()
        elif choice == "3":
            edit_order()
        elif choice == "4":
            delete_order()
        elif choice == "5":
            analyze_orders()
        elif choice == "6":
            analyze_status()
        elif choice == "7":
            find_max_order()
        elif choice == "8":
            pie()
        elif choice == "9":
            histogram()
        elif choice == "10":
            save_to_csv()
        elif choice == "11":
            print("Завершено.")
            break
        else:
            print("Невірно.Спробуйте ще раз.")

menu()
