from function import summ as s


def main():
    '''
    Точка входа программы
    :return: None
    '''

    try:
        a, b = map(int, input('Введите значения а и б разделя пробелом: ').split())
    except Exception as e:
        print(f'Твоя ошбка - {e}')
    finally:
        print(s(a, b))


if __name__ == '__main__':
    main()
