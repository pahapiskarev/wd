conversion_to_meters = {
    'км': 1000,
    'м': 1,
    'см': 0.01,
    'мм': 0.001,
    'mi': 1609.344,
    'yd': 0.9144
}

def get_unit_choice(prompt, available_units):
    while True:
        print(prompt)
        for i, (key, desc) in enumerate(available_units.items(), 1):
            print(f"{i}. {desc} ({key})")

        try:
            choice = int(input("Выберите номер: "))
            if 1 <= choice <= len(available_units):
                unit_key = list(available_units.keys())[choice - 1]
                return unit_key
            else:
                print(f"Пожалуйста, выберите число от 1 до {len(available_units)}")
        except ValueError:
            print("Пожалуйста, введите число")

def main():
    unit_descriptions = {
        'км': 'Километры',
        'м': 'Метры',
        'см': 'Сантиметры',
        'мм': 'Миллиметры',
        'mi': 'Мили',
        'yd': 'Ярды'
    }

    print("Выберите исходную единицу измерения:")
    from_unit = get_unit_choice("Из какой единицы конвертируем?", unit_descriptions)

    print("\nВыберите целевую единицу измерения:")
    to_unit = get_unit_choice("В какую единицу конвертируем?", unit_descriptions)

    while True:
        try:
            value = float(input(f"\nВведите значение в {unit_descriptions[from_unit]}: "))
            if value < 0:
                print("Значение не может быть отрицательным. Попробуйте снова.")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите число")

    value_in_meters = value * conversion_to_meters[from_unit]

    result = value_in_meters / conversion_to_meters[to_unit]

    print("\n" + "=" * 50)
    print(f"Результат конвертации:")
    print(f"{value} {unit_descriptions[from_unit]} = {result:.6f} {unit_descriptions[to_unit]}")
    print("=" * 50)


if __name__ == "__main__":
    main()