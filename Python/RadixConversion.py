class RadixConversion:
    """
    進数を変換するクラス
    """

    def decimal_to_binary():
        """_10進数から2進数に変換する"""
        print("10進数を入力してください")
        N = int(input())
        answer = ""
        while N >= 1:
            if N % 2 == 0:
                answer = "0" + answer
            if N % 2 == 1:
                answer = "1" + answer
            N = N // 2
        print(" 2進数：%s" % answer)

    def binary_to_decimal():
        """2進数から10進数に変換する"""
        print("2進数を入力してください")
        int_val, i, tmp = 0, 0, 0
        N = int(input())
        while N != 0:
            tmp = N % 10
            int_val = int_val + tmp * pow(2, i)
            N = N // 10
            i += 1
        print(int_val)

    # decimal_to_binary()
    binary_to_decimal()
